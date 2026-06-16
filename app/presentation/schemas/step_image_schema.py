from pydantic import BaseModel
from typing import Optional


class StepImageBase(BaseModel):
    image_url: str
    order: int


class StepImageCreate(StepImageBase):
    step_id: int


class StepImageUpdate(BaseModel):
    image_url: Optional[str] = None
    order: Optional[int] = None


class StepImageResponse(StepImageBase):
    id: int
    step_id: int

    class Config:
        from_attributes = True

