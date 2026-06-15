from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class DificultyModel(Base):
    __tablename__ = "Dificulty"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    
    # Relationships
    recipes = relationship("RecipeModel", back_populates="difficulty")

