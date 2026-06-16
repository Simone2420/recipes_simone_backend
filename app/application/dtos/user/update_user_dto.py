from pydantic import BaseModel, EmailStr
from typing import Optional


class UpdateUserDTO(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    status: Optional[bool] = None

