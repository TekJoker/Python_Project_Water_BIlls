from tkinter import *
from tkinter import ttk
import tkcalendar
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import random


master = Tk()
master.title('GRACIOUS APARTMENTS HOUSE ACCOUNTS')
sW = master.winfo_screenwidth()
sH = master.winfo_screenheight()
aW = sW - 200
aH = sH - 100
print(sW)
print(sH)
posx = (sW/2) - (aW/2)
posy = (sH/2) - (aH/2)
master.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
master.configure(background="#cfe0e8")

Lfrm_Gracious = LabelFrame(master, relief="groove", bg="#ffcc5c")
Lfrm_Gracious.grid(row=0,column=0, columnspan=5,padx=150,pady=20)
lbl_Introg = Label(Lfrm_Gracious, text="GRACIOUS APARTMENTS", font=("futura",85,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=0, column=3)

Lfrm_OutCacc = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c",padx=40,pady=40)
Lfrm_OutCacc.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
frm_MidC = Frame(Lfrm_OutCacc, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC.grid(row=1, column=0)
Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC.grid(row=0, column=0,columnspan=2)

Lfrm_OutL1acc = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=40,pady=40)
Lfrm_OutL1acc.grid(row=1, column=0,padx=(15,50), pady=10)
frm_MidL1 = Frame(Lfrm_OutL1acc, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL1.grid(row=1, column=0, padx=60,pady=15)
lbl_pageAd = Label(Lfrm_OutL1acc, text="_Select_ Apartment_", bg="#ffcc5c", fg="#622569", font=("times",18))
lbl_pageAd.grid(row=0, column=0)

class Apartment:
    def __init__(self, hseName, location, num_units, numFloors):
        self.hseName = hseName
        self.location = location
        self.num_units = num_units
        self.numFloors = numFloors



#=================================Page Apartment Details===============================================================
def ApartmentDetails():
    Lfrm_OutCacc.grid_forget()
    Lfrm_OutL1acc.grid_forget()
    Lfrm_OutL2acc.grid_forget()
    frm_Rightacc.grid_forget()

    conn = sqlite3.connect('ProjoZ_SysTest1')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Apartment WHERE House_Name=?",(house.get(),))
    d = cur.fetchall()
    print(d)
    #Apart = d[0]
    House_Name = d[0][0]
    Location = d[0][1]
    Num_Units = d[0][2]
    Floors = d[0][3]
    selectedApt = Apartment(House_Name,Location,Num_Units,Floors)
    conn.commit()
    conn.close()

    Lfrm_OutL1A = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
    Lfrm_OutL1A.grid(row=1, column=0, padx=(15, 5), pady=10)
    frm_MidL1 = Frame(Lfrm_OutL1A, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
    frm_MidL1.grid(row=1, column=0, padx=60, pady=15)
    lbl_pageAdh = Label(Lfrm_OutL1A, text=selectedApt.hseName, bg="#ffcc5c", fg="#622569", font=("times", 25))
    lbl_pageAdh.grid(row=0, column=0)
    lbl_pageAdl = Label(Lfrm_OutL1A, text="City/Town "+selectedApt.location, bg="#ffcc5c", fg="#622569", font=("times", 10))
    lbl_pageAdl.grid(row=1, column=0)
    lbl_pageAdnm = Label(Lfrm_OutL1A, text="No.of Units "+str(selectedApt.num_units), bg="#ffcc5c", fg="#622569", font=("times", 10))
    lbl_pageAdnm.grid(row=2, column=0)
    lbl_pageAdf = Label(Lfrm_OutL1A, text="No.of Floors "+str(selectedApt.numFloors), bg="#ffcc5c", fg="#622569", font=("times", 10))
    lbl_pageAdf.grid(row=3, column=0)

    Lfrm_OutL2A = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
    Lfrm_OutL2A.grid(row=2, column=0, padx=(5, 50), pady=10,rowspan=2)
    frm_MidL2A = Frame(Lfrm_OutL2A, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
    frm_MidL2A.grid(padx=15, pady=15)
    Lfrm_InL2A = LabelFrame(frm_MidL2A, bg="#cfe0e8", padx=15, pady=20)
    Lfrm_InL2A.grid()

    def BackHouse():
        Lfrm_OutL1A.grid_forget()
        Lfrm_OutL2A.grid_forget()
        Lfrm_OutCt.grid_forget()
        Lfrm_OutCb.grid_forget()
        frm_RightA.grid_forget()
        #Lfrm_OutC = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
        Lfrm_OutCacc.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
        #Lfrm_OutL1 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
        Lfrm_OutL1acc.grid(row=1, column=0, padx=(15, 50), pady=10)
        #Lfrm_OutL2 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
        Lfrm_OutL2acc.grid(row=2, column=0, padx=(5, 50), pady=50)
        #frm_Right = Frame(master, bg="#cfe0e8", padx=0, pady=0)
        frm_Rightacc.grid(row=1, column=4, rowspan=2, pady=(20, 10), padx=(20, 20))



    Lfrm_btnL2A = LabelFrame(Lfrm_InL2A, bg="#622569",padx=5,pady=5)
    Lfrm_btnL2A.grid(pady=(0,10))
    btn_InL2a = Button(Lfrm_btnL2A, text="B_A_C_K_ H_o_m_e_", font=("times", 15), bg="#cfe0e8", fg="#622569",
                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                       command=BackHouse)
    btn_InL2a.grid()
    def viewTenants():
        conn = sqlite3.connect('ProjoZ_SysAdminTest1')
        cur = conn.cursor()

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight="25",
                        fieldbackground="#D3D3D3"
                        )
        style.map('Treeview',
                  background=[('selected', 'pink')],
                  foreground=[('selected', 'blue')]
                  )

        frame_treeten = Frame(Lfrm_InR1A, bg="#622569")
        frame_treeten.grid(row=1, column=0)
        tree_ten = ttk.Treeview(frame_treeten)
        tree_ten.grid(row=1, column=0, padx=(5, 0), pady=5, columnspan=3)
        tree_ten['columns'] = ("hseno", "fname", "lname", "idno", "contact", "image")
        tree_ten.column("#0", width=0, stretch=NO)
        tree_ten.column("hseno", width=100)
        tree_ten.column("fname", width=100)
        tree_ten.column("lname", width=100)
        tree_ten.column("idno", width=100)
        tree_ten.column("contact", width=100)

        tree_ten.heading("#0", text="")
        tree_ten.heading("hseno", text="Hse No")
        tree_ten.heading("fname", text="First Name")
        tree_ten.heading("lname", text="Last Name")
        tree_ten.heading("idno", text="ID No")
        tree_ten.heading("contact", text="Contact")
        tree_ten.heading("image", text="Photo Image")

        # Reading from database and inserting on treeview

        cur.execute("SELECT House_No,First_Name, Last_Name, Id_No, Contact FROM Apartment_Tenants WHERE Apart_Name=?",
                    (house.get(),))
        info = cur.fetchall()

        line = 1
        for hseno, fname, lname, idno, contact in info:
            tree_ten.tag_configure('evenrow', background="white")
            tree_ten.tag_configure('oddrow', background="lightblue")
            if line % 2 == 0:
                tree_ten.insert(parent='', index='end', iid=str(line), values=(hseno, fname, lname, idno, contact),
                                tags=('evenrow',))
            else:
                tree_ten.insert(parent='', index='end', iid=str(line), values=(hseno, fname, lname, idno, contact),
                                tags=('oddrow',))
            line += 1

        ys = ttk.Scrollbar(frame_treeten, orient=VERTICAL, command=tree_ten.yview)
        tree_ten["yscrollcommand"] = ys.set
        ys.grid(row=1, column=2, sticky="E", padx=(0, 5))

        frame_edit = LabelFrame(Lfrm_InR1A, padx=30, pady=20)
        frame_edit.grid(row=2, column=0)

        def EditSelected():
            etr_hsNo.delete(0, END)
            etr_fname.delete(0, END)
            etr_lname.delete(0, END)
            etr_id.delete(0, END)
            etr_contact.delete(0, END)
            selected = tree_ten.focus()
            value = tree_ten.item(selected, 'values')
            # val1 = value[0]
            # entry_hse entry_f entry_l entry_id entry_cont
            etr_hsNo.insert(0, value[0])
            etr_fname.insert(0, value[1])
            etr_lname.insert(0, value[2])
            etr_id.insert(0, value[3])
            etr_contact.insert(0, value[4])
            rec_selected = Label(frame_edit, text=value, font=("times", 15), bg="#ffcc5c", fg="#622569",
                                 relief="sunken", borderwidth=2)
            rec_selected.grid(row=2, column=1)

            selected = tree_ten.focus()
            tree_ten.item(selected, text='', values=(etr_hsNo.get(), etr_fname.get(), etr_lname.get(), etr_id.get(), etr_contact.get()))
            

            x = tree_ten.selection()
            for rec in x:
                tree_ten.set(rec)

        def resetField():
            etr_hsNo.delete(0, END)
            etr_fname.delete(0, END)
            etr_lname.delete(0, END)
            etr_id.delete(0, END)
            etr_contact.delete(0, END)
            etr_hsNo.focus()

        def exitTree():
            frame_treeten.grid_forget()
            frame_edit.grid_forget()

        btn_reset = Button(frame_treeten, text="_Reset/Clear_", pady=10, command=resetField, activebackground="#ff6f69",
                           activeforeground="#588c7e",
                           font=("times", 10, "bold"), fg="blue", bg="pink")
        btn_reset.grid(row=3, column=0, pady=10)
        btn_editTree = Button(frame_treeten, text="Click On Record To Edit.", pady=10, command=EditSelected,
                              activebackground="#ff6f69", activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
        btn_editTree.grid(row=3, column=1, pady=10)
        btn_exitTree = Button(frame_treeten, text=" E_X_I_T ", pady=10, command=exitTree, activebackground="#ff6f69",
                              activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
        btn_exitTree.grid(row=3, column=2, pady=10)

        '''def del_save():
            label_confirm.grid_forget()

        label_confirm = Label(Lfrm_InR1A, text="Save Successful!", bg="#ffcc5c", fg="#622569")
        etr_hsNo.delete(0, END)
        etr_fname.delete(0, END)
        etr_lname.delete(0, END)
        etr_id.delete(0, END)
        etr_contact.delete(0, END)
        label_confirm.grid(row=3, column=0)
        label_confirm.after(3000, del_save)'''

        conn.commit()
        conn.close()
    def ViewMeter():
        conn = sqlite3.connect('ProjoZ_SysAdminTest1')
        cur = conn.cursor()
        cur.execute("SELECT Hse_No, Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?", (house.get(),))
        hm = cur.fetchall()
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight="25",
                        fieldbackground="#D3D3D3"
                        )
        style.map('Treeview',
                  background=[('selected', 'pink')],
                  foreground=[('selected', 'blue')]
                  )

        frame_treemtr = Frame(Lfrm_InR2A, bg="#622569")
        frame_treemtr.grid(row=1, column=0)
        treemtr = ttk.Treeview(frame_treemtr)
        treemtr.grid(row=1, column=0, padx=(5, 0), pady=5, columnspan=3)
        treemtr['columns'] = ("hseno", "mtrno")
        treemtr.column("#0", width=0, stretch=NO)
        treemtr.column("hseno", width=100)
        treemtr.column("mtrno", width=100)

        treemtr.heading("#0", text="")
        treemtr.heading("hseno", text="House No")
        treemtr.heading("mtrno", text="Meter No")

        line = 1
        for hsno, mtrno in hm:
            treemtr.tag_configure('evenrow', background="white")
            treemtr.tag_configure('oddrow', background="lightblue")
            if line % 2 == 0:
                treemtr.insert(parent='', index='end', iid=str(line), values=(hsno, mtrno),
                               tags=('evenrow',))
            else:
                treemtr.insert(parent='', index='end', iid=str(line), values=(hsno, mtrno),
                               tags=('oddrow',))
            line += 1

        ys = ttk.Scrollbar(frame_treemtr, orient=VERTICAL, command=treemtr.yview)
        treemtr["yscrollcommand"] = ys.set
        ys.grid(row=1, column=2, sticky="E", padx=(0, 5))

        frame_edit = LabelFrame(Lfrm_InR2A, padx=30, pady=20)
        frame_edit.grid(row=2, column=0)
        conn.commit()
        conn.close()

    Lfrm_btnL2B = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
    Lfrm_btnL2B.grid(pady=(10,10))
    btn_InL2b = Button(Lfrm_btnL2B, text="View "+selectedApt.hseName+" Tenants", font=("times", 15), bg="#cfe0e8", fg="#622569",
                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1, command=viewTenants)
    btn_InL2b.grid()
    Lfrm_btnL2C = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
    Lfrm_btnL2C.grid(pady=(0,10))
    btn_InL2c = Button(Lfrm_btnL2C, text="View Meter Numbers", font=("times", 15), bg="#cfe0e8", fg="#622569",
                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1, command=ViewMeter)
    btn_InL2c.grid()
    Lfrm_btnL2D = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
    Lfrm_btnL2D.grid(pady=(0,10))
    btn_InL2d = Button(Lfrm_btnL2D, text="_V_i_e_w_  _Houses", font=("times", 15), bg="#cfe0e8", fg="#622569",
                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
    btn_InL2d.grid()
    Lfrm_btnL2E = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
    Lfrm_btnL2E.grid(pady=(0,10))
    btn_InL2e = Button(Lfrm_btnL2E, text="_A-g_e_n_t _Report", font=("times", 15), bg="#cfe0e8", fg="#622569",
                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
    btn_InL2e.grid()



    Lfrm_OutCt = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=10)
    Lfrm_OutCt.grid(row=1, column=1, rowspan=2, columnspan=1, padx=(5,10),pady=10)
    frm_MidCt = Frame(Lfrm_OutCt, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
    frm_MidCt.grid(row=1, column=0)
    Lfrm_InCt = LabelFrame(frm_MidCt, bg="#cfe0e8", padx=15, pady=20)
    Lfrm_InCt.grid(row=1, column=0, columnspan=2)

    Lfrm_OutCb = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=10)
    Lfrm_OutCb.grid(row=3, column=1, rowspan=1, columnspan=1, padx=(5,10),pady=10)
    frm_MidCb = Frame(Lfrm_OutCb, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
    frm_MidCb.grid(row=1, column=0)
    Lfrm_InCb = LabelFrame(frm_MidCb, bg="#cfe0e8", padx=15, pady=20)
    Lfrm_InCb.grid(row=1, column=0, columnspan=2)

    frm_RightA = Frame(master, bg="#cfe0e8", padx=0, pady=0)
    frm_RightA.grid(row=1, column=2, rowspan=3, pady=10, padx=(5,10))
    Lfrm_OutR1A = LabelFrame(frm_RightA, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
    Lfrm_OutR1A.grid(row=1, rowspan=2, column=0, padx=0, pady=0)
    frm_MidR1A = Frame(Lfrm_OutR1A, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
    frm_MidR1A.grid(padx=8, pady=8)
    Lfrm_InR1A = LabelFrame(frm_MidR1A, bg="#cfe0e8", padx=15, pady=20)
    Lfrm_InR1A.grid()


    Lfrm_OutR2A = LabelFrame(frm_RightA, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
    Lfrm_OutR2A.grid(row=3, column=0, padx=10, pady=10)
    frm_MidR2A = Frame(Lfrm_OutR2A, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
    frm_MidR2A.grid(padx=8, pady=8)
    Lfrm_InR2A = LabelFrame(frm_MidR2A, bg="#cfe0e8", padx=15, pady=20)
    Lfrm_InR2A.grid()

    lbl_OutCt = Label(Lfrm_OutCt, text="Add Tenant Details To Apartment_", bg="#ffcc5c", fg="#622569", font=("times", 15, "bold"))
    lbl_OutCt.grid(row=0,column=0)

    lbl_hsname = Label(Lfrm_InCt, text="Apartment : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_hsname.grid(row=0, column=0, padx=10, pady=2)
    lbl_hsNo = Label(Lfrm_InCt, text="House No : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_hsNo.grid(row=1, column=0, padx=10, pady=2)
    lbl_fname = Label(Lfrm_InCt, text="First Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_fname.grid(row=2, column=0, padx=10, pady=2)
    lbl_lname = Label(Lfrm_InCt, text="Last Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_lname.grid(row=3, column=0, padx=10, pady=2)
    lbl_id = Label(Lfrm_InCt, text="Id Number : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_id.grid(row=4, column=0, padx=10, pady=2)
    lbl_info = Label(Lfrm_InCt, text="  _Info_  : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_info.grid(row=5, column=0, padx=10, pady=2)
    lbl_contact = Label(Lfrm_InCt, text="Contact : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_contact.grid(row=6, column=0, padx=10, pady=2)

    Hse = StringVar()
    etr_hse = Entry(Lfrm_InCt, textvariable=Hse, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_hse.grid(row=0, column=1, columnspan=2, padx=10, pady=2)
    hsNo = StringVar()
    etr_hsNo = Entry(Lfrm_InCt, textvariable=hsNo, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_hsNo.grid(row=1, column=1, columnspan=2, padx=10, pady=2)
    fname = StringVar()
    etr_fname = Entry(Lfrm_InCt, textvariable=fname, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_fname.grid(row=2, column=1, columnspan=2, padx=10, pady=2)
    lname = StringVar()
    etr_lname = Entry(Lfrm_InCt, textvariable=lname, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_lname.grid(row=3, column=1, columnspan=2, padx=10, pady=2)
    Id = IntVar()
    etr_id = Entry(Lfrm_InCt, textvariable=Id, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_id.grid(row=4, column=1, columnspan=2, padx=10, pady=2)
    info = StringVar()
    radio_phone = Radiobutton(Lfrm_InCt, text="Phone",variable=info, value="Phone",bg="#c1946a", fg="#622569", font=("times", 10, "bold"))
    radio_phone.grid(row=5, column=1, columnspan=2, padx=10, pady=2)
    radio_email = Radiobutton(Lfrm_InCt, text="Email", variable=info, value="Email", bg="#c1946a", fg="#622569", font=("times", 10, "bold"))
    radio_email.grid(row=5, column=2, columnspan=2, padx=10, pady=2)
    contact = StringVar()
    etr_contact = Entry(Lfrm_InCt, textvariable=contact, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_contact.grid(row=6, column=1, columnspan=2, padx=10, pady=2)

    etr_hse.delete(0,END)
    etr_hse.insert(END,house.get())
    etr_hse.configure(state=DISABLED)

    def AddTenant():
        if hsNo.get() == '':
            messagebox.showerror('No Entry', 'House No must be filled')
        elif etr_fname.get() == '':
            etr_fname.insert(END,'xxxx')
        elif etr_lname.get() == '':
            etr_lname.insert(END,'xxxx')
        elif etr_id.get() == '':
            etr_id.insert(END,'xxxx')
        elif etr_contact.get() == '':
            etr_contact.insert(END,'xxxx@xxx.com')

        else:
            '''file_op = open("tenants_info.txt", "a")
            file_op.write(entry_hse.get() + '|' + entry_f.get() + '|' + entry_l.get() + '|' + str(
                entry_id.get()) + '|' + entry_cont.get() + '\n')
            file_op.close()'''
            # save to database
            conn = sqlite3.connect('ProjoZ_SysAdminTest1')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Apartment_Tenants
                        (Apart_Name text,
                        House_No text,
                        First_Name text,
                        Last_Name text,
                        Id_No integer,
                        Contact text)               
                        """)
            cur.execute("INSERT INTO Apartment_Tenants(Apart_Name,House_No,First_Name,Last_Name,Id_No,Contact) VALUES(?,?,?,?,?,?)",
                        (Hse.get(),hsNo.get(),etr_fname.get(),etr_lname.get(),etr_id.get(),etr_contact.get()))
            c = cur.fetchall()

            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview",
                            background="#D3D3D3",
                            foreground="black",
                            rowheight="25",
                            fieldbackground="#D3D3D3"
                            )
            style.map('Treeview',
                      background=[('selected', 'pink')],
                      foreground=[('selected', 'blue')]
                      )

            frame_treeten = Frame(Lfrm_InR1A, bg="#622569")
            frame_treeten.grid(row=1,column=0)
            tree_ten = ttk.Treeview(frame_treeten)
            tree_ten.grid(row=1, column=0, padx=(5,0),pady=5, columnspan=3)
            tree_ten['columns'] = ("hseno", "fname", "lname", "idno", "contact", "image")
            tree_ten.column("#0", width=0, stretch=NO)
            tree_ten.column("hseno", width=100)
            tree_ten.column("fname", width=100)
            tree_ten.column("lname", width=100)
            tree_ten.column("idno", width=100)
            tree_ten.column("contact", width=100)

            tree_ten.heading("#0", text="")
            tree_ten.heading("hseno", text="Hse No")
            tree_ten.heading("fname", text="First Name")
            tree_ten.heading("lname", text="Last Name")
            tree_ten.heading("idno", text="ID No")
            tree_ten.heading("contact", text="Contact")
            tree_ten.heading("image", text="Photo Image")

            # Reading from database and inserting on treeview

            cur.execute("SELECT House_No,First_Name, Last_Name, Id_No, Contact FROM Apartment_Tenants WHERE Apart_Name=?",(house.get(),))
            info = cur.fetchall()

            line = 1
            for hseno, fname, lname, idno, contact in info:
                tree_ten.tag_configure('evenrow', background="white")
                tree_ten.tag_configure('oddrow', background="lightblue")
                if line % 2 == 0:
                    tree_ten.insert(parent='', index='end', iid=str(line), values=(hseno, fname, lname, idno, contact), tags=('evenrow',))
                else:
                    tree_ten.insert(parent='', index='end', iid=str(line), values=(hseno, fname, lname, idno, contact), tags=('oddrow',))
                line += 1

            ys = ttk.Scrollbar(frame_treeten, orient=VERTICAL, command=tree_ten.yview)
            tree_ten["yscrollcommand"] = ys.set
            ys.grid(row=1, column=2, sticky="E", padx=(0,5))

            frame_edit = LabelFrame(Lfrm_InR1A, padx=30, pady=20)
            frame_edit.grid(row=2, column=0)

            def EditSelected():
                etr_hsNo.delete(0,END)
                etr_fname.delete(0, END)
                etr_lname.delete(0, END)
                etr_id.delete(0, END)
                etr_contact.delete(0, END)
                selected = tree_ten.focus()
                value = tree_ten.item(selected, 'values')
                #val1 = value[0]
                # entry_hse entry_f entry_l entry_id entry_cont
                etr_hsNo.insert(0, value[0])
                etr_fname.insert(0, value[1])
                etr_lname.insert(0, value[2])
                etr_id.insert(0, value[3])
                etr_contact.insert(0, value[4])
                rec_selected = Label(frame_edit, text=value, font=("times",15), bg="#ffcc5c", fg="#622569", relief="sunken",borderwidth=2)
                rec_selected.grid(row=2, column=1)

                selected = tree_ten.focus()
                tree_ten.item(selected, text='', values=(etr_hsNo.get(), etr_fname.get(), etr_lname.get(), etr_id.get(), etr_contact.get()))

                x = tree_ten.selection()
                for rec in x:
                    tree_ten.set(rec)
            def resetField():
                etr_hsNo.delete(0, END)
                etr_fname.delete(0, END)
                etr_lname.delete(0, END)
                etr_id.delete(0, END)
                etr_contact.delete(0, END)
                etr_hsNo.focus()

            def exitTree():
                frame_treeten.grid_forget()
                frame_edit.grid_forget()


            btn_reset = Button(frame_treeten, text="_Reset/Clear_", pady=10, command=resetField, activebackground="#ff6f69",activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
            btn_reset.grid(row=3, column=0, pady=10)
            btn_editTree = Button(frame_treeten, text="Click On Record To Edit.", pady=10,command=EditSelected, activebackground="#ff6f69",activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
            btn_editTree.grid(row=3, column=1, pady=10)
            btn_exitTree = Button(frame_treeten, text=" E_X_I_T ", pady=10, command=exitTree, activebackground="#ff6f69",activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
            btn_exitTree.grid(row=3, column=2, pady=10)
            def del_save():
                label_confirm.grid_forget()


            label_confirm = Label(Lfrm_InR1A, text="Save Successful!", bg="#ffcc5c", fg="#622569")
            etr_hsNo.delete(0, END)
            etr_fname.delete(0, END)
            etr_lname.delete(0, END)
            etr_id.delete(0, END)
            etr_contact.delete(0, END)
            label_confirm.grid(row=3, column=0)
            label_confirm.after(3000, del_save)

            conn.commit()
            conn.close()

    '''btn_upload = Button(frame_tentry, text="Save Details", bg="yellow", fg="blue", activebackground="green",
                        activeforeground="yellow", command=save_details, justify="center")
    btn_upload.grid(row=9, column=1, pady=(5, 15))'''
    def ExitTenant():
        lbl_hsname.grid_forget()
        lbl_hsNo.grid_forget()
        lbl_fname.grid_forget()
        lbl_lname.grid_forget()
        lbl_id.grid_forget()
        lbl_info.grid_forget()
        lbl_contact.grid_forget()
        etr_hse.grid_forget()
        etr_hsNo.grid_forget()
        etr_fname.grid_forget()
        etr_lname.grid_forget()
        etr_id.grid_forget()
        radio_phone.grid_forget()
        radio_email.grid_forget()
        etr_contact.grid_forget()
        btn_addtenant.grid_forget()
        btn_exitenant.grid_forget()
        lbl_OutCt.grid_forget()

    btn_addtenant = Button(frm_MidCt,text="Add Tenant", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 15, "bold"),
                           command=AddTenant)
    btn_addtenant.grid(row=2,column=0)
    btn_exitenant = Button(frm_MidCt, text=" _E_X_I_T_ ", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"),
                           command=ExitTenant)
    btn_exitenant.grid(row=2, column=1)

    lbl_OutCb = Label(Lfrm_OutCb, text="Add/Update Water Meter_", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_OutCb.grid(row=0, column=0)

    lbl_hsmNo = Label(Lfrm_InCb, text="House No : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_hsmNo.grid(row=0, column=0, padx=10, pady=2)
    lbl_meter = Label(Lfrm_InCb, text="Meter No_ : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_meter.grid(row=1, column=0, padx=10, pady=2)

    def ExitMtr():
        lbl_OutCb.grid_forget()
        lbl_hsmNo.grid_forget()
        lbl_meter.grid_forget()
        opt_hseNo.grid_forget()
        etr_meter.grid_forget()
        btn_meter.grid_forget()
        btn_exitmtr.grid_forget()

    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
    cur = conn.cursor()
    cur.execute("SELECT House_No FROM Apartment_Tenants WHERE Apart_Name=?",(house.get(),))
    c = cur.fetchall()
    #print(c)
    unitsInApt = []
    for units in c:
        unitsInApt.append(units)

    hseNo = StringVar()
    opt_hseNo = OptionMenu(Lfrm_InCb, hseNo,*unitsInApt)
    opt_hseNo.grid(row=0, column=1, columnspan=2, padx=10, pady=2)
    meter = StringVar()
    etr_meter = Entry(Lfrm_InCb, textvariable=meter, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_meter.grid(row=1, column=1, columnspan=2, padx=10, pady=2)
    conn.commit()
    conn.close()

    def SaveMeter():
        if hseNo.get()=='' or meter.get()=='':
            messagebox.showerror('Empty Field','Must Select House No. And Fill In Meter No To Save!')


        else:
            conn = sqlite3.connect('ProjoZ_SysAdminTest1')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Apartment_MeterNo
                        (Apart_Name text,
                         Hse_No text,
                         Meter_No text)
                        """)
            cur. execute("SELECT Apart_Name,Hse_No FROM Apartment_MeterNo WHERE Apart_Name=? AND Hse_No=?",(house.get(),hseNo.get()))
            h = cur.fetchall()
            cur.execute("SELECT Hse_No,Meter_No FROM Apartment_MeterNo WHERE Meter_No=? AND Apart_Name=?",(meter.get(),house.get()))
            m = cur.fetchall()
            if h:
                que = messagebox.askyesno('Meter Record Already Exists For This House!','Would You Like To Edit Meter No. For This House?')
                if que > 0:
                    cur.execute("UPDATE Apartment_MeterNo SET Meter_No=? WHERE Hse_No=?",(meter.get(),hseNo.get()))
                    print('Updated Successfully')
                    hseNo.set('')
                    etr_meter.delete(0,END)

                    def lbl_suxUpMeterOut():
                        lbl_suxUpMeter.grid_forget()

                    lbl_suxUpMeter = Label(Lfrm_OutCb,
                                         text=str(meter.get()) + " For " + str(hseNo.get()) + " Updated Successfully.",
                                         font=("times", 10), bg="#ffcc5c", fg="#622569")
                    lbl_suxUpMeter.grid(row=2, column=0)
                    lbl_suxUpMeter.after(3000, lbl_suxUpMeterOut)
                else:
                    print('Meter No. Not Updated')
                    def lbl_suxNMeterOut():
                        lbl_suxNMeter.grid_forget()

                    lbl_suxNMeter = Label(Lfrm_OutCb,text=str(meter.get()) + " For " + str(hseNo.get()) + " Not Updated.",
                                         font=("times", 10), bg="#ffcc5c", fg="#622569")
                    lbl_suxNMeter.grid(row=2, column=0)
                    lbl_suxNMeter.after(3000, lbl_suxNMeterOut)
            elif m:
                messagebox.showerror('Meter No Already Exists In This Apartment!','Cannot Save This Meter No For This House')
            else:
                cur.execute("INSERT INTO Apartment_MeterNo VALUES(?,?,?)", (house.get(), hseNo.get(), meter.get()))
                print('House Meter No Added Successfully')
                hseNo.set('')
                etr_meter.delete(0, END)
                def lbl_suxMeterOut():
                    lbl_suxMeter.grid_forget()

                lbl_suxMeter = Label(Lfrm_OutCb, text=str(meter.get())+" For "+str(hseNo.get())+" Added Successfully.",font=("times", 10), bg="#ffcc5c", fg="#622569")
                lbl_suxMeter.grid(row=2,column=0)
                lbl_suxMeter.after(3000,lbl_suxMeterOut)
            conn.commit()
            conn.close()


    btn_meter = Button(frm_MidCb, text="Save Meter", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"),
                       command=SaveMeter)
    btn_meter.grid(row=2, column=0)
    btn_exitmtr = Button(frm_MidCb, text=" _E_X_I_T_ ", background="#588c7e", fg="#ff6f69",activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"),
                           command=ExitMtr)
    btn_exitmtr.grid(row=2, column=1)






#================================End Of Apartment Details==============================================================



def hseLogin():
    if house.get()=='':
        messagebox.showerror('Apartment Not Selected','You Must Select Apartment')
    else:
        lbl_OutC = Label(Lfrm_OutCacc, text="Admin/User Log In", font=("times", 15, "bold"), bg="#ffcc5c", fg="#622569")
        lbl_OutC.grid(row=0, column=0)
        lbl_hsName = Label(Lfrm_InC, text="_User_Id_ : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_hsName.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        lbl_pass = Label(Lfrm_InC,    text="_Password_: ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_pass.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        User_Name = StringVar()
        etr_name = Entry(Lfrm_InC, textvariable=User_Name, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_name.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
        password = StringVar()
        etr_password = Entry(Lfrm_InC, textvariable=password, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_password.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

        def Validate():
            if User_Name.get() == '' or password.get() == '':
                messagebox.showerror('Empty Fields', 'User Id and Password Must Be Filled')
            else:
                conn = sqlite3.connect('ProjoZ_SysTest1')
                cur = conn.cursor()
                cur.execute("SELECT * FROM System_UserTest1")
                a = cur.fetchall()
                print(a)
                cur.execute("SELECT * FROM System_UserTest1 WHERE User_Id=? AND Pass_Word=?", (User_Name.get(), password.get()))
                c = cur.fetchall()
                if c:
                    etr_name.delete(0, END)
                    etr_password.delete(0, END)
                    etr_name.focus()
                    print('Log In Successful')
                    print(house.get())
                    ApartmentDetails()
                else:
                    print('Log In Failed!!')

                conn.commit()
                conn.close()

        def ExitLog():
            lbl_OutC.grid_forget()
            lbl_pass.grid_forget()
            lbl_hsName.grid_forget()
            etr_password.grid_forget()
            etr_name.grid_forget()
            btn_Login.grid_forget()
            btn_exitLog.grid_forget()
            opt_select.configure(house.set(''))


        btn_Login = Button(frm_MidC, text="Log In", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"), command=Validate)
        btn_Login.grid(row=1, column=0, pady=5)
        btn_exitLog = Button(frm_MidC, text="E_X_I_T", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"), command=ExitLog)
        btn_exitLog.grid(row=1, column=1, pady=5)

conn = sqlite3.connect('ProjoZ_SysTest1')
cur = conn.cursor()
cur. execute("SELECT * FROM Apartment")
c = cur.fetchall()
AptName = []
#print(c[0])
#print(c[1])
#count = 1
for name,location,units,floors in c:
    AptName.append(name)
house = StringVar()
opt_select = OptionMenu(frm_MidL1, house, *AptName)
opt_select.grid(row=1, column=0, padx=20,pady=(5,10))
btn_select = Button(Lfrm_OutL1acc,text="Select Apartment", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                    command=hseLogin)
btn_select.grid(row=2,column=0)
conn.commit()
conn.close()

def BackHome():
    pass

Lfrm_OutL2acc = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutL2acc.grid(row=2, column=0,padx=(5,50),pady=50)
frm_MidL2 = Frame(Lfrm_OutL2acc, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL2.grid(padx=15,pady=15)
Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InL2.grid()

btn_InL2a = Button(Lfrm_InL2,text="_H_o_m_e_ _P_a_g_e", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                   command=BackHome)
btn_InL2a.grid(padx=10, pady=10)
btn_InL2b = Button(Lfrm_InL2,text="_C_a_r_e_t_a_k_e_r", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2b.grid(padx=10, pady=10)
btn_InL2c = Button(Lfrm_InL2,text="_U_p_l_o_a_d_Image", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2c.grid(padx=10, pady=10)
btn_InL2d = Button(Lfrm_InL2,text="_V_i_e_w_  _Houses", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2d.grid(padx=10, pady=10)
btn_InL2e = Button(Lfrm_InL2,text="_A-g_e_n_t _Report", font=("times",15), bg="#cfe0e8", fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2e.grid(padx=10, pady=10)


frm_Rightacc = Frame(master,bg="#cfe0e8", padx=0, pady=0)
frm_Rightacc.grid(row=1, column=4, rowspan=2, pady=(20,10), padx=(20,20))
Lfrm_OutR1 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR1.grid(row=1, column=0,padx=(50,0),pady=(20,10))
frm_MidR1 = Frame(Lfrm_OutR1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR1.grid(padx=8,pady=8)
Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR1.grid()
btn_InR1 = Button(Lfrm_InR1,text="To Do List", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR1.grid(padx=10, pady=10)

Lfrm_OutR2 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR2.grid(row=2, column=0,padx=(50,0),pady=(20,10))
frm_MidR2 = Frame(Lfrm_OutR2, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR2.grid(padx=8,pady=8)
Lfrm_InR2 = LabelFrame(frm_MidR2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR2.grid()
btn_InR2 = Button(Lfrm_InR2,text="Set Reminder", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR2.grid(padx=10, pady=10)

Lfrm_OutR3 = LabelFrame(frm_Rightacc,relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR3.grid(row=3, column=0,padx=(50,0),pady=(20,10))
frm_MidR3 = Frame(Lfrm_OutR3, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR3.grid(padx=8,pady=8)
Lfrm_InR3 = LabelFrame(frm_MidR3, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR3.grid()
btn_InR3 = Button(Lfrm_InR3,text="Sticky Note", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR3.grid(padx=10, pady=10)

Lfrm_OutR4 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR4.grid(row=4, column=0,padx=(50,0),pady=(20,10))
frm_MidR4 = Frame(Lfrm_OutR4, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR4.grid(padx=8,pady=8)
Lfrm_InR4 = LabelFrame(frm_MidR4, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR4.grid()
btn_InR4 = Button(Lfrm_InR4,text="Tenant Box", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR4.grid(padx=10, pady=10)

mainloop()