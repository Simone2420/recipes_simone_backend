from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.ingredient_image import IngredientImage
from app.domain.repositories.ingredient_image_repository import IngredientImageRepository
from app.infrastructure.database.models.ingredient_image_model import IngredientImageModel
from app.infrastructure.mappers.ingredient_image_mapper import IngredientImageMapper


class IngredientImageRepositoryImpl(IngredientImageRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, image_id: int) -> Optional[IngredientImage]:
        model = self.db.query(IngredientImageModel).filter(IngredientImageModel.id == image_id).first()
        if not model:
            return None
        return IngredientImageMapper.to_domain(model)
    
    def get_by_ingredient_id(self, ingredient_id: int) -> List[IngredientImage]:
        models = self.db.query(IngredientImageModel).filter(IngredientImageModel.ingredient_id == ingredient_id).all()
        return [IngredientImageMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[IngredientImage]:
        models = self.db.query(IngredientImageModel).all()
        return [IngredientImageMapper.to_domain(model) for model in models]
    
    def save(self, image: IngredientImage) -> IngredientImage:
        if image.id:
            model = self.db.query(IngredientImageModel).filter(IngredientImageModel.id == image.id).first()
            if model:
                model.image_url = image.image_url
                model.ingredient_id = image.ingredient_id
            else:
                model = IngredientImageMapper.to_model(image)
                self.db.add(model)
                self.db.flush()
        else:
            model = IngredientImageMapper.to_model(image)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return IngredientImageMapper.to_domain(model)
    
    def delete(self, image_id: int) -> None:
        model = self.db.query(IngredientImageModel).filter(IngredientImageModel.id == image_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

