# 🧠 Домашнє завдання №6 — PostgreSQL + SQLAlchemy + Alembic + Faker + CLI

---

## 📌 Опис проєкту

У цьому проєкті реалізовано взаємодію з базою даних PostgreSQL, яка включає:

- створення моделей `Student`, `Group`, `Teacher`, `Subject`, `Grade`;
- наповнення БД фейковими даними через `seed.py`;
- генерацію та виконання міграцій за допомогою Alembic;
- 10 запитів до БД відповідно до завдання;
- CLI-інтерфейс для виконання CRUD-операцій над усіма моделями.

---

## 🛠 Використані технології

- Python 3.11+
- PostgreSQL
- SQLAlchemy
- Alembic
- Faker
- argparse (CLI)
- tabulate (для форматування запитів)

---

## ⚙️ Інструкція з запуску

1. Клонуйте репозиторій:

- git clone https://github.com/your-username/goit-pythonweb-hw-06.git
- cd goit-pythonweb-hw-06

2. Створіть та активуйте віртуальне середовище:

- python3 -m venv venv
- source venv/bin/activate

3. Встановіть залежності:

- pip install -r requirements.txt

4. Запустіть PostgreSQL через Docker:

- docker run --name students-db -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres

5. Ініціалізуйте базу даних:

- python3 init_db.py

6. Створіть та застосуйте міграції Alembic:

- alembic revision --autogenerate -m "Initial migration"
- alembic upgrade head

7. Заповніть базу фейковими даними:

- python3 seed.py

8. Виконайте вибірки:

- python3 test_queries.py
- python3 test_extra_queries.py

9. Запускайте CLI:

# приклади
- python3 main.py -a create -m Teacher -n "Іван Петров"
- python3 main.py -a list -m Group
- python3 main.py -a update -m Subject --id 1 -n "Математика" --teacher_id 3
- python3 main.py -a search -m Teacher --query "Іван"

---

## 🗂 Структура проєкту

goit-pythonweb-hw-06/
├── alembic/               # Міграції
│   └── versions/          # Історія змін
├── models/                # SQLAlchemy-моделі
├── seed.py                # Заповнення БД Faker-даними
├── init_db.py             # Створення таблиць вручну
├── my_select.py           # SQL-запити 1–10 + додаткові
├── test_queries.py        # Тестування основних запитів
├── test_extra_queries.py  # Тестування додаткових запитів
├── main.py                # CLI для CRUD-операцій
├── config.py              # Налаштування підключення до БД
├── .env                   # URL для SQLAlchemy
├── alembic.ini            # Конфіг Alembic
├── .gitignore             # Ігнорує кеші, pycache, venv
├── requirements.txt       # Залежності
└── README.md              # Цей файл

---

##👤 Автор

Олександр Ребенок

GitHub: https://github.com/999Ralex999
