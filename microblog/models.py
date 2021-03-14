from sqlalchemy import *
from core.db import Base
from sqlalchemy.orm import *

from user.models import User


class Post(Base):
    __tablename__ = "microblog_posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)