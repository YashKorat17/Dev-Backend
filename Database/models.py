from sqlalchemy import Boolean, Column, Integer, String,BLOB,Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)



class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(BLOB, nullable=True)
    name = Column(String)
    number = Column(Integer)
    gender = Column(String)
    premium = Column(Integer)
    premium_validity = Column(String)
    payment_type = Column(String)
    batch_code = Column(String)
    batch_no = Column(Integer)
    date = Column(Date)
