from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
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

        # Title
        title_lbl = Label(self.root, text="Train Data", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        # Train button
        img6 = Image.open(r"Images/images.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b6 = Button(lbl, image=self.photoimg6, cursor="hand2")
        b6.place(x=500, y=450, width=220, height=220)
        b6_1 = Button(lbl, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=500, y=650, width=220, height=40)

    def train_classifier(self):
        data_dir = "DaTa"  # Folder containing the images for training
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

        faces = []
        ids = []

        # Check if the path contains any images
        if not path:
            messagebox.showerror("Error", "No images found in the specified data directory!")
            return

        for image_path in path:
            try:
                # Open image and convert it to grayscale
                img = Image.open(image_path).convert('L')
                image_np = np.array(img, 'uint8')

                # Extract ID from the filename by splitting on '.'
                filename = os.path.basename(image_path)
                id_str = filename.split('.')[1]  # Adjust this index if your naming convention differs
                id = int(id_str)

                faces.append(image_np)
                ids.append(id)
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)  # Wait for a short interval
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")
                continue

        # If no valid images are found, show an error
        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid training data found. Please check your images.")
            cv2.destroyAllWindows()
            return

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed!")

if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()

#