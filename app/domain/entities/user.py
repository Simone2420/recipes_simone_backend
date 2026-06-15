from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    status: bool = True

