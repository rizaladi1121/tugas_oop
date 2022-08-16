import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def getValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)

    e1.insert(0,select['no_ktp'])
    e2.insert(0,select['nama'])
    e3.insert(0,select['alamat'])
    e4.insert(0,select['no_hp'])
    e5.insert(0,select['email'])
    e6.insert(0,select['no_sim'])
    e7.insert(0,select['status'])

def insert():
        konsumenNo_Ktp = e1.get()
        konsumenNama = e2.get()
        konsumenAlamat = e3.get()
        konsumenNoHp = e4.get()
        konsumenEmail = e5.get()
        konsumenNoSim = e6.get()
        konsumenStatus = e7.get()

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor=mysqldb.cursor()

        try:
            sql = "INSERT INTO konsumen (no_ktp,nama,alamat,no_hp,email,no_sim,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = (konsumenNo_Ktp,konsumenNama,konsumenAlamat,konsumenNoHp, konsumenEmail,konsumenNoSim, konsumenStatus)
            mycursor.execute(sql, val)
                
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Data konsumen added successfully")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)

            e1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host= "localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id, no_ktp, nama, alamat, no_hp, email, no_sim, status FROM konsumen")
        dataKonsumen = mycursor.fetchall()
        print(dataKonsumen)

        for i, (id, no_ktp, nama, alamat, no_hp,email, no_sim,status ) in enumerate(dataKonsumen, start=1):
            listBox.insert("", "end", values=(id, no_ktp, nama, alamat, no_hp,email, no_sim,status ))
            mysqldb.close()

def update():
    konsumenNo_Ktp = e1.get()
    konsumenNama = e2.get()
    konsumenAlamat = e3.get()
    konsumenNoHp = e4.get()
    konsumenEmail = e5.get()
    konsumenNoSim = e6.get()
    konsumenStatus = e7.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update konsumen set no_ktp= %s, nama= %s, alamat= %s, no_hp= %s,email= %s,status= %s where no_sim = %s"
        val = (konsumenNo_Ktp,konsumenNama, konsumenAlamat, konsumenNoHp,konsumenEmail,konsumenStatus,konsumenNoSim)
        mycursor.execute(sql, val)
                
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data konsumen updated successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    
    konsumenNo_Ktp = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "delete from konsumen where no_ktp = %s"
        val = (konsumenNo_Ktp,)
        mycursor.execute(sql, val)          
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data konsumen deleted successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



root =Tk()
root.geometry("800x500")
root.title("Konsumen")
global e1 
global e2
global e3
global e4 
global e5 
global e6 
global e7 

# no_ktp
# nama
# alamat
# no_hp
# email
# no_sim
# status


tk.Label(root, text="Data Konsumen", fg="black", font=(None, 12)).place(x=350, y=10)
tk.Label = Label(root, text="No.Ktp").place(x=10, y=50)
Label(root, text="Nama").place(x=10, y=80)
Label(root, text="Alamat").place(x=10, y=110)
Label(root, text="No.Hp").place(x=10, y=140)
Label(root, text="Email").place(x=10, y=170)
Label(root, text="No.SIM").place(x=10, y=200)
Label(root, text="Status").place(x=10, y=230)

e1 = Entry(root)
e1.place(x=140, y=52)

e2 = Entry(root)
e2.place(x=140, y=82)

e3 = Entry(root)
e3.place(x=140, y=112)

e4 = Entry(root)
e4.place(x=140, y=142)

e5 = Entry(root)
e5.place(x=140, y=172)

e6 = Entry(root)
e6.place(x=140, y=202)

e7 = Entry(root)
e7.place(x=140, y=232)

Button(root, text="Insert", command=insert, height=1, width= 10).place(x=10, y=280)
Button(root, text="Update", command=update, height=1, width= 10).place(x=100, y=280)
Button(root, text="Delete", command=delete, height=1, width= 10).place(x=190, y=280)

cols = ('id', 'no_ktp', 'nama', 'alamat', 'no_hp', 'email', 'no_sim', 'status')
listBox = ttk.Treeview(root, columns=cols, show='headings')

listBox.column('#0', width=0, stretch=YES)
listBox.column('id', anchor=CENTER, width=100)
listBox.column('no_ktp', anchor=CENTER, width=100)
listBox.column('nama', anchor=CENTER, width=200)
listBox.column('alamat', anchor=CENTER, width=200)
listBox.column('no_hp', anchor=CENTER, width=100)
listBox.column('email', anchor=CENTER, width=100)
listBox.column('no_sim', anchor=CENTER, width=100)
listBox.column('status', anchor=CENTER, width=100)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan = 2)
    listBox.place(x=10, y=350)
show()
listBox.bind('<Double-Button-1>', getValue)

root.mainloop()