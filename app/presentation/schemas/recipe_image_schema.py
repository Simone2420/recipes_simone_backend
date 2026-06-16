from pydantic import BaseModel
from typing import Optional


class RecipeImageBase(BaseModel):
    image_url: str


class RecipeImageCreate(RecipeImageBase):
    recipe_id: int


class RecipeImageUpdate(BaseModel):
    image_url: Optional[str] = None


class RecipeImageResponse(RecipeImageBase):
    id: int
    recipe_id: int

    class Config:
        from_attributes = True

