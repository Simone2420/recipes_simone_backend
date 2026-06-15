from dataclasses import dataclass
from typing import Optional


@dataclass
class RecipeInfo:
    id: int
    cook_time: Optional[int]
    preparation_time: Optional[int]
    calories: Optional[int]
    quote: Optional[str]
    recipe_id: int

