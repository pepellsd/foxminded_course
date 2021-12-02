CREATE TABLE "group"(
    id serial PRIMARY KEY ,
    name varchar(60) NOT NULL UNIQUE
);

CREATE TABLE student(
    id serial PRIMARY KEY,
    first_name varchar(60) NOT NULL ,
    last_name varchar(60) NOT NULL ,
    group_id integer REFERENCES "group" (id)
);

CREATE TABLE course(
    id serial PRIMARY KEY,
    name varchar(60) NOT NULL UNIQUE,
    description text
);

CREATE TABLE student_in_course(
    student_id INTEGER NOT NULL,FOREIGN KEY ("student_id") REFERENCES student (id),
    course_id INTEGER NOT NULL,FOREIGN KEY ("course_id") REFERENCES course (id),
    PRIMARY KEY (student_id,course_id)
);
