
import sqlalchemy as db
import pandas as pd

## create engine and connect
## following https://docs.sqlalchemy.org/en/14/tutorial/
engine = db.create_engine('sqlite+pysqlite:///datafiles/datacamp.sqlite', 
                          echo=True,
                          future = True)
'''
with engine.connect() as conn:
    result = conn.execute(db.text("select 'hello'"))
    print(result.all())
'''
    

'''with engine.connect() as conn:
    conn.execute(db.text("create table some_table (x int, y int)"))
    conn.execute(db.text("insert into some_table(x,y) values(:x,:y)"),
                 [{"x":1, "y":2}, {"x":2, "y":4}])
    conn.commit()'''

'''print("---------")
with engine.begin() as conn:
    conn.execute(
        db.text("insert into some_table (x, y) values (:x, :y)"),
        [{"x": 6, "y": 8}, 
         {"x": 9, "y": 10},
         {"x": 19, "y": 64}
         ],
        )'''
        
with engine.connect() as conn:
    result = conn.execute(
        db.text("select * from some_table where y > :y_lower and y < :y_upper"), 
        [{"y_lower": 4, "y_upper": 16}]
        )
    
    for row in result:
        print(f"x: {row.x} y: {row.y}")