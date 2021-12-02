--Find all groups with less or equals student count.
SELECT
       "group".name, count(student.id) AS cnt
FROM
     student
LEFT JOIN
         "group" on student.group_id = "group".id
GROUP BY
         "group".name
HAVING
       count(student.id) <= 2;
--Find all students related to the course with a given name.
select * from student
where exists (
    select 1 from student_in_course
    where student_in_course.student_id = student.id
    and exists (
        select 1 from course
        where course.id = student_in_course.course_id
        and course.name = 'language x'
    )
);
--Add new student
INSERT INTO student (first_name, last_name) VALUES (?,?);
--Delete student by STUDENT_ID
DELETE  FROM student WHERE student.id = ?;
--Add a student to the course (from a list)
INSERT INTO student_in_course(student_id, course_id) VALUES (?,?),(?,?);
--Remove the student from one of his or her courses\
DELETE FROM student_in_course WHERE course_id = ? AND student_id = ?;