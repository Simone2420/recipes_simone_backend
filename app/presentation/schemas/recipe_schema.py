from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RecipeBase(BaseModel):
    title: str
    description: str


class RecipeCreate(RecipeBase):
    user_id: int
    dificulty_id: int


class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    dificulty_id: Optional[int] = None


class RecipeResponse(RecipeBase):
    id: int
    created_at: datetime
    updated_at: datetime
    status: bool
    user_id: int
    dificulty_id: int

    class Config:
        from_attributes = True

