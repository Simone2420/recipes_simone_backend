from pydantic import BaseModel


class CreateRecipeDTO(BaseModel):
    title: str
    description: str
    user_id: int
    dificulty_id: int

