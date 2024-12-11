

from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import csv

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x850+0+0")
        self.root.title("Student Attendance Management System")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()

        # Title Label
        title_lbl = Label(self.root, text="Student Attendance Management System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        # Exit button
        exit_btn = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="red", fg="white", command=root.quit, cursor="hand2")
        exit_btn.place(x=1450, y=10, width=70, height=40)

        # Background image
        img = Image.open("Images/attend_Ai_image.webp")
        img = img.resize((1550, 900), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=1550, height=900)

        main_frame = Frame(lbl, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1500, height=800)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=750, height=500)

        # Current Course Frame
        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=0, width=720, height=130)

        # Attendance ID
        Label(course_frame, text="Attendance ID", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Entry(course_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        Label(course_frame, text="Name", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Entry(course_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Date
        Label(course_frame, text="Date", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Entry(course_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 12, "bold")).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        Label(course_frame, text="Department", font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Entry(course_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        Label(course_frame, text="Time", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        Entry(course_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 12, "bold")).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Attendance Status
        Label(course_frame, text="Attendance Status", font=("times new roman", 12, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky=W)
        self.attendance_combo = ttk.Combobox(course_frame, font=("times new roman", 12, "bold"), state="readonly", width=18, textvariable=self.var_atten_attendence)
        self.attendance_combo["values"] = ("Status", "Present", "Absent")
        self.attendance_combo.current(0)
        self.attendance_combo.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Button Frame
        button_frame = Frame(left_frame, bd=2, relief=RIDGE)
        button_frame.place(x=5, y=155, width=720, height=40)

        Button(button_frame, text="Import CSV", command=self.importCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(button_frame, text="Export CSV", command=self.exportCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(button_frame, text="Update", command=self.updateData, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(button_frame, text="Reset", command=self.reset_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=770, y=10, width=700, height=500)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=680, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.attendanceReportTable = ttk.Treeview(table_frame, column=("id", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        # Table headings
        self.attendanceReportTable.heading("id", text="Attendance ID")
        self.attendanceReportTable.heading("name", text="Name")
        self.attendanceReportTable.heading("department", text="Department")
        self.attendanceReportTable.heading("time", text="Time")
        self.attendanceReportTable.heading("date", text="Date")
        self.attendanceReportTable.heading("attendance", text="Attendance Status")
        self.attendanceReportTable["show"] = "headings"
        
        # Adjust columns
        for col in ("id", "name", "department", "time", "date", "attendance"):
            self.attendanceReportTable.column(col, width=100)

        self.attendanceReportTable.pack(fill=BOTH, expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Method to fetch data
    def fetchData(self, rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if file_path:
            with open(file_path) as file:
                reader = csv.reader(file)
                for row in reader:
                    mydata.append(row)
                self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        if not mydata:
            messagebox.showwarning("No Data", "There is no data to export!", parent=self.root)
            return
        file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        if file_path:
            if not file_path.endswith(".csv"):
                file_path += ".csv"
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(mydata)
                messagebox.showinfo("Data Exported", f"Data successfully exported to {os.path.basename(file_path)}")

    # Get cursor
    def get_cursor(self, event=""):
        cursor_row = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        row = content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_name.set(row[1])
        self.var_atten_dep.set(row[2])
        self.var_atten_time.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_attendence.set(row[5])

    # Update data
    def updateData(self):
        selected = self.attendanceReportTable.selection()
        if not selected:
            messagebox.showerror("No Selection", "Please select a record to update", parent=self.root)
            return
        # update code logic here
        self.attendanceReportTable.item(selected, values=(
            self.var_atten_id.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendence.get()
        ))
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

    # Reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

