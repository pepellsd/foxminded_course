import pytest
from flask import url_for


class TestApi:
    @pytest.mark.test_students
    def test_student_get(self, client):
        response = client.get(url_for("student", student_id=1))
        assert response.status_code == 200
        assert 'alina' == response.get_json()['first_name']

    @pytest.mark.test_students
    def test_students_post(self, client):
        response = client.post(url_for("studentlist"), data={'first_name': 'ivan', 'last_name': 'ivanov'})
        assert response.status_code == 200

    @pytest.mark.test_students
    def test_students_post_reject(self, client):
        response = client.post(url_for("studentlist"), json={'first_name': 'ivan', 'last_name': 'ivanov'})
        assert response.status_code == 406

    @pytest.mark.test_students
    def test_student_delete(self, client, session):
        response = client.delete(url_for("student", student_id=4))
        assert response.status_code == 200
        deleted_student = session.execute("select * from student where id=4")
        assert deleted_student.first() is None

    @pytest.mark.test_students
    def test_student_put(self, client, session):
        response = client.put(url_for('student', student_id=1), json={'first_name': 'alinaa', 'last_name': 'ilenova'})
        assert response.status_code == 200
        updated = session.execute("select * from student where id=1").first()
        assert "alinaa" == updated.first_name

    @pytest.mark.test_students
    def test_students_list(self, client):
        response = client.get(url_for("studentlist"))
        assert response.status_code == 200
        assert len(response.get_json()) == 3

    #-------------------------------------------------------------------------------------------------------------------

    @pytest.mark.test_courses
    def test_course_get(self, client):
        response = client.get(url_for("course", course_id=1))
        assert response.status_code == 200
        assert 'math' == response.get_json()['name']

    @pytest.mark.test_courses
    def test_courses_post(self, client):
        response = client.post(url_for("courselist"), json={'course_name': 'biology', 'description': 'no'})
        assert response.status_code == 200

    @pytest.mark.test_courses
    def test_courses_post_reject(self, client):
        response = client.post(url_for("courselist"), json={'course_name': 'biology', 'description': 'no'})
        assert response.status_code == 406

    @pytest.mark.test_courses
    def test_course_delete(self, client, session):
        response = client.delete(url_for("course", course_id=4))
        assert response.status_code == 200
        deleted_course = session.execute("select * from course where id=4")
        assert deleted_course.first() is None

    @pytest.mark.test_courses
    def test_course_put(self, client, session):
        response = client.put(url_for("course", course_id=1), json={'course_name': 'mathh', 'description': 'so cool desc'})
        assert response.status_code == 200
        updated = session.execute("select * from course where id=1").first()
        assert "mathh" == updated.name

    @pytest.mark.test_courses
    def test_courses_list(self, client):
        response = client.get(url_for("courselist"))
        assert response.status_code == 200
        assert len(response.get_json()) == 3

    #-------------------------------------------------------------------------------------------------------------------

    @pytest.mark.test_groups
    def test_group_get(self, client):
        response = client.get(url_for("group", group_id=1))
        assert response.status_code == 200
        assert 'group1' == response.get_json()['name']

    @pytest.mark.test_groups
    def test_groups_post(self, client):
        response = client.post(url_for("grouplist"), json={'group_name': 'group4'})
        assert response.status_code == 200

    @pytest.mark.test_groups
    def test_groups_post_reject(self, client):
        response = client.post(url_for("grouplist"), json={'group_name': 'group4'})
        assert response.status_code == 406

    @pytest.mark.test_groups
    def test_group_delete(self, client, session):
        response = client.delete(url_for("group", group_id=4))
        assert response.status_code == 200
        deleted_course = session.execute('select * from "group" where id=4')
        assert deleted_course.first() is None

    @pytest.mark.test_groups
    def test_group_put(self, client, session):
        response = client.put(url_for("group", group_id=1), json={'group_name': 'GROUP1'})
        assert response.status_code == 200
        updated = session.execute('select * from "group" where id=1').first()
        assert "GROUP1" == updated.name

    @pytest.mark.test_groups
    def test_groups_list(self, client):
        response = client.get(url_for("grouplist"))
        assert response.status_code == 200
        assert len(response.get_json()) == 3
