from tkinter import *
from tkinter import ttk

class HelpWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x900+0+0")
        self.root.title("Help - Face Detection Attendance System")

        # Title Label
        title_lbl = Label(self.root, text="Help & User Guide", font=("Helvetica", 30, "bold"), bg="white", fg="blue")
        title_lbl.pack(side=TOP, fill=X, pady=10)

        # Content Frame for Guide Content
        content_frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        content_frame.place(x=20, y=80, width=1960, height=780)

        # Adding Scrollbar for Content
        scrollbar_y = Scrollbar(content_frame, orient=VERTICAL)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        # Text Widget with Increased Font Size
        help_text = Text(content_frame, wrap=WORD, yscrollcommand=scrollbar_y.set, font=("Arial", 16), padx=20, pady=20)
        help_text.pack(fill=BOTH, expand=1)
        scrollbar_y.config(command=help_text.yview)

        # Help Guide Content (Expanded for readability)
        guide_content = """
        Welcome to the Face Detection Attendance System!

        This system provides an efficient and secure way to manage attendance using face recognition technology.
        Below is a detailed guide to help you make the best use of each feature.

        1. **Student Details**:
           - Navigate to this section to add, view, or modify student details.
           - Ensure that details are accurate, as they are directly linked with the attendance records.

        2. **Face Recognition**:
           - Click this feature to initiate face recognition. The system will identify and log attendance in real-time.
           - Make sure students are directly facing the camera for optimal detection accuracy.

        3. **Attendance Tracking**:
           - Attendance is marked automatically upon face detection, streamlining the process.
           - This feature removes the need for manual attendance, improving speed and accuracy.

        4. **Data Export and Import**:
           - Use the Import function to load student or attendance data from CSV files.
           - Use Export to save attendance records as CSV files for easy reporting and archiving.

        5. **Train Data**:
           - This feature is used to train the system with new face data for better recognition.
           - Regular training ensures high accuracy in face detection.

        6. **Help Section**:
           - This page provides a comprehensive guide for users, covering all features and usage tips.

        **Advantages of Face Detection Attendance System**:
        - **Speed**: Faster attendance marking, saving time.
        - **Accuracy**: High accuracy with minimal human error.
        - **Security**: Automatic, secure storage of attendance data.

        **Upcoming Feature: Chatbot (Coming Soon)**
        - Soon, a chatbot will be available to provide real-time support, answering any questions as you use the system.

        We hope you find this system intuitive and efficient. Thank you for using our Face Detection Attendance System!
        """

        # Insert content into text box
        help_text.insert(END, guide_content)
        help_text.config(state=DISABLED)  # Make the text read-only for users

# Main Program Execution
if __name__ == "__main__":
    root = Tk()
    app = HelpWindow(root)
    root.mainloop()
