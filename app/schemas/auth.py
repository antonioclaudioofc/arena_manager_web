from pydantic import BaseModel, Field 

class AuthCreate(BaseModel):
    email: str = Field(min_length=10)
    username: str = Field(min_length=6)
    first_name: str = Field(min_length=6)
    password: str = Field(min_length=6)
    role: str