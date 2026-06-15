from sqlalchemy import Column, Integer, String, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base


class RecipeRatingModel(Base):
    __tablename__ = "Recipe_Rating"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    content = Column(Text, nullable=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    
    __table_args__ = (
        CheckConstraint("value BETWEEN 1 AND 5", name="check_rating_value"),
    )
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="ratings")
    user = relationship("UserModel", back_populates="ratings")

