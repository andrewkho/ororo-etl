import os
from sqlalchemy import create_engine

DB_URL = 'ororo-db.c3nezxtqc2fj.us-west-1.rds.amazonaws.com'
DB_USER = 'root'
DB_SECRET = os.environ.get('POSTGRES_PASSWORD')
DB_DATABASE = 'ororo'


engine = create_engine('postgresql://%s:%s@%s/%s' % (DB_USER, DB_SECRET, DB_URL, DB_DATABASE))
