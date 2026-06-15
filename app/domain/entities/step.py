from dataclasses import dataclass
from typing import Optional


@dataclass
class Step:
    id: int
    content: str
    description: Optional[str]
    order: int
    recipe_id: int

