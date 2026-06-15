from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class UserRoleModel(Base):
    __tablename__ = "User_Role"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("Role.id"), nullable=False)

