import sqlite3
conn=sqlite3.connect('test1.db')
c=conn.cursor()
for row in c.execute('SELECT * FROM PARK'):
        print(row)
conn.commit()
conn.close()

