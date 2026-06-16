from app.domain.entities.role import Role
from app.domain.repositories.role_repository import RoleRepository
from app.application.dtos.role.create_role_dto import CreateRoleDTO


class CreateRoleUseCase:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository

    def execute(self, dto: CreateRoleDTO) -> Role:
        role = Role(
            id=0,
            name=dto.name,
            description=dto.description,
            is_active=True
        )
        return self.role_repository.save(role)

