
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    TEXT,
    DateTime,
    ForeignKey
) 
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(200),unique=True, nullable=False)
    email = Column(String(64))
    created_at = Column(DateTime,default=datetime.utcnow)
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(TEXT)
    body = Column(String(126))
    user_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime,default=datetime.utcnow)
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer,primary_key=True,index=True)
    text = Column(TEXT)
    post_id = Column(Integer,ForeignKey("posts.id"))
    user_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime,default=datetime.utcnow)
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
