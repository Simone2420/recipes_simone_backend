from pydantic import BaseModel
from typing import Optional


class CreateStepDTO(BaseModel):
    content: str
    description: Optional[str] = None
    order: int
    recipe_id: int

