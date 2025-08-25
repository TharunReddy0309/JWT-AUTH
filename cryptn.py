from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_password(user_password, hashed_password):
    return pwd_context.verify(user_password, hashed_password)

def create_hash_pass(user_password):
    return pwd_context.hash(user_password)
