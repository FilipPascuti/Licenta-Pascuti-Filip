from typing import Optional

from sqlalchemy.orm import Session

from domain.user import User


class UserRepo:
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get(self, db: Session, id: int) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def create(self, db: Session, *, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, *, user_in: User, vectorization: str, cluster: int):
        user_in.vectorization = vectorization
        user_in.cluster = cluster
        db.add(user_in)
        db.commit()
        db.refresh(user_in)
        return user_in

    def get_all_from_cluster(self, db: Session, *, cluster: int):
        users = db.query(User).filter(User.cluster == cluster).all()
        return users


user_repo = UserRepo()
