from typing import List
from app.domain.entities.comment import Comment
from app.domain.repositories.comment_repository import CommentRepository


class ListCommentsByRecipeUseCase:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, recipe_id: int) -> List[Comment]:
        return self.comment_repository.get_by_recipe_id(recipe_id)

