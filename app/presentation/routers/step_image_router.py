from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.step_image import (
    CreateStepImageUseCase,
    GetStepImageUseCase,
    ListStepImagesByStepUseCase,
    UpdateStepImageUseCase,
    DeleteStepImageUseCase
)
from app.application.dtos.step_image import CreateStepImageDTO, UpdateStepImageDTO
from app.infrastructure.repositories.step_image_repository_impl import StepImageRepositoryImpl
from app.presentation.schemas.step_image_schema import (
    StepImageCreate,
    StepImageUpdate,
    StepImageResponse
)

router = APIRouter(prefix="/step-images", tags=["step-images"])


def get_step_image_repository(db: Session = Depends(get_db)) -> StepImageRepositoryImpl:
    return StepImageRepositoryImpl(db)


@router.post("/", response_model=StepImageResponse, status_code=status.HTTP_201_CREATED)
def create_step_image(
    image_data: StepImageCreate,
    image_repo: StepImageRepositoryImpl = Depends(get_step_image_repository)
):
    use_case = CreateStepImageUseCase(image_repo)
    dto = CreateStepImageDTO(
        image_url=image_data.image_url,
        order=image_data.order,
        step_id=image_data.step_id
    )
    image = use_case.execute(dto)
    return StepImageResponse.model_validate(image)


@router.get("/step/{step_id}", response_model=List[StepImageResponse])
def list_step_images_by_step(
    step_id: int,
    image_repo: StepImageRepositoryImpl = Depends(get_step_image_repository)
):
    use_case = ListStepImagesByStepUseCase(image_repo)
    images = use_case.execute(step_id)
    return [StepImageResponse.model_validate(i) for i in images]


@router.get("/{image_id}", response_model=StepImageResponse)
def get_step_image(
    image_id: int,
    image_repo: StepImageRepositoryImpl = Depends(get_step_image_repository)
):
    use_case = GetStepImageUseCase(image_repo)
    image = use_case.execute(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Step image not found")
    return StepImageResponse.model_validate(image)


@router.put("/{image_id}", response_model=StepImageResponse)
def update_step_image(
    image_id: int,
    image_data: StepImageUpdate,
    image_repo: StepImageRepositoryImpl = Depends(get_step_image_repository)
):
    try:
        use_case = UpdateStepImageUseCase(image_repo)
        dto = UpdateStepImageDTO(
            image_url=image_data.image_url,
            order=image_data.order
        )
        image = use_case.execute(image_id, dto)
        return StepImageResponse.model_validate(image)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_step_image(
    image_id: int,
    image_repo: StepImageRepositoryImpl = Depends(get_step_image_repository)
):
    try:
        use_case = DeleteStepImageUseCase(image_repo)
        use_case.execute(image_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

