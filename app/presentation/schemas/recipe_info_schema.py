from pydantic import BaseModel
from typing import Optional


class RecipeInfoBase(BaseModel):
    cook_time: Optional[int] = None
    preparation_time: Optional[int] = None
    calories: Optional[int] = None
    quote: Optional[str] = None


class RecipeInfoCreate(RecipeInfoBase):
    recipe_id: int


class RecipeInfoUpdate(BaseModel):
    cook_time: Optional[int] = None
    preparation_time: Optional[int] = None
    calories: Optional[int] = None
    quote: Optional[str] = None


class RecipeInfoResponse(RecipeInfoBase):
    id: int
    recipe_id: int

    class Config:
        from_attributes = True

