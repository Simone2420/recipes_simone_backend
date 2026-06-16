from pydantic import BaseModel


class CreateRecipeImageDTO(BaseModel):
    image_url: str
    recipe_id: int

