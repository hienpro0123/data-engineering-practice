CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    grade INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE INDEX idx_students_gender ON students(gender);
CREATE INDEX idx_enrollments_grade ON enrollments(grade);
INSERT INTO students (id, name, age, gender) VALUES
(1, 'Nguyen Van A', 20, 'Male'),
(2, 'Tran Thi B', 21, 'Female'),
(3, 'Le Van C', 22, 'Male');

INSERT INTO courses (id, course_name, credits) VALUES
(101, 'Toan Cao Cap', 3),
(102, 'Lap Trinh Python', 4);

INSERT INTO enrollments (student_id, course_id, grade) VALUES
(1, 101, 85),
(2, 102, 90),
(3, 102, 78);
