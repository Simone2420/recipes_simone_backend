from dataclasses import dataclass


@dataclass
class Ingredient:
    id: int
    name: str
    recipe_id: int

