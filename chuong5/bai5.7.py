import sqlite3
conn = sqlite3.connect(r'C:\code\gitpythonnangcao\baitap pỵthon\chuong5\data5.4.db')
cursor = conn.cursor()
cursor.execute("""UPDATE hocsinh SET 'Tuoi' = 19""")
row =cursor.execute("SELECT * FROM hocsinh")
conn.commit()
for rows in row:
    print(rows)
conn.close()