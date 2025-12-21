from models.auth import Users


class UserRepository:

    @staticmethod
    def get_by_id(user_id: int, db):
        return db.query(Users).filter(Users.id == user_id).first()

    @staticmethod
    def delete(user_id: int, db):
        user_model = db.query(Users.id == user_id).first()

        if user_model:
            db.delete(user_model)
