from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(platin_password: str, hashed_password:str):
    return pwd_context.verify(platin_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)