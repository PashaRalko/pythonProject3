import random
import sqlite3

conn = sqlite3.connect(r'bd.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')

list_1 = [random.randint(1, 10) for i in range(1, 11)]
list_2 = [random.randint(1, 10) for x in range(1, 11)]

print(list_2, list_1)
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ("hello", "world")''')
command = '''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)'''

for i in range(1, 10):
    cursor.execute(command, (list_1[i], list_2[i]))

cursor.execute('''SELECT * FROM tab_1''')
conn.commit()
k = cursor.fetchall()

rand_id = random.choice(k)
print(rand_id)

counter_even = 0
counter_odd = 0

for i in rand_id[1: 2]:
    if i % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1

if counter_even == len(rand_id):
    cursor.execute('''DELETE FROM tab_1 WHERE id=?''', rand_id[0])
elif counter_odd == len(rand_id):
    cursor.execute('''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id=?''', rand_id[0])
else:
    print("Есть четные и нечетные элементы")
k = cursor.fetchall()
print(k)
