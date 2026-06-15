from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeInfoModel(Base):
    __tablename__ = "Recipe_Info"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cook_time = Column(Integer, nullable=True)  # in minutes
    preparation_time = Column(Integer, nullable=True)  # in minutes
    calories = Column(Integer, nullable=True)
    quote = Column(Text, nullable=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), unique=True, nullable=False)
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="info")

