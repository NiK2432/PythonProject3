from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int
class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

stations = [
    {"id": 1, "name": "МКС", "orbit": "Земля", "crew": 7},
    {"id": 2, "name": "Тяньгун", "orbit": "Земля", "crew": 3},
]

@app.get("/stations", response_model=List[Station])
def get_stations():
    return stations

@app.post("/stations", response_model=Station, status_code=status.HTTP_201_CREATED)
def create_station(station_data: StationCreate):

    new_id = stations[-1]["id"] + 1


    new_station = station_data.model_dump()
    new_station["id"] = new_id


    stations.append(new_station)

    return new_station
