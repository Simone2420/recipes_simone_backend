from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.step import (
    CreateStepUseCase,
    GetStepUseCase,
    ListStepsByRecipeUseCase,
    UpdateStepUseCase,
    DeleteStepUseCase
)
from app.application.dtos.step import CreateStepDTO, UpdateStepDTO
from app.infrastructure.repositories.step_repository_impl import StepRepositoryImpl
from app.presentation.schemas.step_schema import (
    StepCreate,
    StepUpdate,
    StepResponse
)

router = APIRouter(prefix="/steps", tags=["steps"])


def get_step_repository(db: Session = Depends(get_db)) -> StepRepositoryImpl:
    return StepRepositoryImpl(db)


@router.post("/", response_model=StepResponse, status_code=status.HTTP_201_CREATED)
def create_step(
    step_data: StepCreate,
    step_repo: StepRepositoryImpl = Depends(get_step_repository)
):
    use_case = CreateStepUseCase(step_repo)
    dto = CreateStepDTO(
        content=step_data.content,
        description=step_data.description,
        order=step_data.order,
        recipe_id=step_data.recipe_id
    )
    step = use_case.execute(dto)
    return StepResponse.model_validate(step)


@router.get("/recipe/{recipe_id}", response_model=List[StepResponse])
def list_steps_by_recipe(
    recipe_id: int,
    step_repo: StepRepositoryImpl = Depends(get_step_repository)
):
    use_case = ListStepsByRecipeUseCase(step_repo)
    steps = use_case.execute(recipe_id)
    return [StepResponse.model_validate(s) for s in steps]


@router.get("/{step_id}", response_model=StepResponse)
def get_step(
    step_id: int,
    step_repo: StepRepositoryImpl = Depends(get_step_repository)
):
    use_case = GetStepUseCase(step_repo)
    step = use_case.execute(step_id)
    if not step:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Step not found")
    return StepResponse.model_validate(step)


@router.put("/{step_id}", response_model=StepResponse)
def update_step(
    step_id: int,
    step_data: StepUpdate,
    step_repo: StepRepositoryImpl = Depends(get_step_repository)
):
    try:
        use_case = UpdateStepUseCase(step_repo)
        dto = UpdateStepDTO(
            content=step_data.content,
            description=step_data.description,
            order=step_data.order
        )
        step = use_case.execute(step_id, dto)
        return StepResponse.model_validate(step)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{step_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_step(
    step_id: int,
    step_repo: StepRepositoryImpl = Depends(get_step_repository)
):
    try:
        use_case = DeleteStepUseCase(step_repo)
        use_case.execute(step_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

