from pydantic import BaseModel
from typing import Optional


class UpdateStepDTO(BaseModel):
    content: Optional[str] = None
    description: Optional[str] = None
    order: Optional[int] = None

