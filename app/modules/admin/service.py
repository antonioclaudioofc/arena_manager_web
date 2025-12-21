from datetime import datetime, timezone
from models.court import Courts
from modules.admin.exceptions import AdminOnlyException
from modules.admin.repository import AdminRepository
from shared.exceptions import NotFoundException


class AdminService:

    @staticmethod
    def _ensure_admin(user: dict):
        if not user or user.get("user_role") != "admin":
            raise AdminOnlyException()

    @staticmethod
    def create_court(user: dict, court_request, db):
        AdminService._ensure_admin(user)

        court_model = Courts(
            **court_request.model_dump(),
            owner_id=user["id"],
            created_at=datetime.now(timezone.utc)
        )

        return AdminRepository.create(court_model, db)

    @staticmethod
    def delete_user(user: dict, db, user_id: int):
        AdminService._ensure_admin(user)

        user_model = AdminRepository.get_user_by_id(user_id, db)
        if not user_model:
            raise NotFoundException("Usuário não encontrado!")

        AdminRepository.delete_user(user_id, db)
