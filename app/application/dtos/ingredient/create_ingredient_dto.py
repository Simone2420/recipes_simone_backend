from pydantic import BaseModel


class CreateIngredientDTO(BaseModel):
    name: str
    recipe_id: int

