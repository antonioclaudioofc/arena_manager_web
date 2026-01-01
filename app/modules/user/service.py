from datetime import datetime, timezone
from app.modules.user.respository import UserRepository
from app.shared.exceptions import NotFoundException, UnathorizedException
from app.core.security import bcrypt_context


class UserService:

    @staticmethod
    def get_profile(user: dict, db):
        if not user:
            raise UnathorizedException()

        user_model = UserRepository.get_by_id(user["id"], db)

        if not user_model:
            raise NotFoundException("Usuário não encontrado")

        return user_model

    @staticmethod
    def change_password(user: dict, data, db):
        if not user:
            raise UnathorizedException()

        user_model = UserRepository.get_by_id(user["id"], db)

        if not bcrypt_context.verify(data.password, user_model.hashed_password):
            raise UnathorizedException("Senha incorreta")

        user_model.hashed_password = bcrypt_context.hash(data.new_password)
        user_model.updated_at = datetime.now(timezone.utc)

        db.commit()
