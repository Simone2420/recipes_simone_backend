from pydantic import BaseModel, Field
from typing import Optional


class RecipeRatingBase(BaseModel):
    value: int = Field(..., ge=1, le=5)
    content: Optional[str] = None


class RecipeRatingCreate(RecipeRatingBase):
    recipe_id: int
    user_id: int


class RecipeRatingUpdate(BaseModel):
    value: Optional[int] = Field(None, ge=1, le=5)
    content: Optional[str] = None


class RecipeRatingResponse(RecipeRatingBase):
    id: int
    recipe_id: int
    user_id: int

    class Config:
        from_attributes = True

