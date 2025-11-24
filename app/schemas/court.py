from pydantic import BaseModel, Field


class CourtCreate(BaseModel):
    name: str = Field(min_length=6)
    sport_type: str = Field(min_length=6)
    description: str = Field(min_length=6)
