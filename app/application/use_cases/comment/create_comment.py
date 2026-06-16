from datetime import datetime
from app.domain.entities.comment import Comment
from app.domain.repositories.comment_repository import CommentRepository
from app.application.dtos.comment.create_comment_dto import CreateCommentDTO


class CreateCommentUseCase:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, dto: CreateCommentDTO) -> Comment:
        now = datetime.utcnow()
        comment = Comment(
            id=0,
            title=dto.title,
            content=dto.content,
            created_at=now,
            updated_at=now,
            recipe_id=dto.recipe_id,
            user_id=dto.user_id
        )
        return self.comment_repository.save(comment)

