from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class RoleModel(Base):
    __tablename__ = "Role"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Relationships
    users = relationship("UserModel", secondary="User_Role", back_populates="roles")
    permissions = relationship("PermisionModel", secondary="Permision_Role", back_populates="roles")

