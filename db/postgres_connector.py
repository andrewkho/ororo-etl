import os

import pandas as pd
from sqlalchemy import create_engine

DB_URL = 'ororo-db.c3nezxtqc2fj.us-west-1.rds.amazonaws.com'
DB_USER = 'root'
DB_SECRET = os.environ.get('POSTGRES_PASSWORD')
DB_DATABASE = 'ororo'

engine = create_engine('postgresql://%s:%s@%s/%s' % (DB_USER, DB_SECRET, DB_URL, DB_DATABASE))


def store_df(df, schema_name, table_name):
    # type: (pd.DataFrame, str, str) -> None
    df.to_sql(schema_name + "." + table_name, engine, if_exists='append')
