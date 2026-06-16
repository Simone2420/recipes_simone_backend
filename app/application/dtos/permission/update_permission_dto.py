from pydantic import BaseModel
from typing import Optional


class UpdatePermissionDTO(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

