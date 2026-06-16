from pydantic import BaseModel


class CreateCommentDTO(BaseModel):
    title: str
    content: str
    recipe_id: int
    user_id: int

