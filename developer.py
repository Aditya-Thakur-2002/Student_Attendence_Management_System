

from tkinter import *
from PIL import Image, ImageTk

class DeveloperPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x850+0+0")
        self.root.title("Developer Information")

        # Title Label
        title_lbl = Label(self.root, text="Developer Information", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        # Exit button
        exit_btn = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="red", fg="white", command=root.quit, cursor="hand2")
        exit_btn.place(x=1450, y=10, width=70, height=40)

        # Background image
        img = Image.open(r"Images/developer.jpg")  # Update this path
        img = img.resize((1550, 900), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=1550, height=900)

        # Developer Profiles Information
        developer_info = [
            {"name": "Aditya Thakur", "role": "Lead Developer", "skills": "Python, SQL", "email": "aditya@example.com", "image": "Images/team_leader.jpg"}
           
        ]

        # Displaying developer information in a single horizontal line
        x_offset = 20  # Starting x position for the first developer
        y_offset = 80  # Keep y_offset constant to avoid vertical overflow

        max_width = 1550  # Width of the window, set maximum width for all developers to fit

        for dev in developer_info:
            dev_frame = Frame(self.root, bd=2, bg="lightblue", relief=RIDGE)
            dev_frame.place(x=x_offset, y=y_offset, width=280, height=400)

            # Display developer's image
            try:
                dev_img = Image.open(dev["image"])
                dev_img = dev_img.resize((250, 250), Image.LANCZOS)
                dev_photo = ImageTk.PhotoImage(dev_img)
                img_label = Label(dev_frame, image=dev_photo)
                img_label.place(x=15, y=15, width=250, height=250)
                img_label.image = dev_photo  # Keep a reference to the image
            except Exception as e:
                print(f"Error loading image for {dev['name']}: {e}")
            
            # Display developer's info
            Label(dev_frame, text=f"Name: {dev['name']}", font=("times new roman", 15, "bold"), bg="lightblue").place(x=10, y=250)
            Label(dev_frame, text=f"Role: {dev['role']}", font=("times new roman", 15, "bold"), bg="lightblue").place(x=10, y=290)
            Label(dev_frame, text=f"Skills: {dev['skills']}", font=("times new roman", 15, "bold"), bg="lightblue").place(x=10, y=330)
            Label(dev_frame, text=f"Email: {dev['email']}", font=("times new roman", 15, "bold"), bg="lightblue").place(x=10, y=370)

            # Update x_offset for the next developer
            x_offset += 300  # Increase the x_offset for the next developer
            if x_offset > max_width - 300:  # If the next developer would overflow, stop placing more
                break

        # Back button
        back_button = Button(self.root, text="Back to Main", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.back_to_main, cursor="hand2")
        back_button.place(x=550, y=550, width=200, height=40)

    def back_to_main(self):
        self.root.destroy()  # Close this window and go back to the main application

if __name__ == "__main__":
    root = Tk()
    app = DeveloperPage(root)
    root.mainloop()