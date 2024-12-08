import sqlite3
conn = sqlite3.connect(r'C:\code\gitpythonnangcao\baitap pỵthon\chuong5\data5.4.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS hocsinh (
               id INTEGER PRIMARY KEY,
               'Name' TEXT,
               'Tuoi' INTEGER)""")

cursor.execute("""INSERT INTO hocsinh ('Name','Tuoi') VALUES
               ('vinh',18),('khanh',14)""")
conn.commit()

conn.close()