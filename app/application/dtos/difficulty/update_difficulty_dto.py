from pydantic import BaseModel
from typing import Optional


class UpdateDifficultyDTO(BaseModel):
    name: Optional[str] = None

