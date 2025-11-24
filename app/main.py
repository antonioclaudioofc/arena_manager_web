from fastapi import FastAPI
from db.database import engine, Base
from routers import auth, court

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(court.router)
