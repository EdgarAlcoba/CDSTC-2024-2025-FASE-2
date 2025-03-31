from fastapi import HTTPException
from sqlmodel import select
from passlib.hash import argon2
import random
import string

from ..utils.db import get_session
from ..dto.user import User

class Users:
    @staticmethod
    def create(name: str, surname: str, email: str, password: str, mock: bool, role: str = "basic"):
        session = next(get_session())
        db_emails: list[User] = session.exec(select(User).where(User.email == email)).all()
        if len(db_emails) > 0:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )
        profile_picture = "default_profile_picture.png"
        if mock:
            profile_picture = "default_profile_picture_demo.png"
        new_user = User(
            name=name, surname=surname, email=email,
            password=argon2.hash(password),
            mock=mock, role=role,
            profile_picture=profile_picture
        )
        session.add(new_user)
        session.commit()


    @staticmethod
    def verify_password(email: str, password: str) -> User:
        session = next(get_session())
        db_emails: list[User] = session.exec(select(User).where(User.email == email)).all()
        if len(db_emails) < 1:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        if not argon2.verify(password, db_emails[0].password):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        return db_emails[0]

    @staticmethod
    def find_by_id(user_id: int) -> User|None:
        session = next(get_session())
        db_users: list[User] = session.exec(select(User).where(User.id == user_id)).all()
        if len(db_users) < 1:
            return None
        return db_users[0]

    @staticmethod
    def get_random_string(length) -> str:
        letters: str = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def generate_random(num_reviews: int, comments_per_user: int=4) -> list[User]:
        session = next(get_session())
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
                password = argon2.hash(Users.get_random_string(5)),
                profile_picture = "default_profile_picture_demo.png"
            ))

        session.add_all(users_to_create)
        session.commit()

        db_users: list[User] = \
            session.exec(select(User).where(User.mock == True)).all()

        return db_users
