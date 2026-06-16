from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.comment import (
    CreateCommentUseCase,
    GetCommentUseCase,
    ListCommentsByRecipeUseCase,
    UpdateCommentUseCase,
    DeleteCommentUseCase
)
from app.application.dtos.comment import CreateCommentDTO, UpdateCommentDTO
from app.infrastructure.repositories.comment_repository_impl import CommentRepositoryImpl
from app.presentation.schemas.comment_schema import (
    CommentCreate,
    CommentUpdate,
    CommentResponse
)

router = APIRouter(prefix="/comments", tags=["comments"])


def get_comment_repository(db: Session = Depends(get_db)) -> CommentRepositoryImpl:
    return CommentRepositoryImpl(db)


@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment(
    comment_data: CommentCreate,
    comment_repo: CommentRepositoryImpl = Depends(get_comment_repository)
):
    use_case = CreateCommentUseCase(comment_repo)
    dto = CreateCommentDTO(
        title=comment_data.title,
        content=comment_data.content,
        recipe_id=comment_data.recipe_id,
        user_id=comment_data.user_id
    )
    comment = use_case.execute(dto)
    return CommentResponse.model_validate(comment)


@router.get("/recipe/{recipe_id}", response_model=List[CommentResponse])
def list_comments_by_recipe(
    recipe_id: int,
    comment_repo: CommentRepositoryImpl = Depends(get_comment_repository)
):
    use_case = ListCommentsByRecipeUseCase(comment_repo)
    comments = use_case.execute(recipe_id)
    return [CommentResponse.model_validate(c) for c in comments]


@router.get("/{comment_id}", response_model=CommentResponse)
def get_comment(
    comment_id: int,
    comment_repo: CommentRepositoryImpl = Depends(get_comment_repository)
):
    use_case = GetCommentUseCase(comment_repo)
    comment = use_case.execute(comment_id)
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return CommentResponse.model_validate(comment)


@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment(
    comment_id: int,
    comment_data: CommentUpdate,
    comment_repo: CommentRepositoryImpl = Depends(get_comment_repository)
):
    try:
        use_case = UpdateCommentUseCase(comment_repo)
        dto = UpdateCommentDTO(title=comment_data.title, content=comment_data.content)
        comment = use_case.execute(comment_id, dto)
        return CommentResponse.model_validate(comment)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    comment_id: int,
    comment_repo: CommentRepositoryImpl = Depends(get_comment_repository)
):
    try:
        use_case = DeleteCommentUseCase(comment_repo)
        use_case.execute(comment_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

