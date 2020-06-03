from app.sample.entities.user import User

class UsersRepository:
    def __init__(self, db_cur):
        self.db_cur = db_cur

    def get_user(self, username, password):
        if password is None:
            self.db_cur.execute(
                'SELECT * FROM users WHERE username LIKE %s', (username,)
                )
        else:
            self.db_cur.execute(
                'SELECT * FROM users WHERE username LIKE %s AND password LIKE %s', (username, password,)
            )

        result = self.db_cur.fetchone()
        if result is None:
            return None

        return self.to_user(result[0])

    @classmethod
    def to_user(cls, username):
        return User(username=username)
