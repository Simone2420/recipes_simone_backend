from pydantic import BaseModel
from typing import Optional


class StepBase(BaseModel):
    content: str
    description: Optional[str] = None
    order: int


class StepCreate(StepBase):
    recipe_id: int


class StepUpdate(BaseModel):
    content: Optional[str] = None
    description: Optional[str] = None
    order: Optional[int] = None


class StepResponse(StepBase):
    id: int
    recipe_id: int

    class Config:
        from_attributes = True

