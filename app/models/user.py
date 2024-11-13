import os

from sqlalchemy import Column, Integer, String, create_engine
from app.core.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)