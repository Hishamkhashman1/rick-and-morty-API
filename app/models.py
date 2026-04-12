from typing import Optional
from sqlmodel import Field, SQLModel

class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str
    species: str
    type: str
    gender: str
    place_of_origin: str
