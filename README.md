# FastAPI Authentication System (JWT + PostgreSQL)

A simple authentication system built using:

- FastAPI
- PostgreSQL
- JWT Authentication
- Passlib (bcrypt)
- Jinja2 Templates

### Live Demo

```text
https://jwt-auth-no4z.onrender.com
```

---

# Features

- User Registration
- Secure Password Hashing with bcrypt
- JWT-based Authentication
- HTTP-only Cookie Sessions
- Protected Dashboard Route
- PostgreSQL Database Integration

---

# Project Structure

```text
.
├── app.py              # Main FastAPI application
├── auth.py             # JWT creation & verification
├── cryptn.py           # Password hashing utilities
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── requirements.txt
└── README.md
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/fastapi-auth.git
cd fastapi-auth
```

---

## 2. Create Virtual Environment

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
secret_key=your_secret_key_here
algo=HS256
DATABASE_URL=postgresql://username:password@localhost:5432/yourdbname
```

---

## 5. Initialize Database

The app automatically creates the `users` table on startup.

Or create manually:

```sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
```

---

## 6. Run the Application

```bash
uvicorn app:app --reload
```

---

# Routes

| Route | Description |
|---|---|
| `/` | Home Page |
| `/register` | User Registration |
| `/login` | User Login |
| `/dashboard` | Protected Dashboard |

---

# Usage Flow

1. Register a new account  
2. Login with credentials  
3. JWT token is stored in HTTP-only cookies  
4. Access protected dashboard  
5. Invalid token redirects to login page  

---

# Requirements

```txt
fastapi
uvicorn
jinja2
python-jose
passlib[bcrypt]
python-dotenv
psycopg2-binary
```

---

# Security Features

- Passwords stored as bcrypt hashes
- JWT stored in HTTP-only cookies
- Secure token verification
- PostgreSQL database backend

---

# Future Improvements

- Logout functionality
- Role-based authentication
- Email verification
- Docker deployment support

---

# Author

Built by **Tharun**
