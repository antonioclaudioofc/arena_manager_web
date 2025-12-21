from models.auth import Users


class AdminRepository:

    @staticmethod
    def create_court(model, db):
        db.add(model)
        db.commit()
        db.refresh(model)

        return model

    @staticmethod
    def get_user_by_id(user_id: int, db):
        return db.query(Users).filter(Users.id == user_id).first()

    @staticmethod
    def delete_user(user_id: int, db):
        db.query(Users).filter(Users.id == user_id).delete()