from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Recipe:
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    status: bool
    user_id: int
    dificulty_id: int

