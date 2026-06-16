from sqlalchemy.orm import Session
from app.infrastructure.database.models.permission_model import PermisionModel
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.role_permission_model import PermisionRoleModel


class AssignPermissionUseCase:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, role_id: int, permission_id: int) -> None:
        role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if not role:
            raise ValueError("Role not found")
        
        permission = self.db.query(PermisionModel).filter(PermisionModel.id == permission_id).first()
        if not permission:
            raise ValueError("Permission not found")
        
        # Check if already assigned
        existing = self.db.query(PermisionRoleModel).filter(
            PermisionRoleModel.role_id == role_id,
            PermisionRoleModel.permision_id == permission_id
        ).first()
        
        if existing:
            return  # Already assigned
        
        role_permission = PermisionRoleModel(role_id=role_id, permision_id=permission_id)
        self.db.add(role_permission)
        self.db.commit()

