from pydantic import BaseModel
from typing import Optional


class UpdateIngredientDTO(BaseModel):
    name: Optional[str] = None

