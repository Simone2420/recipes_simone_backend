from pydantic import BaseModel
from typing import Optional


class UpdateRecipeImageDTO(BaseModel):
    image_url: Optional[str] = None

