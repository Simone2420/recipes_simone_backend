from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.permission import Permission
from app.domain.repositories.permission_repository import PermissionRepository
from app.infrastructure.database.models.permission_model import PermisionModel
from app.infrastructure.mappers.permission_mapper import PermissionMapper


class PermissionRepositoryImpl(PermissionRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, permission_id: int) -> Optional[Permission]:
        model = self.db.query(PermisionModel).filter(PermisionModel.id == permission_id).first()
        if not model:
            return None
        return PermissionMapper.to_domain(model)
    
    def get_all(self) -> List[Permission]:
        models = self.db.query(PermisionModel).all()
        return [PermissionMapper.to_domain(model) for model in models]
    
    def save(self, permission: Permission) -> Permission:
        if permission.id:
            model = self.db.query(PermisionModel).filter(PermisionModel.id == permission.id).first()
            if model:
                model.permision_name = permission.name
                model.description = permission.description
                model.is_active = permission.is_active
            else:
                model = PermissionMapper.to_model(permission)
                self.db.add(model)
                self.db.flush()
        else:
            model = PermissionMapper.to_model(permission)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return PermissionMapper.to_domain(model)
    
    def delete(self, permission_id: int) -> None:
        model = self.db.query(PermisionModel).filter(PermisionModel.id == permission_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

