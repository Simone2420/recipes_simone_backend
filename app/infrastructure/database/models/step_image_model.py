from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class StepImageModel(Base):
    __tablename__ = "Step_Image"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_url = Column(String(500), nullable=False)
    order = Column(Integer, nullable=False)
    step_id = Column(Integer, ForeignKey("Step.id"), nullable=False)
    
    # Relationships
    step = relationship("StepModel", back_populates="images")

