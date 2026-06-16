from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.recipe import (
    CreateRecipeUseCase,
    GetRecipeUseCase,
    ListRecipesUseCase,
    ListRecipesByUserUseCase,
    UpdateRecipeUseCase,
    DeleteRecipeUseCase
)
from app.application.dtos.recipe import CreateRecipeDTO, UpdateRecipeDTO
from app.infrastructure.repositories.recipe_repository_impl import RecipeRepositoryImpl
from app.presentation.schemas.recipe_schema import (
    RecipeCreate,
    RecipeUpdate,
    RecipeResponse
)

router = APIRouter(prefix="/recipes", tags=["recipes"])


def get_recipe_repository(db: Session = Depends(get_db)) -> RecipeRepositoryImpl:
    return RecipeRepositoryImpl(db)


@router.post("/", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED)
def create_recipe(
    recipe_data: RecipeCreate,
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    use_case = CreateRecipeUseCase(recipe_repo)
    dto = CreateRecipeDTO(
        title=recipe_data.title,
        description=recipe_data.description,
        user_id=recipe_data.user_id,
        dificulty_id=recipe_data.dificulty_id
    )
    recipe = use_case.execute(dto)
    return RecipeResponse.model_validate(recipe)


@router.get("/", response_model=List[RecipeResponse])
def list_recipes(
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    use_case = ListRecipesUseCase(recipe_repo)
    recipes = use_case.execute()
    return [RecipeResponse.model_validate(r) for r in recipes]


@router.get("/user/{user_id}", response_model=List[RecipeResponse])
def list_recipes_by_user(
    user_id: int,
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    use_case = ListRecipesByUserUseCase(recipe_repo)
    recipes = use_case.execute(user_id)
    return [RecipeResponse.model_validate(r) for r in recipes]


@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(
    recipe_id: int,
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    use_case = GetRecipeUseCase(recipe_repo)
    recipe = use_case.execute(recipe_id)
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return RecipeResponse.model_validate(recipe)


@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(
    recipe_id: int,
    recipe_data: RecipeUpdate,
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    try:
        use_case = UpdateRecipeUseCase(recipe_repo)
        dto = UpdateRecipeDTO(
            title=recipe_data.title,
            description=recipe_data.description,
            status=recipe_data.status,
            dificulty_id=recipe_data.dificulty_id
        )
        recipe = use_case.execute(recipe_id, dto)
        return RecipeResponse.model_validate(recipe)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(
    recipe_id: int,
    recipe_repo: RecipeRepositoryImpl = Depends(get_recipe_repository)
):
    try:
        use_case = DeleteRecipeUseCase(recipe_repo)
        use_case.execute(recipe_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

