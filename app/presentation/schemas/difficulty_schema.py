from pydantic import BaseModel
from typing import Optional


class DifficultyBase(BaseModel):
    name: str


class DifficultyCreate(DifficultyBase):
    pass


class DifficultyUpdate(BaseModel):
    name: Optional[str] = None


class DifficultyResponse(DifficultyBase):
    id: int

    class Config:
        from_attributes = True

