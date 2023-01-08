import numpy as np
import pandas as pd
import sqlite3 as db

x = 10
df = pd.DataFrame(
        {"first":['i','m','e'],
         "second":[1,2,3],
         "third":[x, x/2, x/3]}
)

conn = db.connect('datafiles/pandas_frame.db')
c = conn.cursor()

df_from_db = pd.read_sql_query("select * from demo", con=conn)

def anti_join(df_new, df_old):
    
    outer = df_new.merge(df_old, how='outer', indicator=True)
    anti_join = outer[(outer._merge=='left_only')].drop('_merge', axis=1)
    return anti_join

missing = anti_join(df, df_from_db)
print(missing )


if len(missing.index) != 0:
    df.to_sql(name='demo', 
          con=conn, 
          if_exists='append', 
          index=False)


conn.close()