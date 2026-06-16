from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_db
from app.application.use_cases.role import CreateRoleUseCase, AssignRoleUseCase
from app.application.dtos.role import CreateRoleDTO
from app.infrastructure.repositories.role_repository_impl import RoleRepositoryImpl
from app.presentation.schemas.role_schema import (
    RoleCreate,
    RoleResponse,
    AssignRoleRequest
)

router = APIRouter(prefix="/roles", tags=["roles"])


def get_role_repository(db: Session = Depends(get_db)) -> RoleRepositoryImpl:
    return RoleRepositoryImpl(db)


@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(
    role_data: RoleCreate,
    role_repo: RoleRepositoryImpl = Depends(get_role_repository)
):
    use_case = CreateRoleUseCase(role_repo)
    dto = CreateRoleDTO(name=role_data.name, description=role_data.description)
    role = use_case.execute(dto)
    return RoleResponse.model_validate(role)


@router.post("/assign", status_code=status.HTTP_204_NO_CONTENT)
def assign_role(
    assign_data: AssignRoleRequest,
    db: Session = Depends(get_db)
):
    try:
        use_case = AssignRoleUseCase(db)
        use_case.execute(assign_data.user_id, assign_data.role_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

