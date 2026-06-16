from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.difficulty import Difficulty
from app.domain.repositories.difficulty_repository import DifficultyRepository
from app.infrastructure.database.models.difficulty_model import DificultyModel
from app.infrastructure.mappers.difficulty_mapper import DifficultyMapper


class DifficultyRepositoryImpl(DifficultyRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, difficulty_id: int) -> Optional[Difficulty]:
        model = self.db.query(DificultyModel).filter(DificultyModel.id == difficulty_id).first()
        if not model:
            return None
        return DifficultyMapper.to_domain(model)
    
    def get_all(self) -> List[Difficulty]:
        models = self.db.query(DificultyModel).all()
        return [DifficultyMapper.to_domain(model) for model in models]
    
    def save(self, difficulty: Difficulty) -> Difficulty:
        if difficulty.id:
            model = self.db.query(DificultyModel).filter(DificultyModel.id == difficulty.id).first()
            if model:
                model.name = difficulty.name
            else:
                model = DifficultyMapper.to_model(difficulty)
                self.db.add(model)
                self.db.flush()
        else:
            model = DifficultyMapper.to_model(difficulty)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return DifficultyMapper.to_domain(model)
    
    def delete(self, difficulty_id: int) -> None:
        model = self.db.query(DificultyModel).filter(DificultyModel.id == difficulty_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

