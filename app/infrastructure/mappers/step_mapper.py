from app.domain.entities.step import Step
from app.infrastructure.database.models.step_model import StepModel


class StepMapper:
    @staticmethod
    def to_domain(model: StepModel) -> Step:
        return Step(
            id=model.id,
            content=model.content,
            description=model.description,
            order=model.order,
            recipe_id=model.recipe_id
        )
    
    @staticmethod
    def to_model(entity: Step) -> StepModel:
        return StepModel(
            id=entity.id,
            content=entity.content,
            description=entity.description,
            order=entity.order,
            recipe_id=entity.recipe_id
        )

