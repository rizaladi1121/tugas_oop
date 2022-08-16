import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from tkcalendar import DateEntry

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
    e5.insert(0,select['jenis_sim'])
    e6.insert(0,select['no_sim'])
    e7.insert(0,select['berlaku_sim'])

def insert():
        driverNo_Ktp = e1.get()
        driverNama = e2.get()
        driverAlamat = e3.get()
        driverNo_Hp = e4.get()
        driverJenis_SIM= e5.get()
        driverNo_SIM = e6.get()
        driverBerlaku_SIM = e7.get_date()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor=mysqldb.cursor()

        try:
            sql = "INSERT INTO driver (no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (driverNo_Ktp, driverNama, driverAlamat, driverNo_Hp, driverJenis_SIM, driverNo_SIM, driverBerlaku_SIM)
            mycursor.execute(sql, val)
                
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Data Driver added successfully")

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
        mycursor.execute("SELECT id, no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim FROM driver")
        dataDriver = mycursor.fetchall()
        print(dataDriver)

        for i, (id, no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim) in enumerate(dataDriver, start= 1):
            listBox.insert("", "end", values=(id, no_ktp, nama, alamat, no_hp, jenis_sim, no_sim, berlaku_sim))
            mysqldb.close()

def update():
    driverNo_Ktp = e1.get()
    driverNama = e2.get()
    driverAlamat = e3.get()
    driverNo_Hp = e4.get()
    driverJenis_SIM = e5.get()
    driverNo_SIM = e6.get()
    driverBerlaku_SIM = e7.get_date()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update driver set no_ktp = %s, nama= %s, alamat= %s, no_hp= %s, jenis_sim= %s, berlaku_sim= %s where no_sim= %s"
        val = (driverNo_Ktp, driverNama, driverAlamat, driverNo_Hp, driverJenis_SIM, driverBerlaku_SIM, driverNo_SIM)
        mycursor.execute(sql, val)
                
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data driver updated successfully")

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
    
    driverNama = e2.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Delete from driver where nama= %s"
        val = (driverNama,)
        mycursor.execute(sql, val)          
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data pegawai deleted successfully")

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



root = Tk()
root.geometry("1020x780")
root.title("Driver")



global e1 
global e2
global e3
global e4 
global e5
global e6
global e7


tk.Label(root, text="Data Driver", fg="black", font=(None, 12)).place(x=350, y=10)
tk.Label = Label(root, text="No KTP").place(x=10, y=50)
Label(root, text="Nama").place(x=10, y=80)
Label(root, text="Alamat").place(x=10, y=110)
Label(root, text="No Hp").place(x=10, y=140)
Label(root, text="Jenis SIM").place(x=10, y=170)
Label(root, text="No SIM").place(x=10, y=200)
Label(root, text="Berlaku SIM").place(x=10, y=230)

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

e7 = DateEntry(root, selectmode='day', date_pattern='m/d/yy')
e7.grid(padx=140, pady=232)


Button(root, text="Insert", command=insert, height=1, width= 10).place(x=10, y=400)
Button(root, text="Update", command=update, height=1, width= 10).place(x=100, y=400)
Button(root, text="Delete", command=delete, height=1, width= 10).place(x=190, y=400)

cols = ('id', 'no_ktp', 'nama', 'alamat', 'no_hp', 'jenis_sim', 'no_sim', 'berlaku_sim')

listBox = ttk.Treeview(root, columns=cols, show='headings')

listBox.column('#0', width=0, stretch=YES)
listBox.column('id', anchor=CENTER, width=100)
listBox.column('no_ktp', anchor=CENTER, width=100)
listBox.column('nama', anchor=CENTER, width=200)
listBox.column('alamat', anchor=CENTER, width=200)
listBox.column('no_hp', anchor=CENTER, width=100)
listBox.column('jenis_sim', anchor=CENTER, width=100)
listBox.column('no_sim', anchor=CENTER, width=100)
listBox.column('berlaku_sim', anchor=CENTER, width=100)


for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan = 2)
    listBox.place(x=10, y=480)
show()
listBox.bind('<Double-Button-1>', getValue)


root.mainloop()