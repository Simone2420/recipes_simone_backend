from pydantic import BaseModel, Field
from typing import Optional


class CreateRecipeRatingDTO(BaseModel):
    value: int = Field(..., ge=1, le=5)
    content: Optional[str] = None
    recipe_id: int
    user_id: int

