from pydantic import BaseModel


class CreateStepImageDTO(BaseModel):
    image_url: str
    order: int
    step_id: int

