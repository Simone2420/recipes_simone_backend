from pydantic import BaseModel
from typing import Optional


class CreatePermissionDTO(BaseModel):
    name: str
    description: Optional[str] = None

