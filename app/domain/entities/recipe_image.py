from dataclasses import dataclass


@dataclass
class RecipeImage:
    id: int
    image_url: str
    recipe_id: int

