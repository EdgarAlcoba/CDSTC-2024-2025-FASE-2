from http.client import HTTPException

from fastapi import FastAPI, Depends
from sqlmodel import select
from passlib.context import CryptContext
import random
import string

from ..utils.db import get_session
from ..dto.user import User

class Users:
    @staticmethod
    def get_random_string(length) -> str:
        letters: str = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def generate_random(num_reviews: int, comments_per_user: int=4) -> list[User]:
        session = next(get_session())
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        num_users_to_create: int = int(num_reviews / comments_per_user)

        # Check if the database has already that many mock users
        existing_mock_user_count: int = len(list(session.exec(select(User).where(User.mock == True))))

        if existing_mock_user_count < num_users_to_create:
            num_users_to_create = num_users_to_create - existing_mock_user_count

        users_to_create: list[User] = []
        for i in range(0, num_users_to_create):
            users_to_create.append(User(
                name= Users.get_random_string(20),
                surname= Users.get_random_string(20),
                email = f"{Users.get_random_string(20)}@random.rand",
                password = pwd_context.hash(Users.get_random_string(5))
            ))

        session.add_all(users_to_create)
        session.commit()

        db_users: list[User] = \
            session.exec(select(User).where(User.mock == True)).all()

        return db_users
