from app.domain.entities.comment import Comment
from app.infrastructure.database.models.comment_model import CommentModel


class CommentMapper:
    @staticmethod
    def to_domain(model: CommentModel) -> Comment:
        return Comment(
            id=model.id,
            title=model.title,
            content=model.content,
            created_at=model.created_at,
            updated_at=model.updated_at,
            recipe_id=model.recipe_id,
            user_id=model.user_id
        )
    
    @staticmethod
    def to_model(entity: Comment) -> CommentModel:
        return CommentModel(
            id=entity.id,
            title=entity.title,
            content=entity.content,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            recipe_id=entity.recipe_id,
            user_id=entity.user_id
        )

