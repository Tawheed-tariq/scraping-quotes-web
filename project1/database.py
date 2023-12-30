import sqlite3

conn = sqlite3.connect('myquotes.db') # this creates a database file named myquotes.db
curr = conn.cursor()
# this creates a table in the database file
curr.execute("""
    create table quotes_tb(
             quote text,
             author text,
             tags text
    )
""")
# this inserts a row into the table
curr.execute("""
    insert into quotes_tb values('hello', 'ho', 'this')
""")

conn.commit()
conn.close()