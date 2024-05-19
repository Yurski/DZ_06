from faker import Faker
import sqlite3
import random
import os

# Ініціалізуємо Faker
fake = Faker('uk_UA')

# Створюємо з'єднання з базою даних
conn = sqlite3.connect('university.db')
cur = conn.cursor()

# Створюємо таблиці
cur.execute('''CREATE TABLE students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                group_id INTEGER)''')

cur.execute('''CREATE TABLE groups (
                id INTEGER PRIMARY KEY,
                name TEXT)''')

cur.execute('''CREATE TABLE teachers (
                id INTEGER PRIMARY KEY,
                name TEXT)''')

cur.execute('''CREATE TABLE subjects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER)''')

cur.execute('''CREATE TABLE grades (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                grade INTEGER,
                date TEXT)''')

# Заповнюємо таблиці випадковими даними

# Додамо групи
groups = ['Група 1', 'Група 2', 'Група 3']
for group_name in groups:
    cur.execute("INSERT INTO groups (name) VALUES (?)", (group_name,))
    
# Додамо викладачів
teachers = [fake.name() for _ in range(5)]
for teacher_name in teachers:
    cur.execute("INSERT INTO teachers (name) VALUES (?)", (teacher_name,))

# Додамо студентів
for _ in range(30):
    student_name = fake.name()
    group_id = random.randint(1, len(groups))
    cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (student_name, group_id))

# Додамо предмети
subjects = ['Математика', 'Фізика', 'Хімія', 'Історія', 'Література', 'Біологія', 'Інформатика']
for subject_name in subjects:
    teacher_id = random.randint(1, len(teachers))
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject_name, teacher_id))

# Додамо оцінки студентам
for student_id in range(1, 31):
    for subject_id in range(1, len(subjects) + 1):
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-1y', end_date='today')
        cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))

# Зберігаємо зміни
conn.commit()
conn.close()
