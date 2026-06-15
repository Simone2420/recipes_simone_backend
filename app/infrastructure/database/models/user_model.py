from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class UserModel(Base):
    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    status = Column(Boolean, default=True, nullable=False)
    
    # Relationships
    recipes = relationship("RecipeModel", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("CommentModel", back_populates="user", cascade="all, delete-orphan")
    ratings = relationship("RecipeRatingModel", back_populates="user", cascade="all, delete-orphan")
    roles = relationship("RoleModel", secondary="User_Role", back_populates="users")

