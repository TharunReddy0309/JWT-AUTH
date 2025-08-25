from datetime import datetime, timedelta, timezone
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("secret_key")  # FIXED: Better default
ALGORITHM = os.getenv("algo")
TIME = 30  # minutes

def create_access_token(data: dict, expiredate: timedelta | None = None):
    to_encode = data.copy()
    # FIXED: Use timezone-aware datetime instead of deprecated utcnow()
    expire = datetime.now(timezone.utc) + (expiredate if expiredate else timedelta(minutes=TIME))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # must be list
    except Exception:
        return None