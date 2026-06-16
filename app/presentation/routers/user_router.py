from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.user import (
    CreateUserUseCase,
    GetUserUseCase,
    ListUsersUseCase,
    UpdateUserUseCase,
    DeleteUserUseCase
)
from app.application.dtos.user import CreateUserDTO, UpdateUserDTO
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.infrastructure.security.argon2_hasher import Argon2Hasher
from app.presentation.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)

router = APIRouter(prefix="/users", tags=["users"])


def get_user_repository(db: Session = Depends(get_db)) -> UserRepositoryImpl:
    return UserRepositoryImpl(db)


def get_password_hasher() -> Argon2Hasher:
    return Argon2Hasher()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    password_hasher: Argon2Hasher = Depends(get_password_hasher)
):
    try:
        use_case = CreateUserUseCase(user_repo, password_hasher)
        dto = CreateUserDTO(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password
        )
        user = use_case.execute(dto)
        return UserResponse.model_validate(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/", response_model=List[UserResponse])
def list_users(
    user_repo: UserRepositoryImpl = Depends(get_user_repository)
):
    use_case = ListUsersUseCase(user_repo)
    users = use_case.execute()
    return [UserResponse.model_validate(user) for user in users]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    user_repo: UserRepositoryImpl = Depends(get_user_repository)
):
    use_case = GetUserUseCase(user_repo)
    user = use_case.execute(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse.model_validate(user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    password_hasher: Argon2Hasher = Depends(get_password_hasher)
):
    try:
        use_case = UpdateUserUseCase(user_repo, password_hasher)
        dto = UpdateUserDTO(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password,
            status=user_data.status
        )
        user = use_case.execute(user_id, dto)
        return UserResponse.model_validate(user)
    except ValueError as e:
        if "not found" in str(e).lower():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    user_repo: UserRepositoryImpl = Depends(get_user_repository)
):
    try:
        use_case = DeleteUserUseCase(user_repo)
        use_case.execute(user_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

