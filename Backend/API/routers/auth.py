from fastapi import APIRouter, Request, Response, HTTPException
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel

from ..dao.users import Users
from ..dto.user import User
from ..utils.jwt import JWT

class LoginData(BaseModel):
    email: str
    password: str

class RegisterData(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    mock: bool | None = False
    role: str | None = "basic"

router = APIRouter()

@router.post("/login", status_code=204)
async def login(data: LoginData, response: Response):
    user: User = Users.verify_password(data.email, data.password)
    access_token = JWT.create_token(
        data={"user_id": user.id}
    )
    response.headers["authorization"] = f"Bearer {access_token}"

@router.post("/register", status_code=204)
async def register(data: RegisterData, request: Request):
    user: User = authenticate(request, "admin", False)
    if not user:
        Users.create(
            data.name, data.surname, data.email, data.password, data.mock
        )
    else:
        Users.create(
            data.name, data.surname, data.email, data.password, data.mock, data.role
        )

def authenticate(request: Request, role: str = "basic", fail_mode: bool = True) -> User|None:
    try:
        user_data = JWT.decode_token(request)
        user = Users.find_by_id(user_data["user_id"])
        if user is None:
            if not fail_mode: return None
            raise HTTPException(
                status_code=401,
                detail=f"Could not find the user associated with the provided token",
            )
        if user.role != "admin":
            if user.role != role:
                if not fail_mode: return None
                raise HTTPException(
                    status_code=401,
                    detail=f"You don't have permission to do this operation",
                )
        return user
    except InvalidTokenError as e:
        if not fail_mode: return None
        raise HTTPException(
            status_code=401,
            detail=f"JWT Token error: {str(e)}"
        )