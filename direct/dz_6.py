# -*- coding: cp1251 -*-
import sqlite3

conn = sqlite3.connect(r'bd.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

list_ = ["213", 1, 2, "str", "sda", 2, 5, 7]

for i in list_:
    if isinstance(i, str):
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES(?)''', (i,))
        cursor.execute(f'''INSERT INTO tab_2(col_1) VALUES({len(i)})''')
        conn.commit()
    elif isinstance(i, int):
        if i % 2 == 0:
            cursor.execute(f'''INSERT INTO tab_2(col_1) VALUES({i})''')
            conn.commit()
            pass
        else:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES ('нечетное')''')
            conn.commit()

cursor.execute("SELECT * FROM tab_1")
k = cursor.fetchall()
print(k)

cursor.execute("SELECT * FROM tab_2")
a = cursor.fetchall()
print(a)
