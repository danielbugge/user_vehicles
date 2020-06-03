import os
from psycopg2 import connect
import psycopg2.extras

db_connection = connect(
    host=os.environ['POSTGRES_DB_HOST'],
    dbname=os.environ['POSTGRES_DB_NAME'],
    user=os.environ['POSTGRES_DB_USER']
    )
db_cur = db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
