from fastapi import APIRouter
from app.presentation.routers import (
    user_router,
    auth_router,
    role_router,
    permission_router,
    difficulty_router,
    recipe_router,
    ingredient_router,
    step_router,
    recipe_image_router,
    step_image_router,
    ingredient_image_router,
    comment_router,
    recipe_rating_router,
    recipe_info_router
)

api_router = APIRouter()

api_router.include_router(user_router.router)
api_router.include_router(auth_router.router)
api_router.include_router(role_router.router)
api_router.include_router(permission_router.router)
api_router.include_router(difficulty_router.router)
api_router.include_router(recipe_router.router)
api_router.include_router(ingredient_router.router)
api_router.include_router(step_router.router)
api_router.include_router(recipe_image_router.router)
api_router.include_router(step_image_router.router)
api_router.include_router(ingredient_image_router.router)
api_router.include_router(comment_router.router)
api_router.include_router(recipe_rating_router.router)
api_router.include_router(recipe_info_router.router)

