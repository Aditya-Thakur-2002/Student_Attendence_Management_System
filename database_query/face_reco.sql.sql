CREATE DATABASE FACE_RECOGNITION;
USE FACE_RECOGNITION;

CREATE TABLE student_details (
    Department VARCHAR(255),
    Course VARCHAR(255),
    Year INT,
    Semester INT,
    Student_ID VARCHAR(100) PRIMARY KEY,
    Student_Name VARCHAR(100),
    Gender VARCHAR(10),
    Phone_no VARCHAR(15),
    Email_ID VARCHAR(100),
    DOB DATE,
    Photo_Status VARCHAR(50)
);

SELECT * FROM student_details;
