from fastapi import APIRouter, Depends, Path
from app.schemas.schedule import ScheduleResponse
from app.modules.schedule.service import ScheduleService
from app.dependencies import db_dependency
from starlette import status
from typing import Annotated
from app.modules.auth.service import AuthService

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

user_dependency = Annotated[dict, Depends(AuthService.get_current_user)]


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ScheduleResponse])
def list_schedules(
    db: db_dependency,
):
    return ScheduleService.list_all(db)


@router.get("/{schedule_id}", status_code=status.HTTP_200_OK, response_model=ScheduleResponse)
def get_schedule(
        db: db_dependency,
        schedule_id: int = Path(gt=0)
):
    return ScheduleService.get_by_id(db, schedule_id)
