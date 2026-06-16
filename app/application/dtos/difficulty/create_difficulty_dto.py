from pydantic import BaseModel


class CreateDifficultyDTO(BaseModel):
    name: str

