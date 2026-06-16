from pydantic import BaseModel
from typing import Optional


class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class RoleResponse(RoleBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class AssignRoleRequest(BaseModel):
    user_id: int
    role_id: int

