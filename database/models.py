from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)

    health_records = relationship("UserHealthData", back_populates="user")


class UserHealthData(Base):
    __tablename__ = "health_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float)
    height = Column(Float)
    gender = Column(String)
    pulse = Column(Integer)

    user = relationship("User", back_populates="health_records")
