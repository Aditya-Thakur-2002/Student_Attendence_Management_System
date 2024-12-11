from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x900+0+0")
        self.root.title("Face Recognition System")

        # Background image
        img = Image.open(r"Images/3d_img.jpg")
        img = img.resize((1550, 900), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=1550, height=900)

        # Button
        img1 = Image.open(r"Images/Human_FAce_whit_Dark_background.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(lbl, image=self.photoimg1, cursor="hand2", command=self.face_recog)
        b1.place(x=650, y=500, width=220, height=220)
        b1_1 = Button(lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.face_recog)
        b1_1.place(x=650, y=740, width=220, height=40)

        # Title
        title_lbl = Label(self.root, text="Face Detector", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

         # Exit button
        exit_btn = Button(self.root, text="back", font=("times new roman", 15, "bold"), bg="red", fg="white", command=root.quit, cursor="hand2")
        exit_btn.place(x=1450, y=10, width=70, height=40)


        # attendence.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    def mark_attendence(self,i,sid,dob):
        with open("FAce_Data.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (sid not in name_list) and (dob not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{sid},{dob},{dtString},{d1},present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Abcd@1234",
                    database="FACE_RECOGNITION"
                )
                my_cursor = conn.cursor()

                # Fetch student details based on Student_ID
                my_cursor.execute("SELECT Student_Name FROM student_details WHERE Student_ID = %s", (id,))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                my_cursor.execute("SELECT Student_ID FROM student_details WHERE Student_ID = %s", (id,))
                sid = my_cursor.fetchone()
                sid = sid[0] if sid else "Unknown"

                my_cursor.execute("SELECT DOB FROM student_details WHERE Student_ID = %s", (id,))
                dob = my_cursor.fetchone()
                dob = dob[0] if dob else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Name: {i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 4)
                    cv2.putText(img, f"ID: {sid}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 4)
                    cv2.putText(img, f"DOB: {dob}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 4)
                    self.mark_attendence(i, sid, dob)
                else:
                    # Unrecognized face, show red rectangle with label "Face not found in dataset"
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Face not found in dataset", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]
                conn.close()

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # Change index if needed

        # Check if the camera opened successfully
        if not video_cap.isOpened():
            print("Error: Could not open camera.")
            messagebox.showerror("Camera Error", "Could not open camera. Please check if the camera is connected and not used by another application.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:  # Check if frame is captured
                print("Failed to capture image from camera. Exiting.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()



                