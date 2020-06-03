from pydantic import BaseModel

class Vehicle(BaseModel):
    id: str
    distance: str
    owner: str
