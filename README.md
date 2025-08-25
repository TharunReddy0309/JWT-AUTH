📖 README.md
# 🔐 FastAPI Authentication System (JWT + PostgreSQL)

This project is a simple **authentication system** built with:
- [FastAPI](https://fastapi.tiangolo.com/) 🚀
- **PostgreSQL** (user database)
- **JWT** (JSON Web Tokens) for session management
- **Passlib (bcrypt)** for secure password hashing
- **Jinja2 Templates** for frontend rendering

---

## ✨ Features
- ✅ User Registration (username + password, securely hashed)
- ✅ User Login (with JWT token stored in HTTP-only cookies)
- ✅ Dashboard (only accessible with a valid token)
- ✅ Passwords hashed with bcrypt (never stored in plain text)
- ✅ PostgreSQL as the database backend

---

## 📂 Project Structure


.
├── app.py # Main FastAPI app (routes & logic)
├── auth.py # JWT creation & decoding
├── cryptn.py # Password hashing/verification
├── templates/ # HTML templates (Jinja2)
│ ├── home.html
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
├── requirements.txt # Dependencies
└── README.md # Documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/fastapi-auth.git
cd fastapi-auth

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root:

secret_key=your_secret_key_here
algo=HS256
DATABASE_URL=postgresql://username:password@localhost:5432/yourdbname

5️⃣ Initialize Database

Run the app once, it will automatically create the users table in PostgreSQL.

Or manually:

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

6️⃣ Run the App
uvicorn app:app --reload


Visit:

🏠 Home → http://127.0.0.1:8000/

🔑 Register → http://127.0.0.1:8000/register

🔓 Login → http://127.0.0.1:8000/login

📊 Dashboard → http://127.0.0.1:8000/dashboard

🧑‍💻 Usage Flow

Go to Register Page → create a new account.

Login with your credentials.

On success, a JWT token is stored in cookies.

Visit the Dashboard → shows user & token expiry info.

Without a valid token → you’ll be redirected back to login.

📦 Requirements

Add this in requirements.txt:

fastapi
uvicorn
jinja2
python-jose
passlib[bcrypt]
python-dotenv
psycopg2-binary    # for PostgreSQL

🔐 Security Notes

Passwords are stored only as bcrypt hashes.

JWT tokens are stored in HTTP-only cookies (not accessible via JavaScript).

Make sure to use a strong SECRET_KEY in production.

Always run with HTTPS in production.

📌 Future Improvements

🔄 Add Logout functionality (clear JWT cookie).

🔑 Role-based access (Admin/User).

📬 Email verification on signup.

🐳 Docker support for easy deployment.

👨‍💻 Author

Built by Tharun✨