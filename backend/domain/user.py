from sqlalchemy import Column, Integer, String

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    fullname = Column(String, index=True)



