import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def getValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)

    e1.insert(0,select['nip'])
    e2.insert(0,select['nama'])
    e3.insert(0,select['alamat'])
    e4.insert(0,select['no_hp'])

def insert():
        pegNip = e1.get()
        pegNama = e2.get()
        pegAlamat = e3.get()
        pegNohp = e4.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor=mysqldb.cursor()

        try:
            sql = "INSERT INTO pegawai (nip,nama,alamat,no_hp) VALUES (%s,%s,%s,%s)"
            val = (pegNip,pegNama,pegAlamat,pegNohp)
            mycursor.execute(sql, val)
                
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Data pegawai added successfully")

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
        mysqldb = mysql.connector.connect(host= "localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id, nip, nama, alamat, no_hp FROM pegawai")
        dataPegawai = mycursor.fetchall()
        print(dataPegawai)

        for i, (id, nip, nama, alamat, no_hp) in enumerate(dataPegawai, start=1):
            listBox.insert("", "end", values=(id, nip, nama, alamat, no_hp))
            mysqldb.close()

def update():
    pegNip = e1.get()
    pegNama = e2.get()
    pegAlamat = e3.get()
    pegNohp = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update pegawai set nama= %s, alamat= %s, no_hp= %s where nip = %s"
        val = (pegNama, pegAlamat, pegNohp, pegNip)
        mycursor.execute(sql, val)
                
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data pegawai updated successfully")

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
    
    pegNip = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "delete from pegawai where nip = %s"
        val = (pegNip,)
        mycursor.execute(sql, val)          
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data pegawai deleted successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



root =Tk()
root.geometry("800x500")
root.title("Pegawai")
global e1 
global e2
global e3
global e4 

tk.Label(root, text="Data Pegawai", fg="black", font=(None, 12)).place(x=350, y=10)
tk.Label = Label(root, text="NIP").place(x=10, y=50)
Label(root, text="Nama").place(x=10, y=80)
Label(root, text="Alamat").place(x=10, y=110)
Label(root, text="No.Hp").place(x=10, y=140)

e1 = Entry(root)
e1.place(x=140, y=52)

e2 = Entry(root)
e2.place(x=140, y=82)

e3 = Entry(root)
e3.place(x=140, y=112)

e4 = Entry(root)
e4.place(x=140, y=142)

Button(root, text="Insert", command = insert, height=3, width= 10).place(x=10, y=200)
Button(root, text="Update", command= update, height=3, width= 10).place(x=100, y=200)
Button(root, text="Delete", command= delete, height=3, width= 10).place(x=190, y=200)

cols = ('id', 'nip', 'nama', 'alamat', 'no_hp')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan = 2)
    listBox.place(x=10, y=300)
show()
listBox.bind('<Double-Button-1>', getValue)

root.mainloop()