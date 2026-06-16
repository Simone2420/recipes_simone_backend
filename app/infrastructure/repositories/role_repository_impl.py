from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.role import Role
from app.domain.repositories.role_repository import RoleRepository
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.mappers.role_mapper import RoleMapper


class RoleRepositoryImpl(RoleRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, role_id: int) -> Optional[Role]:
        model = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if not model:
            return None
        return RoleMapper.to_domain(model)
    
    def get_all(self) -> List[Role]:
        models = self.db.query(RoleModel).all()
        return [RoleMapper.to_domain(model) for model in models]
    
    def save(self, role: Role) -> Role:
        if role.id:
            model = self.db.query(RoleModel).filter(RoleModel.id == role.id).first()
            if model:
                model.name = role.name
                model.description = role.description
                model.is_active = role.is_active
            else:
                model = RoleMapper.to_model(role)
                self.db.add(model)
                self.db.flush()
        else:
            model = RoleMapper.to_model(role)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return RoleMapper.to_domain(model)
    
    def delete(self, role_id: int) -> None:
        model = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

