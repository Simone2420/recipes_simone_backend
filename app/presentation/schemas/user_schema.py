from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    status: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    status: bool

    class Config:
        from_attributes = True

