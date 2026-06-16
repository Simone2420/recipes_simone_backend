from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.recipe_rating import (
    CreateRecipeRatingUseCase,
    GetRecipeRatingUseCase,
    ListRecipeRatingsByRecipeUseCase,
    UpdateRecipeRatingUseCase,
    DeleteRecipeRatingUseCase
)
from app.application.dtos.recipe_rating import CreateRecipeRatingDTO, UpdateRecipeRatingDTO
from app.infrastructure.repositories.recipe_rating_repository_impl import RecipeRatingRepositoryImpl
from app.presentation.schemas.recipe_rating_schema import (
    RecipeRatingCreate,
    RecipeRatingUpdate,
    RecipeRatingResponse
)

router = APIRouter(prefix="/recipe-ratings", tags=["recipe-ratings"])


def get_recipe_rating_repository(db: Session = Depends(get_db)) -> RecipeRatingRepositoryImpl:
    return RecipeRatingRepositoryImpl(db)


@router.post("/", response_model=RecipeRatingResponse, status_code=status.HTTP_201_CREATED)
def create_recipe_rating(
    rating_data: RecipeRatingCreate,
    rating_repo: RecipeRatingRepositoryImpl = Depends(get_recipe_rating_repository)
):
    use_case = CreateRecipeRatingUseCase(rating_repo)
    dto = CreateRecipeRatingDTO(
        value=rating_data.value,
        content=rating_data.content,
        recipe_id=rating_data.recipe_id,
        user_id=rating_data.user_id
    )
    rating = use_case.execute(dto)
    return RecipeRatingResponse.model_validate(rating)


@router.get("/recipe/{recipe_id}", response_model=List[RecipeRatingResponse])
def list_recipe_ratings_by_recipe(
    recipe_id: int,
    rating_repo: RecipeRatingRepositoryImpl = Depends(get_recipe_rating_repository)
):
    use_case = ListRecipeRatingsByRecipeUseCase(rating_repo)
    ratings = use_case.execute(recipe_id)
    return [RecipeRatingResponse.model_validate(r) for r in ratings]


@router.get("/{rating_id}", response_model=RecipeRatingResponse)
def get_recipe_rating(
    rating_id: int,
    rating_repo: RecipeRatingRepositoryImpl = Depends(get_recipe_rating_repository)
):
    use_case = GetRecipeRatingUseCase(rating_repo)
    rating = use_case.execute(rating_id)
    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe rating not found")
    return RecipeRatingResponse.model_validate(rating)


@router.put("/{rating_id}", response_model=RecipeRatingResponse)
def update_recipe_rating(
    rating_id: int,
    rating_data: RecipeRatingUpdate,
    rating_repo: RecipeRatingRepositoryImpl = Depends(get_recipe_rating_repository)
):
    try:
        use_case = UpdateRecipeRatingUseCase(rating_repo)
        dto = UpdateRecipeRatingDTO(value=rating_data.value, content=rating_data.content)
        rating = use_case.execute(rating_id, dto)
        return RecipeRatingResponse.model_validate(rating)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{rating_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe_rating(
    rating_id: int,
    rating_repo: RecipeRatingRepositoryImpl = Depends(get_recipe_rating_repository)
):
    try:
        use_case = DeleteRecipeRatingUseCase(rating_repo)
        use_case.execute(rating_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

