from pydantic import BaseModel
from typing import Optional


class UpdateCommentDTO(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

