from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.recipe_image import (
    CreateRecipeImageUseCase,
    GetRecipeImageUseCase,
    ListRecipeImagesByRecipeUseCase,
    UpdateRecipeImageUseCase,
    DeleteRecipeImageUseCase
)
from app.application.dtos.recipe_image import CreateRecipeImageDTO, UpdateRecipeImageDTO
from app.infrastructure.repositories.recipe_image_repository_impl import RecipeImageRepositoryImpl
from app.presentation.schemas.recipe_image_schema import (
    RecipeImageCreate,
    RecipeImageUpdate,
    RecipeImageResponse
)

router = APIRouter(prefix="/recipe-images", tags=["recipe-images"])


def get_recipe_image_repository(db: Session = Depends(get_db)) -> RecipeImageRepositoryImpl:
    return RecipeImageRepositoryImpl(db)


@router.post("/", response_model=RecipeImageResponse, status_code=status.HTTP_201_CREATED)
def create_recipe_image(
    image_data: RecipeImageCreate,
    image_repo: RecipeImageRepositoryImpl = Depends(get_recipe_image_repository)
):
    use_case = CreateRecipeImageUseCase(image_repo)
    dto = CreateRecipeImageDTO(image_url=image_data.image_url, recipe_id=image_data.recipe_id)
    image = use_case.execute(dto)
    return RecipeImageResponse.model_validate(image)


@router.get("/recipe/{recipe_id}", response_model=List[RecipeImageResponse])
def list_recipe_images_by_recipe(
    recipe_id: int,
    image_repo: RecipeImageRepositoryImpl = Depends(get_recipe_image_repository)
):
    use_case = ListRecipeImagesByRecipeUseCase(image_repo)
    images = use_case.execute(recipe_id)
    return [RecipeImageResponse.model_validate(i) for i in images]


@router.get("/{image_id}", response_model=RecipeImageResponse)
def get_recipe_image(
    image_id: int,
    image_repo: RecipeImageRepositoryImpl = Depends(get_recipe_image_repository)
):
    use_case = GetRecipeImageUseCase(image_repo)
    image = use_case.execute(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe image not found")
    return RecipeImageResponse.model_validate(image)


@router.put("/{image_id}", response_model=RecipeImageResponse)
def update_recipe_image(
    image_id: int,
    image_data: RecipeImageUpdate,
    image_repo: RecipeImageRepositoryImpl = Depends(get_recipe_image_repository)
):
    try:
        use_case = UpdateRecipeImageUseCase(image_repo)
        dto = UpdateRecipeImageDTO(image_url=image_data.image_url)
        image = use_case.execute(image_id, dto)
        return RecipeImageResponse.model_validate(image)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe_image(
    image_id: int,
    image_repo: RecipeImageRepositoryImpl = Depends(get_recipe_image_repository)
):
    try:
        use_case = DeleteRecipeImageUseCase(image_repo)
        use_case.execute(image_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

