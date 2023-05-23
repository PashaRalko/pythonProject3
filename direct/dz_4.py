import random
import sqlite3

conn = sqlite3.connect(r'bd.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')

list_1 = [random.randint(1, 10) for i in range(1, 11)]
list_2 = [random.randint(1, 10) for x in range(1, 11)]

command = '''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)'''

print(list_2, list_1)
for i in range(1, 10):
    cursor.execute(command, (list_1[i], list_2[i]))

cursor.execute('''SELECT * FROM tab_1''')
conn.commit()
k = cursor.fetchall()
print(k)


class HomeWork:
    def __init__(self, *args):
        self.mass = []
        for i in args:
            self.mass.append(i)
        print(self.mass)

    def func(self):
        if len(self.mass) == 1:
            cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES(?, ?)''', ("NONE", "3"))
            conn.commit()
        elif len(self.mass) == 2:
            if str(self.mass[1]).isdigit():
                cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
                conn.commit()
        elif len(self.mass) == 1 and str(self.mass[2]).isdigit():
            cursor.execute('''UPDATE tab_1 SET col_1=77, col_2=77 WHERE id=3''')
            conn.commit()


a = HomeWork(1)
a.func()

cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
