from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.application.use_cases.permission import AssignPermissionUseCase
from app.presentation.schemas.permission_schema import AssignPermissionRequest

router = APIRouter(prefix="/permissions", tags=["permissions"])


@router.post("/assign", status_code=status.HTTP_204_NO_CONTENT)
def assign_permission(
    assign_data: AssignPermissionRequest,
    db: Session = Depends(get_db)
):
    try:
        use_case = AssignPermissionUseCase(db)
        use_case.execute(assign_data.role_id, assign_data.permission_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

