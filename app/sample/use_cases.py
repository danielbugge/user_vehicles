from app.sample.database import DB_CUR
from app.sample.repositories.vehicles_repository import VehiclesRepository
from app.sample.repositories.users_repository import UsersRepository

users_repo = UsersRepository(DB_CUR)
vehicles_repo = VehiclesRepository(DB_CUR)

def get_vehicles(owner):
    return vehicles_repo.get_vehicles(owner)

def get_user(username, password=None):
    return users_repo.get_user(username, password)
