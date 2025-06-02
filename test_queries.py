from sqlalchemy.orm import sessionmaker
from config import engine
from my_select import *
from models import Student, Group, Subject, Teacher
from tabulate import tabulate

Session = sessionmaker(bind=engine)
session = Session()

def print_table(title, data, headers=None):
    print(f"\n{title}")
    if not data:
        print(" - Немає даних")
        return
    print(tabulate(data, headers=headers, tablefmt="pretty"))

first_student_id = session.query(Student.id).first()[0]
first_group_id = session.query(Group.id).first()[0]
first_subject_id = session.query(Subject.id).first()[0]
first_teacher_id = session.query(Teacher.id).first()[0]

print_table("1. Топ-5 студентів з найвищим середнім балом:", select_1(session), headers=["Студент", "Середній бал"])
print_table(f"2. Студент з найвищим балом з предмета ID = {first_subject_id}:", [select_2(session, first_subject_id)], headers=["Студент", "Середній бал"])
print_table(f"3. Середній бал по групах з предмета ID = {first_subject_id}:", select_3(session, first_subject_id), headers=["Група", "Середній бал"])
print_table("4. Середній бал по всій базі:", [(select_4(session),)], headers=["Середній бал"])
print_table(f"5. Курси, які читає викладач ID = {first_teacher_id}:", select_5(session, first_teacher_id), headers=["Курс"])
print_table(f"6. Студенти в групі ID = {first_group_id}:", select_6(session, first_group_id), headers=["Студент"])
print_table(f"7. Оцінки студентів з групи ID = {first_group_id} з предмета ID = {first_subject_id}:", select_7(session, first_group_id, first_subject_id), headers=["Студент", "Оцінка"])
print_table(f"8. Середній бал, який ставить викладач ID = {first_teacher_id}:", [(select_8(session, first_teacher_id),)], headers=["Середній бал"])
print_table(f"9. Курси, які відвідує студент ID = {first_student_id}:", select_9(session, first_student_id), headers=["Курс"])
print_table(f"10. Курси, які студенту ID = {first_student_id} читає викладач ID = {first_teacher_id}:", select_10(session, first_student_id, first_teacher_id), headers=["Курс"])

session.close()



