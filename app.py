from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import cryptn
import psycopg2
import auth
import psycopg2.extras
from datetime import timedelta, datetime, timezone

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount(
    "/static",
    StaticFiles(directory="static", html=True, check_dir=True),
    name="static"
)
def connect_postgre():
    return psycopg2.connect(
        'postgresql://neondb_owner:npg_pJMuRjab9C1P@ep-fragrant-shape-a1fmjn84-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
    )

# --- Database Initialization ---
def init_db():
    conn = connect_postgre()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY ,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- User helpers ---
def createuser(name, password):
    conn = connect_postgre()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (name, cryptn.create_hash_pass(password))  # FIXED: Added missing closing parenthesi
    )
    conn.commit()
    conn.close()

def checkuser(name):
    conn = connect_postgre()
    # cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (name,))
    k = cur.fetchone()
    conn.close()
    return k

# --- Routes ---
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home Page"})

@app.get("/register", response_class=HTMLResponse)
async def to_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register Page"})

@app.get("/login", response_class=HTMLResponse)
async def to_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login Page"})

@app.post("/register", response_class=HTMLResponse)
async def do_register(request: Request, username: str = Form(...), password: str = Form(...)):
    k = checkuser(username)
    if not k:
        createuser(username, password)
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register Failed"})

@app.post("/login", response_class=HTMLResponse)
async def do_login(request: Request, username: str = Form(...), password: str = Form(...)):
    k = checkuser(username)

    if k is None:
        return templates.TemplateResponse("login.html", {"request": request, "title": "Invalid Username"})

    try:
        if cryptn.check_password(password, k[2]):
            data = {"sub": username}
            token = auth.create_access_token(data, timedelta(minutes=30))
            response = RedirectResponse(url="/dashboard", status_code=303)
            response.set_cookie(key="token", value=token, httponly=True, max_age=1800)
            return response
        else:
            return templates.TemplateResponse("login.html", {"request": request, "title": "Invalid Password"})
    except Exception as e:
        return templates.TemplateResponse("login.html", {"request": request, "title": f"Login Error: {str(e)}"})

@app.get("/dashboard")
async def dashboard(request: Request):
    token = request.cookies.get("token")
    if not token:
        return RedirectResponse(url="/login", status_code=303)

    k = auth.decode(token)
    if not k:
        return RedirectResponse(url="/login", status_code=303)

    exp = datetime.fromtimestamp(k["exp"])

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "title": "Dashboard",
        "token": token,
        "decode": k,
        "time": exp
    })