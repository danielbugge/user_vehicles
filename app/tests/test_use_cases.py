from doubles import allow, InstanceDouble

def test_get_vehicles():
    owner = 'owner'
    owners_vehicles = 'owners_vehicles'
    vehicles_repo = InstanceDouble('app.sample.repositories.vehicles_repository.VehiclesRepository')
    allow(vehicles_repo).get_vehicles.with_args(owner).and_return(owners_vehicles)

    assert vehicles_repo.get_vehicles(owner) == owners_vehicles

def test_get_user():
    username = 'username'
    password = 'password'
    user = 'user'
    users_repo = InstanceDouble('app.sample.repositories.users_repository.UsersRepository')
    allow(users_repo).get_user.with_args(username, password).and_return(user)

    assert users_repo.get_user(username, password) == user
