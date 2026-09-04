from tkinter import *
from tkinter import ttk,messagebox
import qrcode
from PIL import Image,ImageTk

class qr:
    def __init__ (self, root):
        self.root = root
        self.root.title("QR Code Genrator | Developed by Rashid Farid")
        self.root.geometry("1000x1000+100+100")
        self.root.config(bd=5, relief=RIDGE, bg="white")

        # all Variables
        self.employee_id = StringVar()
        self.name = StringVar()
        self.department = StringVar()
        self.designation = StringVar()

        lbl_title = Label(self.root, text="QR Code Genrator", font=("times new roman", 30), bg="#BE7D7D", fg="white")
        lbl_title.pack(side=TOP, fill=X)

        fielfdFrame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        fielfdFrame.place(x=10, y=70, width=480, height=400)

        lbl_field_title = Label(fielfdFrame, text="Enter Text or URL", font=("times new roman", 20), bg="#332B2B", fg="white")
        lbl_field_title.pack(side=TOP, fill=X)

        lbl_employee_id = Label(fielfdFrame, text="Employye ID", font=("times new roman", 15), bg="white", fg="green")
        lbl_employee_id.place(x=10, y=50)
        lbl_name = Label(fielfdFrame, text="Name", font=("times new roman", 15), bg="white", fg="green")
        lbl_name.place(x=10, y=100)
        lbl_department = Label(fielfdFrame, text="Department", font=("times new roman", 15), bg="white", fg="green")
        lbl_department.place(x=10, y=150)
        lbl_designation = Label(fielfdFrame, text="Designation", font=("times new roman", 15), bg="white", fg="green")
        lbl_designation.place(x=10, y=200)

        # Entries
        txt_employee_id = Entry(fielfdFrame, textvariable=self.employee_id, font=("times new roman", 15), bg="lightyellow")
        txt_employee_id.place(x=200, y=50)
        txt_name = Entry(fielfdFrame, textvariable=self.name, font=("times new roman", 15), bg="lightyellow")
        txt_name.place(x=200, y=100)
        txt_department = Entry(fielfdFrame, textvariable=self.department, font=("times new roman", 15), bg="lightyellow")
        txt_department.place(x=200, y=150)
        txt_designation = Entry(fielfdFrame, textvariable=self.designation, font=("times new roman", 15), bg="lightyellow")
        txt_designation.place(x=200, y=200)

        # buttons 
        btn_qr_genrate = Button(fielfdFrame, text="QR Genrate", command=self.genrate, font=("times new roman", 15), bg="#BE7D7D", fg="white")
        btn_qr_genrate.place(x=10, y=250, width=150, height=30)
        btn_clear = Button(fielfdFrame, text="Clear", command=self.clear, font=("times new roman", 15), bg="#BE7D7D", fg="white")
        btn_clear.place(x=200, y=250, width=150, height=30)

        qrFrame = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        qrFrame.place(x=500, y=70, width=480, height=400)

        lbl_qr_title = Label(qrFrame, text="QR Code", font=("times new roman", 20), bg="#332B2B", fg="white")
        lbl_qr_title.pack(side=TOP, fill=X)

        self.lbl_qr_code = Label(qrFrame, text="QR Code will be displayed here", font=("times new roman", 15), bg="#2A39C4", fg="white",bd=1,relief=RIDGE)
        self.lbl_qr_code.place(x=90, y=65, width=300, height=300)

        # functions
    def genrate (self):
        if self.employee_id.get() == "" or self.name.get() == "" or self.department.get() == "" or self.designation.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            qr_data = f"Employee ID: {self.employee_id.get()}\nName: {self.name.get()}\nDepartment: {self.department.get()}\nDesignation: {self.designation.get()}"
            qr_code = qrcode.make(qr_data)
            qr_code.save(f"QR Code/{self.employee_id.get()}_{self.name.get()}.png")
            self.image = ImageTk.PhotoImage(Image.open(f"QR Code/{self.employee_id.get()}_{self.name.get()}.png").resize((300, 300), Image.Resampling.LANCZOS))
            self.lbl_qr_code.config(image=self.image)
            messagebox.showinfo("Success", "QR Code Generated Successfully", parent=self.root)

    def clear (self):
        self.employee_id.set("")
        self.name.set("")
        self.department.set("")
        self.designation.set("")



if __name__ == "__main__":
    root = Tk()
    obj = qr(root)
    root.mainloop()