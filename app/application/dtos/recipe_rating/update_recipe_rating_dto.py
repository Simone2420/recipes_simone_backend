from pydantic import BaseModel, Field
from typing import Optional


class UpdateRecipeRatingDTO(BaseModel):
    value: Optional[int] = Field(None, ge=1, le=5)
    content: Optional[str] = None

