from dataclasses import dataclass
from typing import Optional


@dataclass
class RecipeRating:
    id: int
    value: int
    content: Optional[str]
    recipe_id: int
    user_id: int

