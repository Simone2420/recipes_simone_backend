from datetime import datetime
from app.domain.entities.comment import Comment
from app.domain.repositories.comment_repository import CommentRepository
from app.application.dtos.comment.update_comment_dto import UpdateCommentDTO


class UpdateCommentUseCase:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: int, dto: UpdateCommentDTO) -> Comment:
        comment = self.comment_repository.get_by_id(comment_id)
        if not comment:
            raise ValueError("Comment not found")
        
        if dto.title is not None:
            comment.title = dto.title
        if dto.content is not None:
            comment.content = dto.content
        
        comment.updated_at = datetime.utcnow()
        
        return self.comment_repository.save(comment)

