import argparse
from config import Session
from models import Teacher, Group, Student, Subject, Grade
from datetime import datetime

def create_teacher(session, name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Викладача '{name}' створено з ID = {teacher.id}")

def list_teachers(session):
    teachers = session.query(Teacher).all()
    if not teachers:
        print("Викладачі відсутні")
    else:
        for t in teachers:
            print(f"ID: {t.id}, Ім'я: {t.name}")

def search_teachers(session, query):
    results = session.query(Teacher).filter(Teacher.name.ilike(f"%{query}%")).all()
    if not results:
        print("Викладачі не знайдені")
    else:
        for t in results:
            print(f"ID: {t.id}, Ім'я: {t.name}")

def update_teacher(session, id_, name):
    teacher = session.get(Teacher, id_)
    if not teacher:
        print(f"Викладача з ID {id_} не знайдено")
    else:
        teacher.name = name
        session.commit()
        print(f"Викладача з ID {id_} оновлено, нове ім'я: {name}")

def remove_teacher(session, id_):
    teacher = session.get(Teacher, id_)
    if not teacher:
        print(f"Викладача з ID {id_} не знайдено")
    else:
        session.delete(teacher)
        session.commit()
        print(f"Викладача з ID {id_} видалено")

def create_group(session, name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"Групу '{name}' створено з ID = {group.id}")

def list_groups(session):
    groups = session.query(Group).all()
    if not groups:
        print("Групи відсутні")
    else:
        for g in groups:
            print(f"ID: {g.id}, Назва: {g.name}")

def search_groups(session, query):
    results = session.query(Group).filter(Group.name.ilike(f"%{query}%")).all()
    if not results:
        print("Групи не знайдені")
    else:
        for g in results:
            print(f"ID: {g.id}, Назва: {g.name}")

def update_group(session, id_, name):
    group = session.get(Group, id_)
    if not group:
        print(f"Групу з ID {id_} не знайдено")
    else:
        group.name = name
        session.commit()
        print(f"Групу з ID {id_} оновлено, нова назва: {name}")

def remove_group(session, id_):
    group = session.get(Group, id_)
    if not group:
        print(f"Групу з ID {id_} не знайдено")
    else:
        session.delete(group)
        session.commit()
        print(f"Групу з ID {id_} видалено")

def create_student(session, name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"Студента '{name}' створено з ID = {student.id}")

def list_students(session):
    students = session.query(Student).all()
    if not students:
        print("Студенти відсутні")
    else:
        for s in students:
            print(f"ID: {s.id}, Ім'я: {s.name}, Група: {s.group_id}")

def update_student(session, id_, name=None, group_id=None):
    student = session.get(Student, id_)
    if not student:
        print(f"Студента з ID {id_} не знайдено")
    else:
        if name:
            student.name = name
        if group_id:
            student.group_id = group_id
        session.commit()
        print(f"Студента з ID {id_} оновлено")

def remove_student(session, id_):
    student = session.get(Student, id_)
    if not student:
        print(f"Студента з ID {id_} не знайдено")
    else:
        session.delete(student)
        session.commit()
        print(f"Студента з ID {id_} видалено")

def create_subject(session, name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"Предмет '{name}' створено з ID = {subject.id}")

def list_subjects(session):
    subjects = session.query(Subject).all()
    if not subjects:
        print("Предмети відсутні")
    else:
        for subj in subjects:
            print(f"ID: {subj.id}, Назва: {subj.name}, Викладач ID: {subj.teacher_id}")

def update_subject(session, id_, name=None, teacher_id=None):
    subject = session.get(Subject, id_)
    if not subject:
        print(f"Предмет з ID {id_} не знайдено")
    else:
        if name:
            subject.name = name
        if teacher_id:
            subject.teacher_id = teacher_id
        session.commit()
        print(f"Предмет з ID {id_} оновлено")

def remove_subject(session, id_):
    subject = session.get(Subject, id_)
    if not subject:
        print(f"Предмет з ID {id_} не знайдено")
    else:
        session.delete(subject)
        session.commit()
        print(f"Предмет з ID {id_} видалено")

def create_grade(session, student_id, subject_id, grade, date_received=None):
    if date_received:
        try:
            date_received = datetime.strptime(date_received, "%Y-%m-%d")
        except ValueError:
            print("Неправильний формат дати. Використовуйте YYYY-MM-DD.")
            return
    else:
        date_received = datetime.utcnow()

    grade_obj = Grade(student_id=student_id, subject_id=subject_id, grade=grade, date_received=date_received)
    session.add(grade_obj)
    session.commit()
    print(f"Оцінка {grade} додана студенту ID {student_id} з предмета ID {subject_id}")

def list_grades(session):
    grades = session.query(Grade).all()
    if not grades:
        print("Оцінки відсутні")
    else:
        for g in grades:
            print(f"ID: {g.id}, Студент ID: {g.student_id}, Предмет ID: {g.subject_id}, Оцінка: {g.grade}, Дата: {g.date_received}")

def update_grade(session, id_, grade=None, date_received=None):
    grade_obj = session.get(Grade, id_)
    if not grade_obj:
        print(f"Оцінку з ID {id_} не знайдено")
    else:
        if grade is not None:
            grade_obj.grade = grade
        if date_received:
            try:
                grade_obj.date_received = datetime.strptime(date_received, "%Y-%m-%d")
            except ValueError:
                print("Неправильний формат дати. Використовуйте YYYY-MM-DD.")
                return
        session.commit()
        print(f"Оцінку з ID {id_} оновлено")

def remove_grade(session, id_):
    grade_obj = session.get(Grade, id_)
    if not grade_obj:
        print(f"Оцінку з ID {id_} не знайдено")
    else:
        session.delete(grade_obj)
        session.commit()
        print(f"Оцінку з ID {id_} видалено")

def main():
    parser = argparse.ArgumentParser(description="CLI для управління базою даних")
    parser.add_argument('-a', '--action', choices=['create', 'list', 'update', 'remove', 'search'], required=True, help="Дія")
    parser.add_argument('-m', '--model', choices=['Teacher', 'Group', 'Student', 'Subject', 'Grade'], required=True, help="Модель")
    parser.add_argument('-n', '--name', help="Ім'я або назва")
    parser.add_argument('--id', type=int, help="ID для оновлення або видалення")
    parser.add_argument('--query', help="Текст пошуку для search")
    parser.add_argument('--group_id', type=int, help="ID групи для студента")
    parser.add_argument('--teacher_id', type=int, help="ID викладача для предмета")
    parser.add_argument('--student_id', type=int, help="ID студента для оцінки")
    parser.add_argument('--subject_id', type=int, help="ID предмета для оцінки")
    parser.add_argument('--grade', type=float, help="Значення оцінки")
    parser.add_argument('--date_received', help="Дата отримання оцінки у форматі YYYY-MM-DD")

    args = parser.parse_args()

    session = Session()

    if args.action == 'create':
        if args.model == 'Teacher':
            if not args.name:
                print("Будь ласка, вкажіть ім'я за допомогою параметра -n")
            else:
                create_teacher(session, args.name)
        elif args.model == 'Group':
            if not args.name:
                print("Будь ласка, вкажіть назву за допомогою параметра -n")
            else:
                create_group(session, args.name)
        elif args.model == 'Student':
            if not args.name or not args.group_id:
                print("Будь ласка, вкажіть ім'я (-n) та ID групи (--group_id)")
            else:
                create_student(session, args.name, args.group_id)
        elif args.model == 'Subject':
            if not args.name or not args.teacher_id:
                print("Будь ласка, вкажіть назву (-n) та ID викладача (--teacher_id)")
            else:
                create_subject(session, args.name, args.teacher_id)
        elif args.model == 'Grade':
            if args.student_id is None or args.subject_id is None or args.grade is None:
                print("Будь ласка, вкажіть ID студента (--student_id), ID предмета (--subject_id) та оцінку (--grade)")
            else:
                create_grade(session, args.student_id, args.subject_id, args.grade, args.date_received)

    elif args.action == 'list':
        if args.model == 'Teacher':
            list_teachers(session)
        elif args.model == 'Group':
            list_groups(session)
        elif args.model == 'Student':
            list_students(session)
        elif args.model == 'Subject':
            list_subjects(session)
        elif args.model == 'Grade':
            list_grades(session)

    elif args.action == 'update':
        if args.model == 'Teacher':
            if not args.id or not args.name:
                print("Будь ласка, вкажіть ID (--id) та нове ім'я (-n)")
            else:
                update_teacher(session, args.id, args.name)
        elif args.model == 'Group':
            if not args.id or not args.name:
                print("Будь ласка, вкажіть ID (--id) та нову назву (-n)")
            else:
                update_group(session, args.id, args.name)
        elif args.model == 'Student':
            if not args.id:
                print("Будь ласка, вкажіть ID студента (--id)")
            else:
                update_student(session, args.id, args.name, args.group_id)
        elif args.model == 'Subject':
            if not args.id:
                print("Будь ласка, вкажіть ID предмета (--id)")
            else:
                update_subject(session, args.id, args.name, args.teacher_id)
        elif args.model == 'Grade':
            if not args.id:
                print("Будь ласка, вкажіть ID оцінки (--id)")
            else:
                update_grade(session, args.id, args.grade, args.date_received)

    elif args.action == 'remove':
        if not args.id:
            print("Будь ласка, вкажіть ID для видалення (--id)")
        else:
            if args.model == 'Teacher':
                remove_teacher(session, args.id)
            elif args.model == 'Group':
                remove_group(session, args.id)
            elif args.model == 'Student':
                remove_student(session, args.id)
            elif args.model == 'Subject':
                remove_subject(session, args.id)
            elif args.model == 'Grade':
                remove_grade(session, args.id)

    elif args.action == 'search':
        if not args.query:
            print("Будь ласка, введіть текст для пошуку через --query")
        elif args.model == 'Teacher':
            results = session.query(Teacher).filter(Teacher.name.ilike(f"%{args.query}%")).all()
            if not results:
                print("Викладачі не знайдені")
            else:
                for t in results:
                    print(f"ID: {t.id}, Ім'я: {t.name}")
        elif args.model == 'Group':
            results = session.query(Group).filter(Group.name.ilike(f"%{args.query}%")).all()
            if not results:
                print("Групи не знайдені")
            else:
                for g in results:
                    print(f"ID: {g.id}, Назва: {g.name}")
        else:
            print(f"Пошук для моделі {args.model} поки не реалізовано")

    session.close()

if __name__ == '__main__':
    main()







