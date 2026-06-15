from dataclasses import dataclass
from datetime import datetime


@dataclass
class Comment:
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    recipe_id: int
    user_id: int

