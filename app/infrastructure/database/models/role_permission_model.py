from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class PermisionRoleModel(Base):
    __tablename__ = "Permision_Role"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    permision_id = Column(Integer, ForeignKey("Permision.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("Role.id"), nullable=False)

