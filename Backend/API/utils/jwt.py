from http.client import HTTPException

from fastapi import Request
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

from ..utils.constants import init as get_constants

class JWT:
    @staticmethod
    def create_token(data: dict, expires_delta: timedelta | None = None) -> str:
        constants = get_constants()
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=constants["JWT_EXPIRE_MINUTES"])
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=constants["JWT_SECRET_KEY"],
            algorithm=constants["JWT_ALGORITHM"]
        )
        return encoded_jwt

    @staticmethod
    def decode_token(request: Request) -> dict:
        jwt_token: str = ""
        for header,value in request.headers.items():
            if header != "authorization":
                continue
            if not value.startswith("Bearer "):
                continue
            value_split = value.split(" ")
            if len(value_split) != 2:
                continue
            jwt_token = value_split[1]

        if len(jwt_token) == 0:
            raise InvalidTokenError("Missing JWT token")

        constants = get_constants()
        payload = jwt.decode(
            jwt=jwt_token,
            key=constants["JWT_SECRET_KEY"],
            algorithms=[constants["JWT_ALGORITHM"]]
        )

        if ("user_id" not in payload) or (type(payload["user_id"]) != int):
            raise InvalidTokenError(
                "user_id field missing or corrupted in the JWT payload"
            )

        return payload

