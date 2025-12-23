from models.schedule import Schedules


class ScheduleRepository:

    @staticmethod
    def create(schedule_request, db):
        db.add(schedule_request)
        db.commit()
        db.refresh(schedule_request)

        return schedule_request

    @staticmethod
    def get_by_id(db, schedule_id):
        return db.query(Schedules).filter(Schedules.id == schedule_id).first()

    @staticmethod
    def list_all(db):
        return db.query(Schedules).all()

    @staticmethod
    def delete(schedule_request, db):
        db.delete(schedule_request)
        db.commit()
