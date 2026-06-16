from pydantic import BaseModel
from typing import Optional


class CreateRoleDTO(BaseModel):
    name: str
    description: Optional[str] = None

