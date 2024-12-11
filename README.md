# Student Attendance Management System with Face Recognition

This project integrates **Face Recognition** and **Generative AI** to provide an innovative solution for managing student attendance efficiently. It utilizes **OpenCV**, **MTCNN**, and facial expression recognition to detect faces, mark attendance, and analyze student engagement.

## Features
- **Face Recognition-Based Attendance**
- **Emotion Recognition for Engagement Analysis**
- **Sentiment-Based Attendance Tracking**
- **User-Friendly Interface with Navigation Features**

## Current Status
This project is incomplete and under active development. Upcoming updates will include:
- Chatbot integration for user assistance.
- Fixes for issues with linking face data for attendance.
- Enhanced emotion analytics and insights.

## Database Structure
The system uses a MySQL database with a `student_details` table containing fields like `Department`, `Course`, `Student_ID`, `Student_Name`, `Photo_Status`, etc.

### Example SQL Commands
- **Create Table:**
  ```sql
  CREATE TABLE student_details (
      Department VARCHAR(50),
      Course VARCHAR(50),
      Year INT,
      Semester INT,
      Student_ID VARCHAR(50) PRIMARY KEY,
      Student_Name VARCHAR(100),
      Gender ENUM('Male', 'Female', 'Other'),
      Phone_no VARCHAR(15),
      Email_ID VARCHAR(100),
      DOB DATE,
      Photo_Status BOOLEAN
  );
  ```


## How to Run
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aditya-Thakur-2002/Student_Attendence_Management_System.git
   cd Student_Attendence_Management_System
   ```
2. **Install Dependencies:**
   ```bash
   pip install opencv-python mtcnn
   ```
3. **Setup the Database:** Import the SQL file provided in the repository.
4. **Run the Application:**
   ```bash
   python main.py
   ```

## Contributions
This project is open to contributions and feedback. If you’d like to help, fork the repository and submit a pull request. Future updates will address existing issues and add new features. 

Thank you for your interest!

