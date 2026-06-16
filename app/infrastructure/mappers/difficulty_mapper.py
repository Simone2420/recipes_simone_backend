from app.domain.entities.difficulty import Difficulty
from app.infrastructure.database.models.difficulty_model import DificultyModel


class DifficultyMapper:
    @staticmethod
    def to_domain(model: DificultyModel) -> Difficulty:
        return Difficulty(
            id=model.id,
            name=model.name
        )
    
    @staticmethod
    def to_model(entity: Difficulty) -> DificultyModel:
        return DificultyModel(
            id=entity.id,
            name=entity.name
        )

