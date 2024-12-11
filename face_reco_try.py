from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
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

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="FACE_RECOGINATION")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student Name FROM student WHERE Student_ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                my_cursor.execute("SELECT Gender FROM student WHERE Student_ID=" + str(id))
                s = my_cursor.fetchone()
                s = "+".join(s) if s else "Unknown"

                my_cursor.execute("SELECT DOB FROM student WHERE Student_ID=" + str(id))
                dob = my_cursor.fetchone()
                dob = "+".join(dob) if dob else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Nm: {i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(img, f"Gen: {s}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                    cv2.putText(img, f"DOB: {dob}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 4)
                else:
                    # Unrecognized face, show red rectangle with label "Face not found in dataset"
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Face not found in dataset", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)  # Change index if multiple cameras

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
