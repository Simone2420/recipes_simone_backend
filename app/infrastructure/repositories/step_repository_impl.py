from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.step import Step
from app.domain.repositories.step_repository import StepRepository
from app.infrastructure.database.models.step_model import StepModel
from app.infrastructure.mappers.step_mapper import StepMapper


class StepRepositoryImpl(StepRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, step_id: int) -> Optional[Step]:
        model = self.db.query(StepModel).filter(StepModel.id == step_id).first()
        if not model:
            return None
        return StepMapper.to_domain(model)
    
    def get_by_recipe_id(self, recipe_id: int) -> List[Step]:
        models = self.db.query(StepModel).filter(StepModel.recipe_id == recipe_id).order_by(StepModel.order).all()
        return [StepMapper.to_domain(model) for model in models]
    
    def get_all(self) -> List[Step]:
        models = self.db.query(StepModel).all()
        return [StepMapper.to_domain(model) for model in models]
    
    def save(self, step: Step) -> Step:
        if step.id:
            model = self.db.query(StepModel).filter(StepModel.id == step.id).first()
            if model:
                model.content = step.content
                model.description = step.description
                model.order = step.order
                model.recipe_id = step.recipe_id
            else:
                model = StepMapper.to_model(step)
                self.db.add(model)
                self.db.flush()
        else:
            model = StepMapper.to_model(step)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return StepMapper.to_domain(model)
    
    def delete(self, step_id: int) -> None:
        model = self.db.query(StepModel).filter(StepModel.id == step_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

