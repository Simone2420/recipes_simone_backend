from app.domain.entities.permission import Permission
from app.infrastructure.database.models.permission_model import PermisionModel


class PermissionMapper:
    @staticmethod
    def to_domain(model: PermisionModel) -> Permission:
        return Permission(
            id=model.id,
            name=model.permision_name,
            description=model.description,
            is_active=model.is_active
        )
    
    @staticmethod
    def to_model(entity: Permission) -> PermisionModel:
        return PermisionModel(
            id=entity.id,
            permision_name=entity.name,
            description=entity.description,
            is_active=entity.is_active
        )

