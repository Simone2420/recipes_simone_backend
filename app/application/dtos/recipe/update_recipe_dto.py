from pydantic import BaseModel
from typing import Optional


class UpdateRecipeDTO(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    dificulty_id: Optional[int] = None

