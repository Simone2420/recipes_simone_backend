from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.step_image import StepImage
from app.domain.repositories.step_image_repository import StepImageRepository
from app.infrastructure.database.models.step_image_model import StepImageModel
from app.infrastructure.mappers.step_image_mapper import StepImageMapper


class StepImageRepositoryImpl(StepImageRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, image_id: int) -> Optional[StepImage]:
        model = self.db.query(StepImageModel).filter(StepImageModel.id == image_id).first()
        if not model:
            return None
        return StepImageMapper.to_domain(model)
    
    def get_by_step_id(self, step_id: int) -> List[StepImage]:
        models = self.db.query(StepImageModel).filter(StepImageModel.step_id == step_id).order_by(StepImageModel.order).all()
        return [StepImageMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[StepImage]:
        models = self.db.query(StepImageModel).all()
        return [StepImageMapper.to_domain(model) for model in models]
    
    def save(self, image: StepImage) -> StepImage:
        if image.id:
            model = self.db.query(StepImageModel).filter(StepImageModel.id == image.id).first()
            if model:
                model.image_url = image.image_url
                model.order = image.order
                model.step_id = image.step_id
            else:
                model = StepImageMapper.to_model(image)
                self.db.add(model)
                self.db.flush()
        else:
            model = StepImageMapper.to_model(image)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return StepImageMapper.to_domain(model)
    
    def delete(self, image_id: int) -> None:
        model = self.db.query(StepImageModel).filter(StepImageModel.id == image_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

