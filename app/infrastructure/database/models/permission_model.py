from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class PermisionModel(Base):
    __tablename__ = "Permision"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    permision_name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Relationships
    roles = relationship("RoleModel", secondary="Permision_Role", back_populates="permissions")

