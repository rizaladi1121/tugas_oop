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
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)

    e1.insert(0,select['nama_mobil'])
    e2.insert(0,select['jenis_mobil'])
    e3.insert(0,select['warna'])
    e4.insert(0,select['tahun'])
    e5.insert(0,select['stnk_atas_nama'])
    e6.insert(0,select['no_rangka'])
    e7.insert(0,select['no_mesin'])
    e8.insert(0,select['no_polisi'])
    e9.insert(0,select['status_pajak'])
    e10.insert(0,select['berlaku_stnk'])
    e11.insert(0,select['harga_sewa'])
    e12.insert(0,select['status'])

def insert():
        namaMobil = e1.get()
        jenisMobil = e2.get()
        warnaMobil = e3.get()
        tahunMobil = e4.get()
        stnkAtasNama= e5.get()
        noRangka = e6.get()
        noMesin = e7.get()
        noPol = e8.get()
        statusPajak = e9.get()
        berlakuStnk = e10.get_date()
        hargaSewa = e11.get()
        status = e12.get()
        
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
        mycursor=mysqldb.cursor()
	
        try:
            sql = "INSERT INTO mobil (nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka, no_mesin, no_polisi,status_pajak, berlaku_stnk, harga_sewa, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (namaMobil, jenisMobil, warnaMobil, tahunMobil, stnkAtasNama, noRangka, noMesin,noPol, statusPajak, berlakuStnk, hargaSewa, status
)
            mycursor.execute(sql, val)
                
            mysqldb.commit()
            lastid = mycursor.lastrowid
            messagebox.showinfo("information", "Data mobil added successfully")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)
            e12.delete(0, END)

            e1.focus_set()

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host= "localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")

        mycursor = mysqldb.cursor()

        mycursor.execute("SELECT id, nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka, no_mesin, no_polisi, status_pajak, berlaku_stnk, harga_sewa, status FROM mobil")

        dataMobil = mycursor.fetchall()

        print(dataMobil)

        for i, (id, nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka, no_mesin, no_polisi, status_pajak, berlaku_stnk, harga_sewa, status) in enumerate(dataMobil, start= 1):
            listBox.insert("", "end", values=(id, nama_mobil, jenis_mobil, warna, tahun, stnk_atas_nama, no_rangka,	no_mesin, no_polisi, status_pajak, berlaku_stnk, harga_sewa, status))
            mysqldb.close()

def update():
    namaMobil = e1.get()
    jenisMobil = e2.get()
    warnaMobil = e3.get()
    tahunMobil = e4.get()
    stnkAtasNama= e5.get()
    noRangka = e6.get()
    noMesin = e7.get()
    noPol = e8.get()
    statusPajak = e9.get()
    berlakuStnk = e10.get_date()
    hargaSewa = e11.get()
    status = e12.get()   
    

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update mobil set nama_mobil = %s, jenis_mobil= %s, warna= %s, tahun= %s, stnk_atas_nama= %s, no_rangka= %s, no_mesin= %s, no_polisi= %s,status_pajak= %s, berlaku_stnk= %s, harga_sewa= %s, where no_rangka = %s"

        val = (namaMobil, jenisMobil ,warnaMobil, tahunMobil, stnkAtasNama, noRangka, noMesin, noPol, statusPajak, berlakuStnk, hargaSewa, status )

        mycursor.execute(sql, val)
                
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data Mobil Updated Successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)
        
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    
    noRangka = e6.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="uas_oop_7101210008_rizal_adi_n")
    mycursor=mysqldb.cursor()

    try:
        sql = "Delete from mobil where no_rangka= %s"
        val = (noRangka,)
        mycursor.execute(sql, val)          
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Data Mobil deleted successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)

        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()



root = Tk()
root.geometry("1020x780")
root.title("Mobil")

global e1 
global e2
global e3
global e4 
global e5
global e6
global e7
global e8
global e9
global e10
global e11
global e12


tk.Label(root, text="Data Mobil", fg="black", font=(None, 12)).place(x=350, y=10)
tk.Label = Label(root, text="Nama mobil").place(x=10, y=50)
Label(root, text="Jenis Mobil").place(x=10, y=80)
Label(root, text="Warna").place(x=10, y=110)
Label(root, text="Tahun").place(x=10, y=140)
Label(root, text="STNK Atas Nama").place(x=10, y=170)
Label(root, text="No Rangka").place(x=10, y=200)
Label(root, text="No Mesin").place(x=10, y=230)
Label(root, text="No polisi").place(x=10, y=260)
Label(root, text="Status Pajak").place(x=10, y=290)
Label(root, text="Berlaku STNK").place(x=10, y=320)
Label(root, text="Harga Sewa").place(x=10, y=350)
Label(root, text="Status").place(x=10, y=380)


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

e8 = Entry(root)
e8.place(x=140, y=262)

e9 = Entry(root)
e9.place(x=140, y=292)

e10 = DateEntry(root, selectmode='day', date_pattern='dd/m/yy')
e10.grid(padx=140, pady=322)

e11 = Entry(root)
e11.place(x=140, y=352)

e12 = Entry(root)
e12.place(x=140, y=392)




Button(root, text="Insert", command=insert, height=1, width= 10).place(x=10, y=440)
Button(root, text="Update", command=update, height=1, width= 10).place(x=100, y=440)
Button(root, text="Delete", command=delete, height=1, width= 10).place(x=190, y=440)

cols = ('id', 'nama_mobil', 'jenis_mobil', 'warna', 'tahun', 'stnk_atas_nama', 'no_rangka', 'no_mesin', 'no_polisi', 'status_pajak','berlaku_stnk','harga_sewa','status')

listBox = ttk.Treeview(root, columns=cols, show='headings')

listBox.column('#0', width=0, stretch=YES)                          
listBox.column('id', anchor=CENTER, width=100)
listBox.column('nama_mobil', anchor=CENTER, width=100)
listBox.column('jenis_mobil', anchor=CENTER, width=100)
listBox.column('warna', anchor=CENTER, width=100)
listBox.column('tahun', anchor=CENTER, width=100)
listBox.column('stnk_atas_nama', anchor=CENTER, width=100)
listBox.column('no_rangka', anchor=CENTER, width=100)
listBox.column('no_mesin', anchor=CENTER, width=100)
listBox.column('no_polisi', anchor=CENTER, width=100)
listBox.column('status_pajak', anchor=CENTER, width=100)
listBox.column('berlaku_stnk', anchor=CENTER, width=100)
listBox.column('harga_sewa', anchor=CENTER, width=100)
listBox.column('status', anchor=CENTER, width=100)
	

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan = 2)
    listBox.place(x=10, y=480)
show()
listBox.bind('<Double-Button-1>', getValue)


root.mainloop()