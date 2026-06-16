from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.recipe_rating import RecipeRating
from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository
from app.infrastructure.database.models.recipe_rating_model import RecipeRatingModel
from app.infrastructure.mappers.recipe_rating_mapper import RecipeRatingMapper


class RecipeRatingRepositoryImpl(RecipeRatingRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, rating_id: int) -> Optional[RecipeRating]:
        model = self.db.query(RecipeRatingModel).filter(RecipeRatingModel.id == rating_id).first()
        if not model:
            return None
        return RecipeRatingMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> List[RecipeRating]:
        models = self.db.query(RecipeRatingModel).filter(RecipeRatingModel.recipe_id == recipe_id).all()
        return [RecipeRatingMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[RecipeRating]:
        models = self.db.query(RecipeRatingModel).all()
        return [RecipeRatingMapper.to_domain(model) for model in models]
    
    def save(self, rating: RecipeRating) -> RecipeRating:
        if rating.id:
            model = self.db.query(RecipeRatingModel).filter(RecipeRatingModel.id == rating.id).first()
            if model:
                model.value = rating.value
                model.content = rating.content
                model.recipe_id = rating.recipe_id
                model.user_id = rating.user_id
            else:
                model = RecipeRatingMapper.to_model(rating)
                self.db.add(model)
                self.db.flush()
        else:
            model = RecipeRatingMapper.to_model(rating)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return RecipeRatingMapper.to_domain(model)
    
    def delete(self, rating_id: int) -> None:
        model = self.db.query(RecipeRatingModel).filter(RecipeRatingModel.id == rating_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

