from typing import Optional
from app.domain.entities.comment import Comment
from app.domain.repositories.comment_repository import CommentRepository


class GetCommentUseCase:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: int) -> Optional[Comment]:
        return self.comment_repository.get_by_id(comment_id)

