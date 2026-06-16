from pydantic import BaseModel
from typing import Optional


class UpdateIngredientImageDTO(BaseModel):
    image_url: Optional[str] = None

