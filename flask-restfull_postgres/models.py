from dataclasses import dataclass
from typing import List

from app import db


class StudentsOnCourse(db.Model):
    __tablename__ = "students_on_course"
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)


@dataclass
class StudentDB(db.Model):
    __tablename__ = "student"

    id: int
    first_name: str
    last_name: str
    group_id: int

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def __repr__(self):
        return f"id:{self.id}, student name: {self.first_name}, group-id: {self.group_id}"


@dataclass
class CourseDB(db.Model):
    __tablename__ = "course"

    id: int
    name: str
    description: str
    students: List[StudentDB]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    description = db.Column(db.Text)
    students = db.relationship('StudentDB', secondary="students_on_course", lazy='subquery',
                               backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return f"id:{self.id}, course name: {self.name}"


@dataclass
class GroupDB(db.Model):
    __tablename__ = "group"

    id: int
    name: str
    students: List[StudentDB]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    students = db.relationship('StudentDB', backref='group', lazy=True)

    def __repr__(self):
        return f"id:{self.id}, group name: {self.name}"


if __name__ == "__main__":
    db.create_all()