import sqlite3 
conn = sqlite3.connect('pakdet.db')
c2 = conn.cursor() 
for row in c2.execute("SELECT * FROM PAKDET"):
    print(row)
conn.close()  
