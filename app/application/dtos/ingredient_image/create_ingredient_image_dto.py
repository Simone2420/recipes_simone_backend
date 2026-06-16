from pydantic import BaseModel


class CreateIngredientImageDTO(BaseModel):
    image_url: str
    ingredient_id: int

