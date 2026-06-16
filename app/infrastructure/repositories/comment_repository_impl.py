from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.comment import Comment
from app.domain.repositories.comment_repository import CommentRepository
from app.infrastructure.database.models.comment_model import CommentModel
from app.infrastructure.mappers.comment_mapper import CommentMapper


class CommentRepositoryImpl(CommentRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, comment_id: int) -> Optional[Comment]:
        model = self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()
        if not model:
            return None
        return CommentMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> List[Comment]:
        models = self.db.query(CommentModel).filter(CommentModel.recipe_id == recipe_id).order_by(CommentModel.created_at.desc()).all()
        return [CommentMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[Comment]:
        models = self.db.query(CommentModel).all()
        return [CommentMapper.to_domain(model) for model in models]
    
    def save(self, comment: Comment) -> Comment:
        if comment.id:
            model = self.db.query(CommentModel).filter(CommentModel.id == comment.id).first()
            if model:
                model.title = comment.title
                model.content = comment.content
                model.recipe_id = comment.recipe_id
                model.user_id = comment.user_id
            else:
                model = CommentMapper.to_model(comment)
                self.db.add(model)
                self.db.flush()
        else:
            model = CommentMapper.to_model(comment)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return CommentMapper.to_domain(model)
    
    def delete(self, comment_id: int) -> None:
        model = self.db.query(CommentModel).filter(CommentModel.id == comment_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

