from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserDTO(BaseModel):
    id: int
    username: str
    email: str | None = None
    role: int | None = None


class UserInDB(UserDTO):
    hashed_password: str
