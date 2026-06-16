from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entities.recipe_info import RecipeInfo
from app.domain.repositories.recipe_info_repository import RecipeInfoRepository
from app.infrastructure.database.models.recipe_info_model import RecipeInfoModel
from app.infrastructure.mappers.recipe_info_mapper import RecipeInfoMapper


class RecipeInfoRepositoryImpl(RecipeInfoRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, info_id: int) -> Optional[RecipeInfo]:
        model = self.db.query(RecipeInfoModel).filter(RecipeInfoModel.id == info_id).first()
        if not model:
            return None
        return RecipeInfoMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> Optional[RecipeInfo]:
        model = self.db.query(RecipeInfoModel).filter(RecipeInfoModel.recipe_id == recipe_id).first()
        if not model:
            return None
        return RecipeInfoMapper.to_domain(model)
    
    def save(self, info: RecipeInfo) -> RecipeInfo:
        if info.id:
            model = self.db.query(RecipeInfoModel).filter(RecipeInfoModel.id == info.id).first()
            if model:
                model.cook_time = info.cook_time
                model.preparation_time = info.preparation_time
                model.calories = info.calories
                model.quote = info.quote
                model.recipe_id = info.recipe_id
            else:
                model = RecipeInfoMapper.to_model(info)
                self.db.add(model)
                self.db.flush()
        else:
            model = RecipeInfoMapper.to_model(info)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return RecipeInfoMapper.to_domain(model)
    
    def delete(self, info_id: int) -> None:
        model = self.db.query(RecipeInfoModel).filter(RecipeInfoModel.id == info_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

