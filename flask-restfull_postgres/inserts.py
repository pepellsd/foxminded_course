from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from generater import Generator
from models import StudentDB, GroupDB, CourseDB, StudentsOnCourse

engine = create_engine("postgresql://pepel:123@localhost/collegue")


students = Generator.generate_students()
groups = Generator.generate_groups()
courses = Generator.generate_courses()
data_student_on_course = Generator.generate_students_on_course()
obj_list = []


with Session(engine) as session:
    for group in groups:
        obj_group = GroupDB(**group)
        obj_list.append(obj_group)
    for course in courses:
        obj_course = CourseDB(**course)
        obj_list.append(obj_course)
    session.add_all(obj_list)
    session.commit()

obj_list.clear()

with Session(engine) as session:
    stateement = StudentDB.insert().values(students)
    session.execute(stateement)
    session.commit()

with Session(engine) as session:
    statement = StudentsOnCourse.insert().values(data_student_on_course)
    session.execute(statement)
    session.commit()