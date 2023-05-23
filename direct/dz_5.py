import random
import sqlite3

conn = sqlite3.connect(r'bd.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')

list_1 = [random.randint(1, 10) for i in range(1, 5)]
list_2 = [random.randint(1, 10) for x in range(1, 5)]

command = '''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)'''

print(list_2, list_1)
for i in range(1, 4):
    cursor.execute(command, (list_1[i], list_2[i]))
conn.commit()

cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
conn.commit()

cursor.execute('''UPDATE tab_1 SET col_1 = 'hello', col_2 = 'world' WHERE id = 3''')

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)

with open('database.txt', 'w') as file:
    for i in k:
        file.writelines(str(i) + "\n")
