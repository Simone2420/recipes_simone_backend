from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CommentBase(BaseModel):
    title: str
    content: str


class CommentCreate(CommentBase):
    recipe_id: int
    user_id: int


class CommentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class CommentResponse(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    recipe_id: int
    user_id: int

    class Config:
        from_attributes = True

