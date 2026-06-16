from app.domain.entities.step_image import StepImage
from app.infrastructure.database.models.step_image_model import StepImageModel


class StepImageMapper:
    @staticmethod
    def to_domain(model: StepImageModel) -> StepImage:
        return StepImage(
            id=model.id,
            image_url=model.image_url,
            order=model.order,
            step_id=model.step_id
        )
    
    @staticmethod
    def to_model(entity: StepImage) -> StepImageModel:
        return StepImageModel(
            id=entity.id,
            image_url=entity.image_url,
            order=entity.order,
            step_id=entity.step_id
        )

