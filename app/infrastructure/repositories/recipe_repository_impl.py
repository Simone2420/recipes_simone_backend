from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.recipe import Recipe
from app.domain.repositories.recipe_repository import RecipeRepository
from app.infrastructure.database.models.recipe_model import RecipeModel
from app.infrastructure.mappers.recipe_mapper import RecipeMapper


class RecipeRepositoryImpl(RecipeRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        model = self.db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
        if not model:
            return None
        return RecipeMapper.to_domain(model)
    
    def get_all(self) -> List[Recipe]:
        models = self.db.query(RecipeModel).all()
        return [RecipeMapper.to_domain(model) for model in models]
    
    def get_by_user_id(self, user_id: int) -> List[Recipe]:
        models = self.db.query(RecipeModel).filter(RecipeModel.user_id == user_id).all()
        return [RecipeMapper.to_domain(model) for model in models]
    
    def save(self, recipe: Recipe) -> Recipe:
        if recipe.id:
            model = self.db.query(RecipeModel).filter(RecipeModel.id == recipe.id).first()
            if model:
                model.title = recipe.title
                model.description = recipe.description
                model.status = recipe.status
                model.user_id = recipe.user_id
                model.dificulty_id = recipe.dificulty_id
            else:
                model = RecipeMapper.to_model(recipe)
                self.db.add(model)
                self.db.flush()
        else:
            model = RecipeMapper.to_model(recipe)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return RecipeMapper.to_domain(model)
    
    def delete(self, recipe_id: int) -> None:
        model = self.db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

