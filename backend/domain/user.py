from sqlalchemy import Column, Integer, String

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    vectorization = Column(String, nullable=True)
    cluster = Column(Integer, nullable=True)
    fullname = Column(String, index=True)

    def __str__(self):
        return str(self.id) + " " + self.username + " " + self.fullname +\
               " " + self.hashed_password + " " + self.vectorization + " " + str(self.cluster) + "\n"

