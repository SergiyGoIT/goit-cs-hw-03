from faker import Faker
import psycopg2
import random

fake = Faker()

connection = psycopg2.connect(
    dbname="tasks_db",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

# Додати статуси
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))

# Додати користувачів
for _ in range(10):
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s);",
                   (fake.name(), fake.unique.email()))

# Додати завдання
for _ in range(20):
    cursor.execute("""
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (%s, %s, %s, %s);
    """, (
        fake.sentence(nb_words=4),
        fake.text(),
        random.randint(1, 3),
        random.randint(1, 10)
    ))

connection.commit()
cursor.close()
connection.close()
