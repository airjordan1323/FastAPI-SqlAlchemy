from sqlalchemy import *
from core.db import Base
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)

# class User(Base, SQLAlchemyBaseUserTable):
#     __tablename__ = "user"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     name = Column(String, unique=True)
#     email = Column(String, unique=True)
#     password = Column(String)
#     date = Column(DateTime)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
