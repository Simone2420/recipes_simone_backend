from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.application.use_cases.auth import LoginUseCase, RegisterUseCase, RefreshTokenUseCase
from app.application.dtos.auth import LoginDTO, RegisterDTO
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.infrastructure.security.argon2_hasher import Argon2Hasher
from app.infrastructure.security.jwt_service import JWTService
from app.presentation.schemas.auth_schema import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    RefreshTokenRequest
)

router = APIRouter(prefix="/auth", tags=["authentication"])


def get_user_repository(db: Session = Depends(get_db)) -> UserRepositoryImpl:
    return UserRepositoryImpl(db)


def get_password_hasher() -> Argon2Hasher:
    return Argon2Hasher()


def get_token_service() -> JWTService:
    return JWTService()


@router.post("/login", response_model=TokenResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    password_hasher: Argon2Hasher = Depends(get_password_hasher),
    token_service: JWTService = Depends(get_token_service)
):
    try:
        use_case = LoginUseCase(user_repo, password_hasher, token_service)
        dto = LoginDTO(email=login_data.email, password=login_data.password)
        return use_case.execute(dto)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(
    register_data: RegisterRequest,
    db: Session = Depends(get_db),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    password_hasher: Argon2Hasher = Depends(get_password_hasher),
    token_service: JWTService = Depends(get_token_service)
):
    try:
        use_case = RegisterUseCase(user_repo, password_hasher, token_service)
        dto = RegisterDTO(
            first_name=register_data.first_name,
            last_name=register_data.last_name,
            email=register_data.email,
            password=register_data.password
        )
        return use_case.execute(dto)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.post("/refresh-token", response_model=TokenResponse)
def refresh_token(
    refresh_data: RefreshTokenRequest,
    db: Session = Depends(get_db),
    user_repo: UserRepositoryImpl = Depends(get_user_repository),
    token_service: JWTService = Depends(get_token_service)
):
    try:
        use_case = RefreshTokenUseCase(user_repo, token_service)
        return use_case.execute(refresh_data.refresh_token)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

