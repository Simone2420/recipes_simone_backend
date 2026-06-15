from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class CommentModel(Base):
    __tablename__ = "Comment"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    recipe_id = Column(Integer, ForeignKey("Recipe.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    
    # Relationships
    recipe = relationship("RecipeModel", back_populates="comments")
    user = relationship("UserModel", back_populates="comments")

