from sqlalchemy.orm import Session

from db.base_class import Base
from db.session import engine
from db import base


def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
