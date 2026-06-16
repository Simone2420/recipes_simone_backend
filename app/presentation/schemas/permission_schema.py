from pydantic import BaseModel
from typing import Optional


class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class PermissionResponse(PermissionBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class AssignPermissionRequest(BaseModel):
    role_id: int
    permission_id: int

