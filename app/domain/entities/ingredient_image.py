from dataclasses import dataclass


@dataclass
class IngredientImage:
    id: int
    image_url: str
    ingredient_id: int

