from app.sample.repositories.vehicles_repository import VehiclesRepository
from app.sample.repositories.users_repository import UsersRepository
from app.sample.database import db_cur

users_repo = UsersRepository(db_cur)
vehicles_repo = VehiclesRepository(db_cur)

def get_vehicles(owner):
    return vehicles_repo.get_vehicles(owner)

def get_user(username, password=None):
    return users_repo.get_user(username, password)
