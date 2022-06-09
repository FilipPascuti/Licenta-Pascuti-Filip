import logging
import pandas as pd

from db.init_db import init_db
from db.session import SessionLocal
from sqlalchemy.orm import Session
from core.security import get_password_hashed, verify_password
from domain.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)
    populate_db(db)


def create_user_from_list(values):
    fullname = values[1]
    password = fullname.replace(" ", "").lower()
    hashed_password = get_password_hashed(password)
    username = password + "@gmail.com"
    cluster = values[-1]
    vectorization = ""
    for percentage in values[2:-1]:
        vectorization += str(percentage) + ","
    vectorization = vectorization[:-1]
    return User(
        username=username,
        hashed_password=hashed_password,
        fullname=fullname,
        vectorization=vectorization,
        cluster=cluster
    )


def populate_db(db: Session):
    df = pd.read_csv("resources/artists_clustered.csv")
    artists = []
    usernames = []
    for index, row in df.iterrows():
        print(f"at index {index}")
        values = row.tolist()
        artist = create_user_from_list(values)
        if artist.username not in usernames:
            artists.append(artist)
            usernames.append(artist.username)
        #
        # if index >= 1000:
        #     break

    db.add_all(artists)
    db.commit()


def main():
    logger.info("creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
