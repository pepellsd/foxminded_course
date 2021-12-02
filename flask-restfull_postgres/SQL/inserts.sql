INSERT INTO "group"(name) VALUES ('group1');
INSERT INTO "group"(name) VALUES ('group2');
INSERT INTO "group"(name) VALUES ('group3');
INSERT INTO student(FIRST_NAME, LAST_NAME, GROUP_ID)
VALUES ('alina','ilenova',3),
       ('artem','kim',1),
       ('lena', 'artamonova',3);
INSERT INTO course(name) VALUES ('math'),('PE'),('language x');
INSERT INTO students_on_course(student_id, course_id) VALUES (1,1),(2,1),(3,3);