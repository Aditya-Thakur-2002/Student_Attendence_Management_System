from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("2000x900+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_Dep = StringVar()
        self.var_Cor = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.var_ID = StringVar()
        self.var_Nm = StringVar()
        self.var_Gen = StringVar()
        self.var_Ph_no = StringVar()
        self.var_Email = StringVar()
        self.var_DOB = StringVar()
        self.var_photo_sample = StringVar()


        # Call fetch_data method
        

        # Background image
        img = Image.open(r"Images/19393.jpg")
        img = img.resize((1550, 900), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=1550, height=900)

        # Title
        title_lbl = Label(self.root, text="Student Management System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        main_frame = Frame(lbl, bd=2, bg="White")
        main_frame.place(x=20, y=50, width=1500, height=800)

        # Left frame for Student Details
        Left_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=750, height=500)

        # Right frame for Student Details
        right_frame = LabelFrame(main_frame, bd=2, bg="White", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=770, y=10, width=700, height=500)

        # Current course section in Left frame
        Current_Course_Left_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Current course", font=("times new roman", 12, "bold"))
        Current_Course_Left_frame.place(x=5, y=0, width=720, height=130)

        # Department
        dep_label = Label(Current_Course_Left_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=2, pady=9, sticky=W)

        dep_combo = ttk.Combobox(Current_Course_Left_frame, textvariable=self.var_Dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Management Studies", "Pharmacy", "Engineering", "Human and Social Sciences", "Business Administration", "Agricultural Sciences", "Architecture and Design", "Commerce and Finance")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=9, sticky=W)

        # Course
        course_label = Label(Current_Course_Left_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=2, pady=9, sticky=W)

        course_combo = ttk.Combobox(Current_Course_Left_frame, textvariable=self.var_Cor, font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "BCA", "MCA", "BBA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=9, sticky=W)

        # Year
        year_label = Label(Current_Course_Left_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=2, pady=9, sticky=W)

        year_combo = ttk.Combobox(Current_Course_Left_frame, textvariable=self.var_Year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "1", "2", "3", "4")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=9, sticky=W)

        # Semester
        semester_label = Label(Current_Course_Left_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=2, pady=9, sticky=W)

        semester_combo = ttk.Combobox(Current_Course_Left_frame, textvariable=self.var_Sem, font=("times new roman", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=9, sticky=W)

        # Class student information in Left frame
        Class_Student_Left_frame = LabelFrame(Left_frame, bd=2, bg="White", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_Left_frame.place(x=5, y=150, width=720, height=280)

        # Student ID
        Student_ID_label = Label(Class_Student_Left_frame, text="Student ID", font=("times new roman", 12, "bold"))
        Student_ID_label.grid(row=0, column=0, padx=2, pady=9, sticky=W)

        Student_ID_entry = ttk.Entry(Class_Student_Left_frame, textvariable=self.var_ID, width=20, font=("times new roman", 12, "bold"))
        Student_ID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student Name
        Student_Name_label = Label(Class_Student_Left_frame, text="Student Name", font=("times new roman", 12, "bold"))
        Student_Name_label.grid(row=0, column=2, padx=2, pady=9, sticky=W)

        Student_Name_entry = ttk.Entry(Class_Student_Left_frame, textvariable=self.var_Nm, width=20, font=("times new roman", 12, "bold"))
        Student_Name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Gender
        gender_label = Label(Class_Student_Left_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender_label.grid(row=1, column=0, padx=2, pady=9, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_Left_frame, textvariable=self.var_Gen, font=("times new roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=2, pady=9, sticky=W)

        # Phone Number
        phone_label = Label(Class_Student_Left_frame, text="Phone Number", font=("times new roman", 12, "bold"))
        phone_label.grid(row=1, column=2, padx=2, pady=9, sticky=W)

        phone_entry = ttk.Entry(Class_Student_Left_frame, textvariable=self.var_Ph_no, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Email
        Email_ID_label = Label(Class_Student_Left_frame, text="Email ID", font=("times new roman", 12, "bold"))
        Email_ID_label.grid(row=2, column=0, padx=2, pady=9, sticky=W)

        Email_ID_entry = ttk.Entry(Class_Student_Left_frame, textvariable=self.var_Email, width=20, font=("times new roman", 12, "bold"))
        Email_ID_entry.grid(row=2, column=1, padx=10, sticky=W)

        # DOB
        DOB_label = Label(Class_Student_Left_frame, text="DOB", font=("times new roman", 12, "bold"))
        DOB_label.grid(row=2, column=2, padx=2, pady=9, sticky=W)

        DOB_entry = ttk.Entry(Class_Student_Left_frame, textvariable=self.var_DOB, width=20, font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, sticky=W)

        # Radio Buttons for Photo Sample
        radiobutton1 = ttk.Radiobutton(Class_Student_Left_frame, text="Take photo sample", variable=self.var_photo_sample, value="Yes")
        radiobutton1.grid(row=3, column=0)

        radiobutton2 = ttk.Radiobutton(Class_Student_Left_frame, text="No photo sample", variable=self.var_photo_sample, value="No")
        radiobutton2.grid(row=3, column=1)

        # Function to add data
        def add_data():
            if self.var_Dep.get() == "Select Department" or not self.var_Nm.get() or not self.var_ID.get():
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    # Convert DOB to YYYY-MM-DD format
                    # dob_formatted = datetime.datetime.strptime(self.var_DOB.get(), "%d-%m-%Y").strftime("%d/%m/%Y")
                    conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="FACE_RECOGINATION")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        INSERT INTO student_details (Department, Course, Year, Semester, Student_ID, Student_Name, Gender, Phone_no, Email_ID, DOB, Photo_Status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        self.var_Dep.get(),
                        self.var_Cor.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_ID.get(),
                        self.var_Nm.get(),
                        self.var_Gen.get(),
                        self.var_Ph_no.get(),
                        self.var_Email.get(),
                        self.var_DOB.get(),
                        self.var_photo_sample.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)



    










        # Button Frame for Save, Update, Delete, Reset
        button_Frame = Frame(Class_Student_Left_frame, bd=2, relief=RIDGE)
        button_Frame.place(x=0, y=155, width=715, height=40)

        save_Button = Button(button_Frame, text="Save", width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white", command=add_data)
        save_Button.grid(row=0, column=0)

        update_Button=Button(button_Frame,text="Update",width=19,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        update_Button.grid(row=0,column=1)


        Delete_Button=Button(button_Frame,text="Delete",width=18,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        Delete_Button.grid(row=0,column=2)


        Reset_Button=Button(button_Frame,text="Reset",width=19,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        Reset_Button.grid(row=0,column=3)


        button_Frame1=Frame(Class_Student_Left_frame,bd=2,relief=RIDGE)
        button_Frame1.place(x=0,y=200,width=715,height=40)

        Take_Photo_Button=Button(button_Frame1,text="Take Photo Sample",width=40,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        Take_Photo_Button.grid(row=0,column=0)

        Update_Photo_Button=Button(button_Frame1,text="Update Photo Sample",width=40,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        Update_Photo_Button.grid(row=0,column=1)


        # ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,right_column,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


        # Right frame section
        Search_frame = LabelFrame(right_frame, bd=2, bg="White", relief=RIDGE, text="Search", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=1, width=680, height=130)

        Search_label = Label( Search_frame, text="Search By:", font=("times new roman", 11, "bold"))
        Search_label.grid(row=0, column=0, padx=2, pady=9, sticky=W)

        
        search_combo = ttk.Combobox(Search_frame , font=("times new roman", 11, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Student ID", "Phone number")
        search_combo .current(0)
        search_combo .grid(row=0, column=1, padx=2, pady=9, sticky=W)


        Search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 11, "bold"))
        Search_entry.grid(row=0, column=2, padx=10, sticky=W)


    


        Search_Button=Button(Search_frame,text="Search",width=14,font=("times new roman", 11, "bold"),bg="blue",fg="white")
        Search_Button.grid(row=0,column=3,padx=4)


        Show_All_Button=Button(Search_frame,text="Show_All",width=14,font=("times new roman", 11, "bold"),bg="blue",fg="white")
        Show_All_Button.grid(row=0,column=4,padx=4)

        table_frame = Frame(right_frame, bd=2, bg="White", relief=RIDGE)
        table_frame.place(x=5, y=100, width=680, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Dep","Cor","Year","Sem", "ID","Nm","Gen","Ph_no","Email","DOB","Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Cor",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Nm",text="Student Name")
        self.student_table.heading("Gen",text="Gender")
        self.student_table.heading("Ph_no",text="Phone no")
        self.student_table.heading("Email",text="Email ID")
        self.student_table.heading("DOB",text="DOB")
        
        self.student_table.heading("Photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Cor",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Nm",width=100)
        self.student_table.column("Gen",width=100)
        self.student_table.column("Ph_no",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Photo",width=100)
        
        


        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def fetch_data(self):
        # Fetch data from database and display it in the table
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abcd@1234", database="FACE_RECOGINATION")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student_details")
            rows = cursor.fetchall()

            # Clear the table
            self.student_table.delete(*self.student_table.get_children())

            # Insert new data
            for row in rows:
                self.student_table.insert("", END, values=row)

            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")
        




        

        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

