from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.ingredient_image import (
    CreateIngredientImageUseCase,
    GetIngredientImageUseCase,
    ListIngredientImagesByIngredientUseCase,
    UpdateIngredientImageUseCase,
    DeleteIngredientImageUseCase
)
from app.application.dtos.ingredient_image import CreateIngredientImageDTO, UpdateIngredientImageDTO
from app.infrastructure.repositories.ingredient_image_repository_impl import IngredientImageRepositoryImpl
from app.presentation.schemas.ingredient_image_schema import (
    IngredientImageCreate,
    IngredientImageUpdate,
    IngredientImageResponse
)

router = APIRouter(prefix="/ingredient-images", tags=["ingredient-images"])


def get_ingredient_image_repository(db: Session = Depends(get_db)) -> IngredientImageRepositoryImpl:
    return IngredientImageRepositoryImpl(db)


@router.post("/", response_model=IngredientImageResponse, status_code=status.HTTP_201_CREATED)
def create_ingredient_image(
    image_data: IngredientImageCreate,
    image_repo: IngredientImageRepositoryImpl = Depends(get_ingredient_image_repository)
):
    use_case = CreateIngredientImageUseCase(image_repo)
    dto = CreateIngredientImageDTO(image_url=image_data.image_url, ingredient_id=image_data.ingredient_id)
    image = use_case.execute(dto)
    return IngredientImageResponse.model_validate(image)


@router.get("/ingredient/{ingredient_id}", response_model=List[IngredientImageResponse])
def list_ingredient_images_by_ingredient(
    ingredient_id: int,
    image_repo: IngredientImageRepositoryImpl = Depends(get_ingredient_image_repository)
):
    use_case = ListIngredientImagesByIngredientUseCase(image_repo)
    images = use_case.execute(ingredient_id)
    return [IngredientImageResponse.model_validate(i) for i in images]


@router.get("/{image_id}", response_model=IngredientImageResponse)
def get_ingredient_image(
    image_id: int,
    image_repo: IngredientImageRepositoryImpl = Depends(get_ingredient_image_repository)
):
    use_case = GetIngredientImageUseCase(image_repo)
    image = use_case.execute(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ingredient image not found")
    return IngredientImageResponse.model_validate(image)


@router.put("/{image_id}", response_model=IngredientImageResponse)
def update_ingredient_image(
    image_id: int,
    image_data: IngredientImageUpdate,
    image_repo: IngredientImageRepositoryImpl = Depends(get_ingredient_image_repository)
):
    try:
        use_case = UpdateIngredientImageUseCase(image_repo)
        dto = UpdateIngredientImageDTO(image_url=image_data.image_url)
        image = use_case.execute(image_id, dto)
        return IngredientImageResponse.model_validate(image)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient_image(
    image_id: int,
    image_repo: IngredientImageRepositoryImpl = Depends(get_ingredient_image_repository)
):
    try:
        use_case = DeleteIngredientImageUseCase(image_repo)
        use_case.execute(image_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

