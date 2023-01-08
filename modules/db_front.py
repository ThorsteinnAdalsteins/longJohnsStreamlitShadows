import sqlite3 as db


if __name__ == '__main__':
    
    print("--- start ---")
    print('  - Create connection')
    con = db.connect('datafiles/tutorial.db')
    
    print('  - Bind the connection to a cursor')
    cur = con.cursor()
    
    print('Create the movies table')
    cur.execute("Create table movies(title, year, score)")

    print("  - Insert two lines into the table")
    cur.execute("""
    insert into movies values 
    ('Monty Python and the hoy grail', 1755, 8.2),
    ('And Now for Something Completely Different', 1971, 7.5)
                """)

    con.commit()
    
    print('  - Fetch the two lines back')
    res= cur.execute("select * from movies")
    print(res.fetchall())
    
    print("insert multiple lines")
    data = [("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
            ("Monty Python's The meaning of Life", 1983, 7.5),
            ("Monty Python's Life of Brian", 1979, 8.0)]

    cur.executemany("Insert into movies Values(?,?,?)", data)
    con.commit()
    
    print("  - Fetch lines and list using for-loop")

    for row in cur.execute("Select year, title from movies order by year desc"):
        print(row)
        
    print("  - Drop the table")
    res = cur.execute("drop table movies")

    print("  - Close the connection")
    con.close()
    print("--- end ---")