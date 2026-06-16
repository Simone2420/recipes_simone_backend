from pydantic import BaseModel
from typing import Optional


class IngredientImageBase(BaseModel):
    image_url: str


class IngredientImageCreate(IngredientImageBase):
    ingredient_id: int


class IngredientImageUpdate(BaseModel):
    image_url: Optional[str] = None


class IngredientImageResponse(IngredientImageBase):
    id: int
    ingredient_id: int

    class Config:
        from_attributes = True

