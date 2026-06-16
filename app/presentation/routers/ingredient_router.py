from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.ingredient import (
    CreateIngredientUseCase,
    GetIngredientUseCase,
    ListIngredientsByRecipeUseCase,
    UpdateIngredientUseCase,
    DeleteIngredientUseCase
)
from app.application.dtos.ingredient import CreateIngredientDTO, UpdateIngredientDTO
from app.infrastructure.repositories.ingredient_repository_impl import IngredientRepositoryImpl
from app.presentation.schemas.ingredient_schema import (
    IngredientCreate,
    IngredientUpdate,
    IngredientResponse
)

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


def get_ingredient_repository(db: Session = Depends(get_db)) -> IngredientRepositoryImpl:
    return IngredientRepositoryImpl(db)


@router.post("/", response_model=IngredientResponse, status_code=status.HTTP_201_CREATED)
def create_ingredient(
    ingredient_data: IngredientCreate,
    ingredient_repo: IngredientRepositoryImpl = Depends(get_ingredient_repository)
):
    use_case = CreateIngredientUseCase(ingredient_repo)
    dto = CreateIngredientDTO(name=ingredient_data.name, recipe_id=ingredient_data.recipe_id)
    ingredient = use_case.execute(dto)
    return IngredientResponse.model_validate(ingredient)


@router.get("/recipe/{recipe_id}", response_model=List[IngredientResponse])
def list_ingredients_by_recipe(
    recipe_id: int,
    ingredient_repo: IngredientRepositoryImpl = Depends(get_ingredient_repository)
):
    use_case = ListIngredientsByRecipeUseCase(ingredient_repo)
    ingredients = use_case.execute(recipe_id)
    return [IngredientResponse.model_validate(i) for i in ingredients]


@router.get("/{ingredient_id}", response_model=IngredientResponse)
def get_ingredient(
    ingredient_id: int,
    ingredient_repo: IngredientRepositoryImpl = Depends(get_ingredient_repository)
):
    use_case = GetIngredientUseCase(ingredient_repo)
    ingredient = use_case.execute(ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient not found")
    return IngredientResponse.model_validate(ingredient)


@router.put("/{ingredient_id}", response_model=IngredientResponse)
def update_ingredient(
    ingredient_id: int,
    ingredient_data: IngredientUpdate,
    ingredient_repo: IngredientRepositoryImpl = Depends(get_ingredient_repository)
):
    try:
        use_case = UpdateIngredientUseCase(ingredient_repo)
        dto = UpdateIngredientDTO(name=ingredient_data.name)
        ingredient = use_case.execute(ingredient_id, dto)
        return IngredientResponse.model_validate(ingredient)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient(
    ingredient_id: int,
    ingredient_repo: IngredientRepositoryImpl = Depends(get_ingredient_repository)
):
    try:
        use_case = DeleteIngredientUseCase(ingredient_repo)
        use_case.execute(ingredient_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

