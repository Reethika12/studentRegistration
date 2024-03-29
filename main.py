import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print(select)
    e1.insert(0, select["Student id"])
    e2.insert(0, select["Student Name"])
    e3.insert(0, select["Course"])
    e4.insert(0, select["Fee"])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="ammanana204", database="payroll"
    )
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  registration (studid, studname, coursename, feee) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Student registration successfull")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="ammanana204", database="payroll"
    )
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  registration set studname= %s,coursename= %s,feee= %s where studid= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record update successfull")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="ammanana204", database="payroll"
    )
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registration where studid = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Delete successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(
        host="localhost", user="root", password="ammanana204", database="payroll"
    )
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT * FROM registration")
    records = mycursor.fetchall()
    print(records)
    print(listBox.see)
    for i, (stuid, studname, coursename, feee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(stuid, studname, coursename, feee))
        mysqldb.close()
    # listBox.pack()


def delete1():
    listBox.delete(0, END)


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Student Registration", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Student ID").place(x=10, y=10)
Label(root, text="Student Name").place(x=10, y=40)
Label(root, text="Student Course").place(x=10, y=70)
Label(root, text="Fee").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="update", command=update, height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=250, y=130)

cols = ("Student id", "Student Name", "Course", "Fee")
listBox = ttk.Treeview(root, columns=cols, show="headings")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind("<Double-Button-1>", GetValue)

root.mainloop()
