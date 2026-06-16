from app.domain.repositories.comment_repository import CommentRepository


class DeleteCommentUseCase:
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def execute(self, comment_id: int) -> None:
        comment = self.comment_repository.get_by_id(comment_id)
        if not comment:
            raise ValueError("Comment not found")
        
        self.comment_repository.delete(comment_id)

