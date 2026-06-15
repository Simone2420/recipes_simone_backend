from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeImageModel(Base):
    __tablename__ = "Recipe_Image"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_url = Column(String(500), nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), nullable=False)
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="images")

