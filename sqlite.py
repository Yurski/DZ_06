import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cur = conn.cursor()

# SQL-запиту
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

# Виведення результатів
for row in rows:
    print(row)

# Закриття з'єднання
cur.close()
conn.close()
