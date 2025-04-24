-- Tạo bảng students
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

-- Tạo bảng courses
CREATE TABLE courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT
);

-- Tạo bảng enrollments
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    grade INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Thêm chỉ mục (index) để tăng hiệu năng truy vấn
CREATE INDEX idx_students_gender ON students(gender);
CREATE INDEX idx_enrollments_grade ON enrollments(grade);
