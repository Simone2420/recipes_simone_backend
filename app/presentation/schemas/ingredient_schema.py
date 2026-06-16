from pydantic import BaseModel
from typing import Optional


class IngredientBase(BaseModel):
    name: str


class IngredientCreate(IngredientBase):
    recipe_id: int


class IngredientUpdate(BaseModel):
    name: Optional[str] = None


class IngredientResponse(IngredientBase):
    id: int
    recipe_id: int

    class Config:
        from_attributes = True

