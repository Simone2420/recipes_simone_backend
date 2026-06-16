from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.difficulty import (
    CreateDifficultyUseCase,
    GetDifficultyUseCase,
    ListDifficultiesUseCase,
    UpdateDifficultyUseCase,
    DeleteDifficultyUseCase
)
from app.application.dtos.difficulty import CreateDifficultyDTO, UpdateDifficultyDTO
from app.infrastructure.repositories.difficulty_repository_impl import DifficultyRepositoryImpl
from app.presentation.schemas.difficulty_schema import (
    DifficultyCreate,
    DifficultyUpdate,
    DifficultyResponse
)

router = APIRouter(prefix="/difficulties", tags=["difficulties"])


def get_difficulty_repository(db: Session = Depends(get_db)) -> DifficultyRepositoryImpl:
    return DifficultyRepositoryImpl(db)


@router.post("/", response_model=DifficultyResponse, status_code=status.HTTP_201_CREATED)
def create_difficulty(
    difficulty_data: DifficultyCreate,
    difficulty_repo: DifficultyRepositoryImpl = Depends(get_difficulty_repository)
):
    use_case = CreateDifficultyUseCase(difficulty_repo)
    dto = CreateDifficultyDTO(name=difficulty_data.name)
    difficulty = use_case.execute(dto)
    return DifficultyResponse.model_validate(difficulty)


@router.get("/", response_model=List[DifficultyResponse])
def list_difficulties(
    difficulty_repo: DifficultyRepositoryImpl = Depends(get_difficulty_repository)
):
    use_case = ListDifficultiesUseCase(difficulty_repo)
    difficulties = use_case.execute()
    return [DifficultyResponse.model_validate(d) for d in difficulties]


@router.get("/{difficulty_id}", response_model=DifficultyResponse)
def get_difficulty(
    difficulty_id: int,
    difficulty_repo: DifficultyRepositoryImpl = Depends(get_difficulty_repository)
):
    use_case = GetDifficultyUseCase(difficulty_repo)
    difficulty = use_case.execute(difficulty_id)
    if not difficulty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Difficulty not found")
    return DifficultyResponse.model_validate(difficulty)


@router.put("/{difficulty_id}", response_model=DifficultyResponse)
def update_difficulty(
    difficulty_id: int,
    difficulty_data: DifficultyUpdate,
    difficulty_repo: DifficultyRepositoryImpl = Depends(get_difficulty_repository)
):
    try:
        use_case = UpdateDifficultyUseCase(difficulty_repo)
        dto = UpdateDifficultyDTO(name=difficulty_data.name)
        difficulty = use_case.execute(difficulty_id, dto)
        return DifficultyResponse.model_validate(difficulty)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{difficulty_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_difficulty(
    difficulty_id: int,
    difficulty_repo: DifficultyRepositoryImpl = Depends(get_difficulty_repository)
):
    try:
        use_case = DeleteDifficultyUseCase(difficulty_repo)
        use_case.execute(difficulty_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

