from pydantic import BaseModel
from typing import Optional


class UpdateStepImageDTO(BaseModel):
    image_url: Optional[str] = None
    order: Optional[int] = None

