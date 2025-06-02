from faker import Faker
from sqlalchemy.orm import sessionmaker

from config import engine
from models import Group, Student, Teacher, Subject, Grade, Base

from random import randint, choice
from datetime import datetime, timedelta

fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

# Очистка таблиц (на всякий случай)
session.query(Grade).delete()
session.query(Subject).delete()
session.query(Student).delete()
session.query(Teacher).delete()
session.query(Group).delete()
session.commit()

# Создание групп
groups = [Group(name=f"Group-{i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# Преподаватели
teachers = [Teacher(name=fake.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Предметы
subjects = [
    Subject(name=fake.word().capitalize(), teacher_id=choice(teachers).id)
    for _ in range(6)
]
session.add_all(subjects)
session.commit()

# Студенты
students = [
    Student(name=fake.name(), group_id=choice(groups).id)
    for _ in range(40)
]
session.add_all(students)
session.commit()

# Оценки
grades = []
for student in students:
    for subject in subjects:
        for _ in range(randint(2, 5)):
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=randint(60, 100),
                date_received=fake.date_between(start_date="-1y", end_date="today")

            )
            grades.append(grade)

session.add_all(grades)
session.commit()

print("✅ Базу успішно заповнено даними")
