from app.modules.schedule.repository import ScheduleRepository
from app.shared.exceptions import NotFoundException


class ScheduleService:

    @staticmethod
    def list_all(db):
        return ScheduleRepository.list_all(db)

    @staticmethod
    def get_by_id(db, schedule_id: int):
        schedule_model = ScheduleRepository.get_by_id(db, schedule_id)

        if not schedule_model:
            raise NotFoundException("Horário não encontrado")

        return schedule_model
