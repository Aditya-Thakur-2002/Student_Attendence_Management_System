
import tkinter as tk
from tkinter import *
from time import strftime
from PIL import Image, ImageTk
from Student import Student
from face_REcogination import FaceRecognition
from Attendence import Attendance
from developer import DeveloperPage
from Help import HelpWindow
from train import Train

from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x900+0+0")
        self.root.title("Face Recognition System")

        # Background image
        img = Image.open(r"Images/19393.jpg")
        img = img.resize((1550, 900), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=1550, height=900)

        # Title
        title_lbl = Label(self.root, text="Face Recognition System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        # Digital Clock
        self.clock_lbl = tk.Label(root, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        self.clock_lbl.place(x=0, y=0, width=150, height=50)
        self.update_time()

        # Student Details Button
        img1 = Image.open(r"Images/Studentsss.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(lbl, image=self.photoimg1, command=self.Student_Detail, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(lbl, text="Student Details", command=self.Student_Detail, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detector Button
        img2 = Image.open(r"Images/Human_FAce_whit_Dark_background.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(lbl, image=self.photoimg2, cursor="hand2", command=self.face_data)
        b2.place(x=500, y=100, width=220, height=220)
        b2_1 = Button(lbl, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img3 = Image.open(r"Images/attendence.jpeg.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b3 = Button(lbl, image=self.photoimg3, cursor="hand2", command=self.Attendence)
        b3.place(x=800, y=100, width=220, height=220)
        b3_1 = Button(lbl, text="Attendance", cursor="hand2", command=self.Attendence, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Chatbot Button
        img4 = Image.open(r"Images/chatbot.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b4 = Button(lbl, image=self.photoimg4, cursor="hand2", )
        b4.place(x=1100, y=100, width=220, height=220)
        b4_1 = Button(lbl, text="Chatbot", cursor="hand2",  font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train Data Button
        img5 = Image.open(r"Images/train_Data.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b5 = Button(lbl, image=self.photoimg5, command=self.train_data, cursor="hand2")
        b5.place(x=200, y=450, width=220, height=220)
        b5_1 = Button(lbl, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=200, y=650, width=220, height=40)

        # Images Button
        img6 = Image.open(r"Images/images.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(lbl, image=self.photoimg6, cursor="hand2")
        b6.place(x=500, y=450, width=220, height=220)
        b6_1 = Button(lbl, text="Images", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=650, width=220, height=40)

        # Developer Button
        img7 = Image.open(r"Images/developer.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b7 = Button(lbl, image=self.photoimg7, cursor="hand2", command=self.developer)
        b7.place(x=800, y=450, width=220, height=220)
        b7_1 = Button(lbl, text="Developer", cursor="hand2", command=self.developer, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=800, y=650, width=220, height=40)

        # Help Button
        img8 = Image.open(r"Images/help.jpeg.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b8 = Button(lbl, image=self.photoimg8, cursor="hand2", command=self.help)
        b8.place(x=1100, y=450, width=220, height=220)
        b8_1 = Button(lbl, text="Help", cursor="hand2", command=self.help, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=1100, y=650, width=220, height=40)

        # Exit button
        exit_btn = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="red", fg="white", command=root.quit, cursor="hand2")
        exit_btn.place(x=1450, y=10, width=70, height=40)

    # Function to update the digital clock
    def update_time(self):
        current_time = strftime('%H:%M:%S %p')
        self.clock_lbl.config(text=current_time)
        self.clock_lbl.after(1000, self.update_time)

    # Function for Student Details button
    def Student_Detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def Attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = DeveloperPage(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = HelpWindow(self.new_window)

   


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
