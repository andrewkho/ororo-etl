import os
from sqlalchemy import create_engine

DB_URL = 'ororo-db.c3nezxtqc2fj.us-west-1.rds.amazonaws.com'
DB_USER = 'root'
DB_SECRET_LOC = os.environ.get('POSTGRES_PASSWORD')

with open(DB_SECRET_LOC, 'r') as f:
    DB_PASSWORD = f.readline()


engine = create_engine('postgresql://'root@localhost:5432/mydatabase')
