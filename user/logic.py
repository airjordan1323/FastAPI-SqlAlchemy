from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db import database
from .models import User
from .schemas import UserDB


users = User.__tablename__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "bu2buy15563b46uyhb47boi1u234oboiub53biu23"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)