from pydantic import BaseModel
from typing import Optional


class CreateRecipeInfoDTO(BaseModel):
    cook_time: Optional[int] = None
    preparation_time: Optional[int] = None
    calories: Optional[int] = None
    quote: Optional[str] = None
    recipe_id: int

