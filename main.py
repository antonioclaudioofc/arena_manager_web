from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Court(BaseModel):
    id: int
    name: str
    type: str
    location: str
    status: str


COURTS = [
    {
        "id": 1,
        "name": "Beach Volleyball Court A",
        "type": "beach_volleyball",
        "location": "North Zone",
        "status": "active"
    },
    {
        "id": 2,
        "name": "Beach Volleyball Court B",
        "type": "beach_volleyball",
        "location": "South Zone",
        "status": "active"
    },
    {
        "id": 3,
        "name": "Futevôlei Court A",
        "type": "footvolley",
        "location": "East Zone",
        "status": "active"
    },
    {
        "id": 4,
        "name": "Futsal Court",
        "type": "futsal",
        "location": "Center Complex",
        "status": "active"
    },
    {
        "id": 5,
        "name": "Society Field",
        "type": "society",
        "location": "West Zone",
        "status": "maintenance"
    }
]


@app.get("/courts")
async def list_all_courts():
    return COURTS


@app.get("/courts/by_location/{location}")
async def list_court(location: str):
    for court in COURTS:
        if court.get("location").casefold() == location.casefold():
            return court


@app.get("/courts/by_name/")
async def list_courts_by_name(name: str):
    courts_to_return = []
    for court in COURTS:
        if court.get("name").casefold() == name.casefold():
            courts_to_return.append(court)

    return courts_to_return


@app.post("/courts/create_court")
async def create_court(new_court: Court):
    COURTS.append(new_court)
