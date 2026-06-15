from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class StepModel(Base):
    __tablename__ = "Step"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), nullable=False)
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="steps")
    images = relationship("StepImageModel", back_populates="step", cascade="all, delete-orphan")

