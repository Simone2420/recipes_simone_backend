from dataclasses import dataclass


@dataclass
class StepImage:
    id: int
    image_url: str
    order: int
    step_id: int

