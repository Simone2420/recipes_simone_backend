from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class IngredientsModel(Base):
    __tablename__ = "Ingredients"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), nullable=False)
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="ingredients")
    images = relationship("IngredientImageModel", back_populates="ingredient", cascade="all, delete-orphan")

