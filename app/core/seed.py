from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.permission_model import PermisionModel
from app.infrastructure.database.models.role_permission_model import PermisionRoleModel
from app.domain.entities.role import Role
from app.domain.entities.permission import Permission


def seed_roles_and_permissions(db: Session):
    # 1. Definir permisos semilla
    permissions_data = [
        {"name": "view_recipes", "description": "Ver recetas"},
        {"name": "create_recipes", "description": "Crear recetas"},
        {"name": "edit_own_recipes", "description": "Editar tus propias recetas"},
        {"name": "delete_own_recipes", "description": "Eliminar tus propias recetas"},
        {"name": "edit_all_recipes", "description": "Editar cualquier receta"},
        {"name": "delete_all_recipes", "description": "Eliminar cualquier receta"},
        {"name": "manage_users", "description": "Gestionar usuarios"},
        {"name": "manage_roles", "description": "Gestionar roles y permisos"},
        {"name": "download_books", "description": "Descargar libros"},
    ]

    # 2. Crear permisos en BD si no existen
    permission_models = {}
    for perm_data in permissions_data:
        perm = db.query(PermisionModel).filter(PermisionModel.permision_name == perm_data["name"]).first()
        if not perm:
            perm = PermisionModel(
                permision_name=perm_data["name"],
                description=perm_data["description"],
                is_active=True
            )
            db.add(perm)
            db.flush()  # Para generar el ID
        permission_models[perm_data["name"]] = perm

    # 3. Definir roles semilla
    roles_data = [
        {
            "name": "usuario",
            "description": "Usuario básico",
            "permissions": ["view_recipes", "create_recipes", "edit_own_recipes", "delete_own_recipes"]
        },
        {
            "name": "usuario_premium",
            "description": "Usuario premium",
            "permissions": ["view_recipes", "create_recipes", "edit_own_recipes", "delete_own_recipes", "download_books"]
        },
        {
            "name": "administrador",
            "description": "Administrador del sistema",
            "permissions": ["view_recipes", "create_recipes", "edit_own_recipes", "delete_own_recipes", "edit_all_recipes", "delete_all_recipes", "manage_users", "manage_roles", "download_books"]
        }
    ]

    # 4. Crear roles y asignar permisos
    for role_data in roles_data:
        role = db.query(RoleModel).filter(RoleModel.name == role_data["name"]).first()
        if not role:
            role = RoleModel(
                name=role_data["name"],
                description=role_data["description"],
                is_active=True
            )
            db.add(role)
            db.flush()  # Para generar el ID

        # Asignar permisos al rol
        for perm_name in role_data["permissions"]:
            perm = permission_models[perm_name]
            # Verificar si la relación ya existe
            existing = db.query(PermisionRoleModel).filter(
                PermisionRoleModel.role_id == role.id,
                PermisionRoleModel.permision_id == perm.id
            ).first()
            if not existing:
                role_perm = PermisionRoleModel(role_id=role.id, permision_id=perm.id)
                db.add(role_perm)

    db.commit()
    print("✅ Semillas de roles y permisos creadas exitosamente!")


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_roles_and_permissions(db)
    finally:
        db.close()