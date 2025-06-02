from sqlalchemy.orm import sessionmaker
from config import engine
from my_select import select_extra_1, select_extra_2
from models import Student, Group, Subject, Teacher

Session = sessionmaker(bind=engine)
session = Session()

first_teacher_id = session.query(Teacher.id).first()[0]
first_student_id = session.query(Student.id).first()[0]
first_group_id = session.query(Group.id).first()[0]
first_subject_id = session.query(Subject.id).first()[0]

print("Середній бал, який певний викладач ставить студенту:")
print(select_extra_1(session, first_teacher_id, first_student_id))

print("\nОцінки студентів у групі на останньому занятті з предмета:")
results = select_extra_2(session, first_group_id, first_subject_id)
if results:
    for r in results:
        print(f"Студент: {r[0]}, Оцінка: {r[1]}, Дата: {r[2]}")
else:
    print("Дані відсутні")

session.close()

