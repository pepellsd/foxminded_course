import random
import string
import names


class Generator:
    @staticmethod
    def generate_groups():
        groups =[]
        for _ in range(0, 10):
            digits = "".join([str(random.randint(0, 9)) for _ in range(0, 2)])
            chars = "".join([random.choice(string.ascii_letters) for _ in range(0, 2)])
            group_name = "{}-{}".format(chars, digits)
            groups.append(dict(name=group_name))
        return groups

    @staticmethod
    def generate_students():
        students = []
        for i in range(200):
            students.append(dict(first_name=names.get_first_name(),
                                 last_name=names.get_last_name(),
                                 group_id=random.randint(1, 10)))
        return students

    @staticmethod
    def generate_courses():
        _names = ["Biology", "PE", "Math", "Physics", "Economy", "Language X",
                  "Literature", "Drawing", "Probability theory", "Computer science"]
        courses = [dict(name=_name, description="no") for _name in _names]
        return courses

    @staticmethod
    def generate_students_on_course():
        list_sc = []
        for student in range(1, 201):
            courses_id = list(range(1,10))
            random.shuffle(courses_id)
            for _ in range(random.randint(1, 3)):
                list_sc.append(dict(student_id=student, course_id=courses_id.pop()))
        return list_sc


if __name__ == "__main__":
    print(Generator.generate_students_on_course())