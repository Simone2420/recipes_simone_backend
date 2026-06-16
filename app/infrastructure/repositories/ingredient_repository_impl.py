from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.ingredient import Ingredient
from app.domain.repositories.ingredient_repository import IngredientRepository
from app.infrastructure.database.models.ingredient_model import IngredientsModel
from app.infrastructure.mappers.ingredient_mapper import IngredientMapper


class IngredientRepositoryImpl(IngredientRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, ingredient_id: int) -> Optional[Ingredient]:
        model = self.db.query(IngredientsModel).filter(IngredientsModel.id == ingredient_id).first()
        if not model:
            return None
        return IngredientMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> List[Ingredient]:
        models = self.db.query(IngredientsModel).filter(IngredientsModel.recipe_id == recipe_id).all()
        return [IngredientMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[Ingredient]:
        models = self.db.query(IngredientsModel).all()
        return [IngredientMapper.to_domain(model) for model in models]
    
    def save(self, ingredient: Ingredient) -> Ingredient:
        if ingredient.id:
            model = self.db.query(IngredientsModel).filter(IngredientsModel.id == ingredient.id).first()
            if model:
                model.name = ingredient.name
                model.recipe_id = ingredient.recipe_id
            else:
                model = IngredientMapper.to_model(ingredient)
                self.db.add(model)
                self.db.flush()
        else:
            model = IngredientMapper.to_model(ingredient)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return IngredientMapper.to_domain(model)
    
    def delete(self, ingredient_id: int) -> None:
        model = self.db.query(IngredientsModel).filter(IngredientsModel.id == ingredient_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

