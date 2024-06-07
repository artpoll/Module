from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("500x300")
root.title("MySQL CRUD Operations")

def Insert():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if(id == "" or name == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please enter all fields")
    else:
        con = mysql.connect(host="localhost", user="root", password="S3tg4rc_7", database="amuht")
        cursor = con.cursor()
        cursor.execute("INSERT INTO `articulos` VALUES('" + id +"', '"+ name +"', '" + phone +"')")
        cursor.execute("commit")
        MessageBox.showinfo("Status", "Successfully Inserted")
        con.close()
        
def Del():
    if(id_entry.get() == ""):
        MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
        con = mysql.connect(host="localhost", user="root", password="S3tg4rc_7", database="amuht")
        cursor = con.cursor()
        cursor.execute("DELETE FROM `articulos` WHERE `id`='"+ id_entry.get() +"'")
        cursor.execute("commit")
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        MessageBox.showinfo("Status", "Successfully Deleted")
        con.close()
# Update funcation
def Update():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    if(name == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please enter fiels you want to update!")
    else:
        con = mysql.connect(host="localhost", user="root", password="S3tg4rc_7", database="amuht")
        cursor = con.cursor()
        cursor.execute("UPDATE `articulos` SET name = '"+ name +"', phone='"+ phone +"' where id ='"+ id +"'")
        cursor.execute("commit")
        MessageBox.showinfo("Status", "Successfully Updated")
        con.close()

def Select():
    if(id_entry.get() == ""):
        MessageBox.showinfo("ALERT","id is required to select row!")
    else:
        con = mysql.connect(host="localhost", user="root", password="S3tg4rc_7", database="amuht")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM `articulos` WHERE `id`= '" + id_entry.get() +"'")
        rows = cursor.fetchall()
        for row in rows:
            name_entry.insert(0, row[1])
            phone_entry.insert(0, row[2])
        con.close()
        
    # Now we will add labels and entry box or inputs
id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=30)

name = Label(root, text="Name:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)

phone = Label(root, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=130)
phone_entry= Entry(root, font=("verdana 15"))
phone_entry.place(x=150, y=130)

btnInsert = Button(root, text="Insert", command=Insert, font=("verdana 15")).place(x=100, y=190)
btnDelete = Button(root, text="Delete", command=Del, font=("verdana 15")).place(x=200, y=190)
btnUpdate = Button(root, text="Update", command=Update, font=("verdana 15")).place(x=320, y=190)
btnSelect= Button(root, text="Select", command=Select, font=("verdana 15")).place(x=200, y=240)
root.mainloop()