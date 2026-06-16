from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.core.dependencies import get_db
from app.application.use_cases.recipe_info import (
    CreateRecipeInfoUseCase,
    GetRecipeInfoUseCase,
    GetRecipeInfoByRecipeUseCase,
    UpdateRecipeInfoUseCase,
    DeleteRecipeInfoUseCase
)
from app.application.dtos.recipe_info import CreateRecipeInfoDTO, UpdateRecipeInfoDTO
from app.infrastructure.repositories.recipe_info_repository_impl import RecipeInfoRepositoryImpl
from app.presentation.schemas.recipe_info_schema import (
    RecipeInfoCreate,
    RecipeInfoUpdate,
    RecipeInfoResponse
)

router = APIRouter(prefix="/recipe-info", tags=["recipe-info"])


def get_recipe_info_repository(db: Session = Depends(get_db)) -> RecipeInfoRepositoryImpl:
    return RecipeInfoRepositoryImpl(db)


@router.post("/", response_model=RecipeInfoResponse, status_code=status.HTTP_201_CREATED)
def create_recipe_info(
    info_data: RecipeInfoCreate,
    info_repo: RecipeInfoRepositoryImpl = Depends(get_recipe_info_repository)
):
    use_case = CreateRecipeInfoUseCase(info_repo)
    dto = CreateRecipeInfoDTO(
        cook_time=info_data.cook_time,
        preparation_time=info_data.preparation_time,
        calories=info_data.calories,
        quote=info_data.quote,
        recipe_id=info_data.recipe_id
    )
    info = use_case.execute(dto)
    return RecipeInfoResponse.model_validate(info)


@router.get("/recipe/{recipe_id}", response_model=Optional[RecipeInfoResponse])
def get_recipe_info_by_recipe(
    recipe_id: int,
    info_repo: RecipeInfoRepositoryImpl = Depends(get_recipe_info_repository)
):
    use_case = GetRecipeInfoByRecipeUseCase(info_repo)
    info = use_case.execute(recipe_id)
    if not info:
        return None
    return RecipeInfoResponse.model_validate(info)


@router.get("/{info_id}", response_model=RecipeInfoResponse)
def get_recipe_info(
    info_id: int,
    info_repo: RecipeInfoRepositoryImpl = Depends(get_recipe_info_repository)
):
    use_case = GetRecipeInfoUseCase(info_repo)
    info = use_case.execute(info_id)
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe info not found")
    return RecipeInfoResponse.model_validate(info)


@router.put("/{info_id}", response_model=RecipeInfoResponse)
def update_recipe_info(
    info_id: int,
    info_data: RecipeInfoUpdate,
    info_repo: RecipeInfoRepositoryImpl = Depends(get_recipe_info_repository)
):
    try:
        use_case = UpdateRecipeInfoUseCase(info_repo)
        dto = UpdateRecipeInfoDTO(
            cook_time=info_data.cook_time,
            preparation_time=info_data.preparation_time,
            calories=info_data.calories,
            quote=info_data.quote
        )
        info = use_case.execute(info_id, dto)
        return RecipeInfoResponse.model_validate(info)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{info_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe_info(
    info_id: int,
    info_repo: RecipeInfoRepositoryImpl = Depends(get_recipe_info_repository)
):
    try:
        use_case = DeleteRecipeInfoUseCase(info_repo)
        use_case.execute(info_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

