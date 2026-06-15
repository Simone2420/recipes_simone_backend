from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeModel(Base):
    __tablename__ = "Recipe"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    status = Column(Boolean, default=True, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    dificuly_id = Column(Integer, ForeignKey("Dificulty.id"), nullable=False)
    
    # Relationships
    user = relationship("UserModel", back_populates="recipes")
    difficulty = relationship("DificultyModel", back_populates="recipes")
    ingredients = relationship("IngredientsModel", back_populates="recipe", cascade="all, delete-orphan")
    steps = relationship("StepModel", back_populates="recipe", cascade="all, delete-orphan")
    images = relationship("RecipeImageModel", back_populates="recipe", cascade="all, delete-orphan")
    comments = relationship("CommentModel", back_populates="recipe", cascade="all, delete-orphan")
    ratings = relationship("RecipeRatingModel", back_populates="recipe", cascade="all, delete-orphan")
    info = relationship("RecipeInfoModel", back_populates="recipe", uselist=False, cascade="all, delete-orphan")

