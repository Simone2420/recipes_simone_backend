from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class IngredientImageModel(Base):
    __tablename__ = "Ingredient_Image"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_url = Column(String(500), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("Ingredients.id"), nullable=False)
    
    # Relationships
    ingredient = relationship("IngredientsModel", back_populates="images")

