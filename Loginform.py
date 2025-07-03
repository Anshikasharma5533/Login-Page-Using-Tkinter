import tkinter
from tkinter import *
from PIL import ImageTk,Image

import csv
import os
def save_to_csv():
    # Get Name
    name = windows.grid_slaves(row=3, column=2)[0].get()
    # Get Age
    age = windows.grid_slaves(row=4, column=2)[0].get()
    # Determine Gender
    gender = "Not Selected"
    # Check which radio button is selected (get() returns "selected" or "")
    if windows.grid_slaves(row=5, column=2)[0].select():
        gender = "Male"
    elif windows.grid_slaves(row=6, column=2)[0].select():
        gender = "Female"
    elif windows.grid_slaves(row=7, column=2)[0].select():
        gender = "Others"
    # Get Email
    email = windows.grid_slaves(row=8, column=2)[0].get()
    # Get Phone
    phone = windows.grid_slaves(row=9, column=2)[0].get()
    # Get Address
    address = windows.grid_slaves(row=10, column=2)[0].get()

    file_exists = os.path.isfile("students.csv")
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Age", "Gender", "Email", "Phone", "Address"])  # header
        writer.writerow([name, age, gender, email, phone, address])

windows=tkinter.Tk()
windows.title("APPLICATION FORM")
windows.configure(bg="pink")
bg_image=Image.open(r"C:\Users\HP\OneDrive\Pictures\Screenshots\Screenshot 2025-06-27 114553.png")
bg_photo=ImageTk.PhotoImage(bg_image)
bg_label=Label(windows,image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1)
#LABLE
tkinter.Label(windows,text="Students Application Form",width=40,fg="black",bg="white",font="bold").grid(row=1,column=2)

#GRID
tkinter.Label(windows,text="Name",fg="black",font="Bold",bg="lightblue").grid(row=3,column=1)
e1=Entry(windows,fg="black",font="bold",bg="white").grid(row=3,column=2)
tkinter.Label(windows,text="Age",fg="black",font="Bold",bg="lightblue").grid(row=4,column=1)
e1=Entry(windows,fg="black",font="bold",bg="white").grid(row=4,column=2)
tkinter.Label(windows,text="Gender",fg="black",font="Bold",bg="lightblue").grid(row=5,column=1)
#RADIO BUTTON
tkinter.Radiobutton(windows,text="Male",font="Italics",fg="black",value=1,bg="white").grid(row=5,column=2)
tkinter.Radiobutton(windows,text="Female",font="Italics",fg="black",value=2,bg="white").grid(row=6,column=2)
tkinter.Radiobutton(windows,text="Others",font="Italics",fg="black",value=3,bg="white").grid(row=7,column=2)
#GRID+ENTRY
tkinter.Label(windows,text="E-Mail",fg="black",font="Bold",bg="lightblue").grid(row=8,column=1)
e1=Entry(windows,fg="black",font="bold",bg="white").grid(row=8,column=2)
tkinter.Label(windows,text="Phone Number",fg="black",font="Bold",bg="lightblue").grid(row=9,column=1)
e1=Entry(windows,fg="black",font="bold",bg="white").grid(row=9,column=2)
tkinter.Label(windows,text="Address",fg="black",font="Bold",bg="lightblue").grid(row=10,column=1)
e1=Entry(windows,fg="black",font="bold",bg="white").grid(row=10,column=2)
#BUTTON

tkinter.Button(windows,text="submit",fg="white",bg="green",command=save_to_csv).grid(row=11,column=2)
windows.mainloop()
