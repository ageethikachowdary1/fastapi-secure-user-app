from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    # ✅ New Pydantic v2 way (fixes warning)
    model_config = ConfigDict(from_attributes=True)
