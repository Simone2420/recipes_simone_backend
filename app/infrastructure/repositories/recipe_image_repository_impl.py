from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.recipe_image import RecipeImage
from app.domain.repositories.recipe_image_repository import RecipeImageRepository
from app.infrastructure.database.models.recipe_image_model import RecipeImageModel
from app.infrastructure.mappers.recipe_image_mapper import RecipeImageMapper


class RecipeImageRepositoryImpl(RecipeImageRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, image_id: int) -> Optional[RecipeImage]:
        model = self.db.query(RecipeImageModel).filter(RecipeImageModel.id == image_id).first()
        if not model:
            return None
        return RecipeImageMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> List[RecipeImage]:
        models = self.db.query(RecipeImageModel).filter(RecipeImageModel.recipe_id == recipe_id).all()
        return [RecipeImageMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[RecipeImage]:
        models = self.db.query(RecipeImageModel).all()
        return [RecipeImageMapper.to_domain(model) for model in models]
    
    def save(self, image: RecipeImage) -> RecipeImage:
        if image.id:
            model = self.db.query(RecipeImageModel).filter(RecipeImageModel.id == image.id).first()
            if model:
                model.image_url = image.image_url
                model.recipe_id = image.recipe_id
            else:
                model = RecipeImageMapper.to_model(image)
                self.db.add(model)
                self.db.flush()
        else:
            model = RecipeImageMapper.to_model(image)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return RecipeImageMapper.to_domain(model)
    
    def delete(self, image_id: int) -> None:
        model = self.db.query(RecipeImageModel).filter(RecipeImageModel.id == image_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

