from flask import jsonify, abort
from flask_restful import Resource, reqparse

from app import db
from models import CourseDB, StudentDB, GroupDB

ver_api = "v2"


class StudentForm:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name', type=str, required=True)
        self.parser.add_argument('last_name', type=str, required=True)
        self.parser.add_argument('group_id', type=int, required=False)


class Student(Resource, StudentForm):
    def get(self, student_id: int):
        student = StudentDB.query.get(student_id)
        if student is not None:
            return jsonify(student)
        else:
            abort(404, f"student with id: {student_id} not found")

    def put(self, student_id):
        args = self.parser.parse_args()
        StudentDB.query.filter(StudentDB.id==student_id).update(dict(first_name=args['first_name'],
                                                                     last_name=args['last_name'],
                                                                     group_id=args['group_id']))
        db.session.commit()
        return 200

    def delete(self, student_id: int):
        student = StudentDB.query.get(student_id)
        if student is None:
            return abort(304, f"no student with with id: {student_id}")
        db.session.delete(student)
        db.session.commit()
        return 200


class StudentList(Resource, StudentForm):
    def get(self):
        return jsonify(StudentDB.query.all())

    def post(self):
        args = self.parser.parse_args()
        student = StudentDB.query.filter(StudentDB.first_name==args['first_name'],
                                         StudentDB.last_name==args['last_name']).first()
        if student is not None:
            return abort(406, f"student with this data already exist")
        new_student = StudentDB(first_name=args['first_name'],
                                last_name=args['last_name'],
                                group_id=args['group_id'])
        db.session.add(new_student)
        db.session.commit()
        return 200


class CourseForm:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('course_name', type=str, required=True)
        self.parser.add_argument('description', type=str, required=False)


class Course(Resource, CourseForm):
    def get(self, course_id):
        course = CourseDB.query.get(course_id)
        if course is not None:
            return jsonify(course)
        else:
            abort(404, f"not course with this id: {course_id}")

    def put(self, course_id):
        args = self.parser.parse_args()
        name = args['course_name']
        description = args['description']
        CourseDB.query.filter(CourseDB.id==course_id).update(dict(name=name, description=description))
        db.session.commit()
        return 200

    def delete(self, course_id):
        course = CourseDB.query.get(course_id)
        db.session.delete(course)
        db.session.commit()
        return 200


class CourseList(Resource, CourseForm):
    def get(self):
        return jsonify(CourseDB.query.all())

    def post(self):
        args = self.parser.parse_args()
        course = CourseDB.query.filter(CourseDB.name==args['course_name']).first()
        if course is not None:
            return abort(406, f"course with this name already exist")
        new_course = CourseDB(name=args['course_name'], description=args['description'])
        db.session.add(new_course)
        db.session.commit()
        return 200


class GroupForm:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('group_name', type=str, required=True)


class Group(Resource, GroupForm):
    def get(self, group_id):
        group = GroupDB.query.get(group_id)
        if group is not None:
            return jsonify(group)
        else:
            abort(404, f"not group with this id: {group_id}")

    def put(self, group_id):
        args = self.parser.parse_args()
        GroupDB.query.filter(GroupDB.id==group_id).update(dict(name=args['group_name']))
        db.session.commit()
        return 200

    def delete(self, group_id):
        group = GroupDB.query.get(group_id)
        db.session.delete(group)
        db.session.commit()
        return 200


class GroupList(Resource, GroupForm):
    def get(self):
        return jsonify(GroupDB.query.all())

    def post(self):
        args = self.parser.parse_args()
        group = GroupDB.query.filter(GroupDB.name==args['group_name']).first()
        if group is not None:
            return abort(406, f"course with this name already exist")
        new_group = GroupDB(name=args['group_name'])
        db.session.add(new_group)
        db.session.commit()
        return 200


def add_urls(api_):
    api_.add_resource(Student, f"/api/{ver_api}/students/<int:student_id>")
    api_.add_resource(Course, f"/api/{ver_api}/courses/<int:course_id>")
    api_.add_resource(Group, f"/api/{ver_api}/groups/<int:group_id>")
    api_.add_resource(GroupList, f"/api/{ver_api}/groups")
    api_.add_resource(CourseList, f"/api/{ver_api}/courses")
    api_.add_resource(StudentList, f"/api/{ver_api}/students")
