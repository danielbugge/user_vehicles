from app.sample.entities.vehicle import Vehicle

class VehiclesRepository:
    def __init__(self, db_cur):
        self.db_cur = db_cur

    def get_vehicles(self, owner):
        self.db_cur.execute(
            'SELECT * FROM vehicles WHERE owner LIKE %s ORDER BY distance DESC', (owner,)
        )
        results = self.db_cur.fetchall()
        objects_results = []

        if not results:
            return objects_results

        for result in results:
            objects_results.append(self.to_vehicle(result[0], result[1], result[2]))

        return objects_results

    @classmethod
    def to_vehicle(cls, vehicle_id, distance, owner):
        return Vehicle(id=vehicle_id, distance=distance, owner=owner)
