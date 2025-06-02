from sqlalchemy.orm import Session
from sqlalchemy import func, desc, Numeric
from models import Student, Group, Subject, Grade, Teacher

# 1. Топ-5 студентів із найвищим середнім балом з усіх предметів
def select_1(session: Session):
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()

# 2. Студент із найвищим середнім балом з певного предмета
def select_2(session: Session, subject_id: int):
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc("avg_grade")).first()

# 3. Середній бал по кожній групі з певного предмета
def select_3(session: Session, subject_id: int):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).select_from(Group).join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()

# 4. Середній бал по всій базі (потоку)
def select_4(session: Session):
    return session.query(func.round(func.avg(Grade.grade).cast(Numeric), 2)).scalar()

# 5. Курси, які викладає певний викладач
def select_5(session: Session, teacher_id: int):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

# 6. Список студентів певної групи
def select_6(session: Session, group_id: int):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

# 7. Оцінки студентів у певній групі з певного предмета
def select_7(session: Session, group_id: int, subject_id: int):
    return session.query(
        Student.name, Grade.grade
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).all()

# 8. Середній бал, який виставляє певний викладач з усіх своїх курсів
def select_8(session: Session, teacher_id: int):
    return session.query(
        func.round(func.avg(Grade.grade).cast(Numeric), 2)
    ).join(Subject, Grade.subject_id == Subject.id).filter(Subject.teacher_id == teacher_id).scalar()

# 9. Курси, які відвідує певний студент
def select_9(session: Session, student_id: int):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).distinct().all()

# 10. Курси, які певному студентові читає певний викладач
def select_10(session: Session, student_id: int, teacher_id: int):
    return session.query(Subject.name).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).distinct().all()

# Додаткові завдання

# Середній бал, який певний викладач ставить певному студентові
def select_extra_1(session: Session, teacher_id: int, student_id: int):
    return session.query(
        func.round(func.avg(Grade.grade).cast(Numeric), 2)
    ).join(Subject, Grade.subject_id == Subject.id).filter(
        Subject.teacher_id == teacher_id,
        Grade.student_id == student_id
    ).scalar()

# Оцінки студентів у певній групі з предмета на останньому занятті
def select_extra_2(session: Session, group_id: int, subject_id: int):
    last_date = session.query(func.max(Grade.date_received)).join(Student).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).scalar()

    if not last_date:
        return []

    return session.query(
        Student.name,
        Grade.grade,
        Grade.date_received
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id,
        Grade.date_received == last_date
    ).all()
