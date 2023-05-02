import tkinter
from tkinter import *
from tkinter import ttk
import tkcalendar
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import random


master = Tk()
master.title('GRACIOUS APARTMENTS ADMINISTRATOR')
sW = master.winfo_screenwidth()
sH = master.winfo_screenheight()
aW = sW - 200
aH = sH - 100
posx = (sW/2) - (aW/2)
posy = (sH/2) - (aH/2)
master.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
master.configure(background="#cfe0e8")

Lfrm_Gracious = LabelFrame(master, relief="groove", bg="#ffcc5c")
Lfrm_Gracious.grid(row=0,column=0, columnspan=5,padx=150,pady=20)
lbl_Introg = Label(Lfrm_Gracious, text="GRACIOUS APARTMENTS", font=("futura",85,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=0, column=3)

Lfrm_OutC = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c",padx=40,pady=40)
Lfrm_OutC.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
frm_MidC = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC.grid(row=1, column=0)
Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC.grid(row=0, column=0,columnspan=2)

Lfrm_OutC1 = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
Lfrm_OutC1.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
frm_MidC1 = Frame(Lfrm_OutC1, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
frm_MidC1.grid(row=1, column=0)
Lfrm_InC1 = LabelFrame(frm_MidC1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC1.grid(row=0, column=0, columnspan=2)

'''frm_MidC2 = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC2.grid(row=1, column=0)
Lfrm_InC2 = LabelFrame(frm_MidC2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC2.grid(row=0, column=0,columnspan=2)

frm_MidC3 = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC3.grid(row=0, column=0)
Lfrm_InC3 = LabelFrame(frm_MidC3, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC3.grid(row=0, column=0,columnspan=2)'''

Lfrm_OutC4 = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
Lfrm_OutC4.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
frm_MidC4 = Frame(Lfrm_OutC4, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC4.grid(row=1, column=0)
Lfrm_InC4 = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC4.grid(row=1, column=0,columnspan=2)

def createNewApartment():
    class Apartment:
        def __init__(self, hseName, location, numFloors):
            self.hseName = hseName
            self.location = location
            self.numFloors = numFloors
    Lfrm_OutC1.grid_forget()
    Lfrm_OutC4.grid_forget()
    Lfrm_OutC.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)

    lbl_OutC = Label(Lfrm_OutC,text="Create New Apartment", font=("times", 15, "bold"), bg="#ffcc5c", fg="#622569")
    lbl_OutC.grid(row=0,column=0)
    lbl_hsName = Label(Lfrm_InC, text="_House_Name_ : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_hsName.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
    lbl_loc = Label(Lfrm_InC, text="Location/City : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_loc.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
    lbl_units = Label(Lfrm_InC, text="Number_Of_Units: ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_units.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
    lbl_flrs = Label(Lfrm_InC, text="No_of_Floo_rs : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_flrs.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    Hse_Name = StringVar()
    etr_Hse = Entry(Lfrm_InC, textvariable=Hse_Name, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_Hse.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
    City = StringVar()
    etr_City = Entry(Lfrm_InC, textvariable=City, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_City.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
    NumUnits = IntVar()
    etr_Units = Entry(Lfrm_InC, textvariable=NumUnits, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_Units.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
    etr_Units.delete(0, END)
    Floors = IntVar()
    etr_Flrs = Entry(Lfrm_InC, textvariable=Floors, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_Flrs.grid(row=3, column=2, columnspan=2, padx=10, pady=20)
    etr_Flrs.delete(0,END)


    def saveApt():
        def saveLblout():
            lbl_sux.grid_forget()
            #btn_saveApt.grid_forget()
            etr_Hse.focus()

            
        try:
            if Hse_Name.get() =='' or City.get() =='' or NumUnits.get()==0 or Floors.get() ==0:
                messagebox.showerror('Empty Field','Fill In All Fields To Continue')
            else:
                '''file = open('apartments.txt', 'a')
                file.write(Hse_Name.get()+'-'+City.get()+'-'+str(Floors.get())+'\n')
                lbl_sux = Label(Lfrm_OutC, text= Hse_Name.get()+" Apartment Created Successfully", font=('times',10,'bold'), fg="yellow", bg="green")
                lbl_sux.grid(row=1,column=0)
                etr_Hse.delete(0,END)
                etr_City.delete(0,END)
                etr_Flrs.delete(0,END)
                lbl_sux.after(3000,saveLblout)

                fop = open('apartments.txt', 'r')
                line = 1
                for house in fop:
                    hsname, city, flrs = house.split('-')
                    apt= Apartment(hsname,city,flrs)
                    print(apt.hseName)
                    #print(Apartment.numOfUnits)
                    line += 1
                file.close()
                fop.close()'''
                conn  = sqlite3.connect('ProjoZ_SysTest1')
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS Apartment
                            (House_Name VARCAHAR NOT NULL,
                             Location VARCHAR NOT NULL,
                             Num_Units INTEGER NOT NULL,
                             Floors INTEGER NOT NULL)
                            """)
                cur.execute("INSERT INTO Apartment(House_Name,Location,Num_Units,Floors) VALUES(?,?,?,?)",(Hse_Name.get(),City.get(),NumUnits.get(),Floors.get()))
                conn.commit()
                conn.close()
                lbl_sux = Label(Lfrm_OutC, text=Hse_Name.get() + "Apartment Created Successfully",font=("times", 10), bg="#ffcc5c", fg="#622569")
                lbl_sux.grid(row=2, column=0)
                etr_Hse.delete(0, END)
                etr_City.delete(0, END)
                etr_Units.delete(0,END)
                etr_Flrs.delete(0, END)
                lbl_sux.after(3000, saveLblout)
        except:
            messagebox.showerror('Empty Field','Fill In Units and Floors And Must Be Numeric')

    def ExitApt():
        lbl_OutC.grid_forget()
        lbl_hsName.grid_forget()
        lbl_loc.grid_forget()
        lbl_units.grid_forget()
        lbl_flrs.grid_forget()
        etr_Hse.grid_forget()
        etr_City.grid_forget()
        etr_Units.grid_forget()
        etr_Flrs.grid_forget()
        btn_saveApt.grid_forget()
        btn_exitApt.grid_forget()

    btn_saveApt = Button(frm_MidC,text="Create New Apartment", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69", activeforeground="#588c7e", font=("arial",15,"bold"),
                         relief="raised", borderwidth=1, command=saveApt)
    btn_saveApt.grid(row=1, column=0, pady=5)
    btn_exitApt = Button(frm_MidC, text="E_X_I_T", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=ExitApt)
    btn_exitApt.grid(row=1, column=1, pady=5)

def addNewUser():
    class User:
        def __init__(self, userID, fname, lname, password):
            self.userID = userID
            self.fname = fname
            self.lname = lname
            self.password = password

    Lfrm_OutC.grid_forget()
    Lfrm_OutC4.grid_forget()
    Lfrm_OutC1.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)

    lbl_OutC1 = Label(Lfrm_OutC1, text="Add New User", font=("times", 15, "bold"), bg="#ffcc5c", fg="#622569")
    lbl_OutC1.grid(row=0, column=0, pady=5)
    lbl_userID = Label(Lfrm_InC1, text="_User_I_D : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_userID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
    lbl_fname = Label(Lfrm_InC1, text="First Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_fname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
    lbl_lname = Label(Lfrm_InC1, text="Last_Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_lname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
    lbl_password = Label(Lfrm_InC1, text="Password : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
    lbl_password.grid(row=3, column=0, columnspan=2, padx=10, pady=20)


    UserID = StringVar()
    etr_usID = Entry(Lfrm_InC1, textvariable=UserID, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_usID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
    firstName = StringVar()
    etr_fname = Entry(Lfrm_InC1, textvariable=firstName, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_fname.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
    lastName = StringVar()
    etr_lname = Entry(Lfrm_InC1, textvariable=lastName, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
    etr_lname.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
    passWord = StringVar()
    etr_psWord = Entry(Lfrm_InC1, textvariable=passWord, bg="#c1946a", fg="#622569", font=("times", 20, "bold"), show="*")
    etr_psWord.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

    def addUser():
        if etr_usID == ''or etr_fname=='' or etr_lname.get()=='' or etr_psWord.get() == '':
            messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
        else:
            conn = sqlite3.connect('ProjoZ_SysTest1')
            cur = conn.cursor()
            cur.execute("""CREATE  TABLE IF NOT EXISTS System_UserTest1
                            (User_Id VARCHAR,
                             First_Name VARCHAR,
                             Last_Name VARCHAR,
                             Pass_Word VARCHAR)
                             """)
            cur.execute("INSERT INTO System_UserTest1(User_Id, First_Name, Last_Name, Pass_Word) VALUES(?,?,?,?)",(UserID.get(),firstName.get(),lastName.get(),passWord.get()))
            conn.commit()
            conn.close()
            def suxMesOut():
                lbl_suxMes.grid_forget()

            etr_fname.delete(0,END)
            etr_lname.delete(0,END)
            etr_usID.delete(0,END)
            etr_psWord.delete(0,END)
            lbl_suxMes = Label(Lfrm_OutC1,text='Successfully Added To Database '+ etr_usID.get(), font=("times", 10), bg="#ffcc5c", fg="#cfe0e8")
            lbl_suxMes.grid(row=2,column=0)
            lbl_suxMes.after(3000,suxMesOut)
    def exitUse():
        lbl_OutC1.grid_forget()
        lbl_password.grid_forget()
        lbl_userID.grid_forget()
        lbl_fname.grid_forget()
        lbl_lname.grid_forget()
        etr_lname.grid_forget()
        etr_fname.grid_forget()
        etr_usID.grid_forget()
        etr_psWord.grid_forget()
        btn_addUser.grid_forget()
        btn_exitUse.grid_forget()

    btn_addUser = Button(frm_MidC1, text="Add New User", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=addUser)
    btn_addUser.grid(row=1, column=0, pady=5)
    btn_exitUse = Button(frm_MidC1, text="E_X_I_T", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=exitUse)
    btn_exitUse.grid(row=1, column=1, pady=5)

def Office():
    Lfrm_OutC.grid_forget()
    Lfrm_OutC1.grid_forget()
    Lfrm_OutC4.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)


    lbl_OutC4 = Label(Lfrm_OutC4, text="Update System Profile", font=("times", 20, "bold"), bg="#ffcc5c", fg="#622569")
    lbl_OutC4.grid(row=0, column=0)

    def UpAdmin():
        Lfrm_UpAdmin.grid_forget()
        Lfrm_UpUser.grid_forget()
        Lfrm_RemUser.grid_forget()
        Lfrm_RemApt.grid_forget()
        Lfrm_bg.grid_forget()
        Lfrm_InC4.grid_forget()
        btn_InL2a['state']= DISABLED
        btn_InL2b['state'] = DISABLED
        btn_InL2c['state'] = DISABLED
        btn_InL2d['state'] = DISABLED
        btn_InL2e['state'] = DISABLED
        Lfrm_InC4i = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
        Lfrm_InC4i.grid(row=1, column=0, columnspan=2)
        #====================================================================================
        Lfrm_UpAdminT = LabelFrame(Lfrm_InC4i, bg="#622569", padx=5, pady=5)
        Lfrm_UpAdminT.grid(row=0, column=0, padx=20, pady=10)
        conn = sqlite3.connect('ProjoZ_SysAdminTest1')
        cur = conn.cursor()
        cur.execute("SELECT Admin_Name,First_Name,Last_Name FROM System_AdminTest1")
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

        tree_admin = ttk.Treeview(Lfrm_UpAdminT)
        tree_admin.grid()
        tree_admin['columns'] = ("userId", "fname", "lname")
        tree_admin.column('#0', stretch=NO, width=0)
        tree_admin.column('userId', anchor=CENTER, width=120)
        tree_admin.column('fname', anchor=CENTER, width=120)
        tree_admin.column('lname', anchor=CENTER, width=120)

        tree_admin.heading('#0', text='')
        tree_admin.heading('userId', text="User Id")
        tree_admin.heading('fname', text="First Name")
        tree_admin.heading('lname', text="Last Name")

        i = 1
        for id, fname, lname in c:
            tree_admin.tag_configure('evenrow', background="white")
            tree_admin.tag_configure('oddrow', background="lightblue")
            if i % 2 == 0:
                tree_admin.insert(parent='', index='end', iid=str(i), values=(id, fname, lname), tags=('evenrow',))
            else:
                tree_admin.insert(parent='', index='end', iid=str(i), values=(id, fname, lname), tags=('oddrow',))
            i += 1
        conn.commit()
        conn.close()
        ys = ttk.Scrollbar(Lfrm_UpAdminT, orient=VERTICAL, command=tree_admin.yview)
        tree_admin["yscrollcommand"] = ys.set
        ys.grid(row=0, column=1, sticky="E")

        def EditAdmin():
            selUser = tree_admin.focus()
            userDetails = tree_admin.item(selUser, 'values')
            userId = userDetails[0]
            userf = userDetails[1]
            userl = userDetails[2]

            etr_adID.insert(0, userId)
            etr_afname.insert(0, userf)
            etr_alname.insert(0, userl)
            btn_editAdmin.grid_forget()

            def Edit():
                if etr_adID == '' or etr_afname == '' or etr_alname.get() == '' or etr_apsWord.get() == '':
                    messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                else:
                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                    cur = conn.cursor()
                    vTop = Toplevel()
                    vTop.title('Confirm You Are Admin')
                    vTop.geometry('500x350')
                    vTop.configure(bg="#ffcc5c")
                    Lfrm_top = LabelFrame(vTop, bg="#622569")
                    Lfrm_top.grid(row=1, column=0, padx=20, pady=20)
                    lbl_Aname = Label(Lfrm_top, text="Admin Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_Aname.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                    lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                          font=("times", 15, "bold"))
                    lbl_Apassword.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                    AdmnID = StringVar()
                    etr_AdmnID = Entry(Lfrm_top, textvariable=AdmnID, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"))
                    etr_AdmnID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                    AdmnPass = StringVar()
                    etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569", show="*",
                                   font=("times", 20, "bold"))
                    etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

                    def UPDATEADMIN():
                        if AdmnID.get() == '' or AdmnPass.get() == '':
                            messagebox.showerror('Empty Field', 'You Must Enter Name and Password')
                        else:
                            # cur.execute("SELECT * FROM System_AdminTest1")
                            # e = cur.fetchall()
                            # print(e)
                            cur.execute(
                                "SELECT Admin_Name,Pass_Word FROM System_AdminTest1 WHERE Admin_Name=? AND Pass_Word=?",
                                (AdmnID.get(), AdmnPass.get()))
                            c = cur.fetchall()

                            if c:
                                cur.execute(
                                    "UPDATE System_AdminTest1 SET Admin_Name=?, First_Name=?, Last_Name=?, Pass_Word=? WHERE Admin_Name=?",
                                    ((AdminID.get(), AfirstName.get(), AlastName.get(), ApassWord.get(), AdminID.get())))
                                conn.commit()
                                conn.close()

                                def suxMesOut():
                                    lbl_suxMes.grid_forget()
                                    vTop.destroy()
                                    etr_adID.focus()

                                
                                selected = tree_admin.focus()
                                tree_admin.item(selected, text='',values=(etr_adID.get(), etr_afname.get(), etr_alname.get()))
                                lbl_suxMes = Label(vTop, text=etr_adID.get() + ' Successfully Added To Database',
                                                   font=("times", 10), bg="#ffcc5c", fg="#622569")
                                etr_afname.delete(0, END)
                                etr_alname.delete(0, END)
                                etr_adID.delete(0, END)
                                etr_apsWord.delete(0, END)
                                etr_adID.focus()
                                lbl_suxMes.grid(row=3, column=0)
                                lbl_suxMes.after(3000, suxMesOut)
                            else:
                                vTop.destroy()
                                messagebox.showerror('Wrong Entry',
                                                     'Wrong Name or Password.\n Cannot Proceed With Admin Update')

                    btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                                      activeforeground="#588c7e", font=("arial", 15, "bold"),
                                      relief="raised", borderwidth=1, command=UPDATEADMIN)
                    btn_vTop.grid(row=2, column=0)

            btn_EDITUSER = Button(Lfrm_UpAdminT, text="Edit User Details", bg="#588c7e", fg="#ff6f69",
                                  activebackground="#ff6f69",
                                  activeforeground="#588c7e", font=("arial", 10, "bold"),
                                  relief="raised", borderwidth=1, command=Edit)
            btn_EDITUSER.grid(row=1, column=0)

        btn_editAdmin = Button(Lfrm_UpAdminT, text="Edit User Details", bg="#588c7e", fg="#ff6f69",
                              activebackground="#ff6f69",
                              activeforeground="#588c7e", font=("arial", 10, "bold"),
                              relief="raised", borderwidth=1, command=EditAdmin)
        btn_editAdmin.grid(row=1, column=0)




        #======================================================================================

        Lfrm_UpAdmin_1 = LabelFrame(Lfrm_InC4i, bg="#622569", padx=5, pady=5)
        Lfrm_UpAdmin_1.grid(row=2, column=0, padx=20, pady=10)
        lbl_MidC4 = Label(frm_MidC4,text=" Update Admin Details",fg="#cfe0e8",bg="#622569",font=("times", 10, "bold"))
        lbl_MidC4.grid(row=0,column=0)

        lbl_AdminID = Label(Lfrm_UpAdmin_1, text="_Admin_I_D : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_AdminID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        lbl_Afname = Label(Lfrm_UpAdmin_1, text="First Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_Afname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        lbl_Alname = Label(Lfrm_UpAdmin_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_Alname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
        lbl_Apassword = Label(Lfrm_UpAdmin_1, text="Password : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_Apassword.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        AdminID = StringVar()
        etr_adID = Entry(Lfrm_UpAdmin_1, textvariable=AdminID, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_adID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
        AfirstName = StringVar()
        etr_afname = Entry(Lfrm_UpAdmin_1, textvariable=AfirstName, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_afname.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
        AlastName = StringVar()
        etr_alname = Entry(Lfrm_UpAdmin_1, textvariable=AlastName, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_alname.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
        ApassWord = StringVar()
        etr_apsWord = Entry(Lfrm_UpAdmin_1, textvariable=ApassWord, bg="#c1946a", fg="#622569", font=("times", 20, "bold"),
                           show="*")
        etr_apsWord.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

        def UpdateAdmin():
            if etr_adID =='' or etr_afname =='' or etr_alname.get() =='' or etr_apsWord.get() == '':
                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
            else:
                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                cur = conn.cursor()
                vTop = Toplevel()
                vTop.title('Confirm You Are Admin')
                vTop.geometry('500x350')
                vTop.configure(bg="#ffcc5c")
                Lfrm_top = LabelFrame(vTop,bg="#622569")
                Lfrm_top.grid(row=1,column=0,padx=20,pady=20)
                lbl_Aname = Label(Lfrm_top, text="Admin Name : ", bg="#ffcc5c", fg="#622569",
                                   font=("times", 15, "bold"))
                lbl_Aname.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                lbl_Apassword.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                AdmnID = StringVar()
                etr_AdmnID = Entry(Lfrm_top, textvariable=AdmnID, bg="#c1946a", fg="#622569",
                                 font=("times", 20, "bold"))
                etr_AdmnID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                AdmnPass = StringVar()
                etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569",show="*",
                                   font=("times", 20, "bold"))
                etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                def UPDATE():
                    if AdmnID.get()=='' or AdmnPass.get()=='':
                        messagebox.showerror('Empty Field','You Must Enter Name and Password')
                    else:
                        cur.execute("SELECT * FROM System_AdminTest1")
                        e = cur.fetchall()
                        print(e)
                        cur.execute("SELECT Admin_Name,Pass_Word FROM System_AdminTest1 WHERE Admin_Name=? AND Pass_word=?",
                                (AdmnID.get(), AdmnPass.get()))
                        c = cur.fetchall()

                        if c:
                            cur.execute("UPDATE System_AdminTest1 SET Admin_Name=?, First_Name=?, Last_Name=?, Pass_Word=? WHERE Admin_Name=?",
                                ((AdminID.get(), AfirstName.get(), AlastName.get(), ApassWord.get(), AdmnID.get())))
                            conn.commit()
                            conn.close()

                            def suxMesOut():
                                lbl_suxMes.grid_forget()
                                vTop.destroy()
                                etr_adID.focus()

                            
                            lbl_suxMes = Label(vTop, text= etr_adID.get()+' Successfully Added To Database',
                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                            etr_afname.delete(0, END)
                            etr_alname.delete(0, END)
                            etr_adID.delete(0, END)
                            etr_apsWord.delete(0, END)
                            lbl_suxMes.grid(row=3, column=0)
                            lbl_suxMes.after(3000, suxMesOut)
                        else:
                            vTop.destroy()
                            messagebox.showerror('Wrong Entry','Wrong Name or Password.\n Cannot Proceed With Admin Update')
                            etr_adID.focus()

                btn_vTop = Button(vTop,text="Confirm",bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=UPDATE)
                btn_vTop.grid(row=2,column=0)



        def BackAdmin():
            Lfrm_InC4i.grid_forget()
            Lfrm_UpAdmin_1.grid_forget()
            lbl_MidC4.grid_forget()
            btn_saveAdmin.grid_forget()
            btn_backAdmin.grid_forget()
            Lfrm_InC4.grid(row=1, column=0, columnspan=2)
            Lfrm_UpAdmin.grid(row=0, column=0, padx=20, pady=10)
            Lfrm_UpUser.grid(row=1, column=0, padx=20, pady=10)
            Lfrm_RemUser.grid(row=2, column=0, padx=20, pady=10)
            Lfrm_RemApt.grid(row=3, column=0, padx=20, pady=10)
            Lfrm_bg.grid(row=4, column=0, padx=20, pady=10)
            btn_InL2a['state'] = NORMAL
            btn_InL2b['state'] = NORMAL
            btn_InL2c['state'] = NORMAL
            btn_InL2d['state'] = NORMAL
            btn_InL2e['state'] = NORMAL

        btn_saveAdmin = Button(frm_MidC4, text="Update Admin",bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 10, "bold",),
                         relief="raised", borderwidth=1, command=UpdateAdmin)
        btn_saveAdmin.grid(row=2,column=0)
        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                               relief="raised", borderwidth=1, command=BackAdmin)
        btn_backAdmin.grid(row=2, column=1)



    Lfrm_UpAdmin = LabelFrame(Lfrm_InC4, bg="#622569", padx=5,pady=5)
    Lfrm_UpAdmin.grid(row=0, column=0,padx=20,pady=10)
    btn_UpAdmin = Button(Lfrm_UpAdmin, text="     _Update_ Admin_ Profile_        ",bg="#cfe0e8",fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",font=("times", 20, "bold"),
                         command=UpAdmin)
    btn_UpAdmin.grid()

    def UpUser():
        Lfrm_UpAdmin.grid_forget()
        Lfrm_UpUser.grid_forget()
        Lfrm_RemUser.grid_forget()
        Lfrm_RemApt.grid_forget()
        Lfrm_bg.grid_forget()
        Lfrm_InC4.grid_forget()
        btn_InL2a['state'] = DISABLED
        btn_InL2b['state'] = DISABLED
        btn_InL2c['state'] = DISABLED
        btn_InL2d['state'] = DISABLED
        btn_InL2e['state'] = DISABLED
        Lfrm_InC4ii = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
        Lfrm_InC4ii.grid(row=1, column=0, columnspan=2)

        Lfrm_UpUserT = LabelFrame(Lfrm_InC4ii, bg="#622569", padx=5, pady=5)
        Lfrm_UpUserT.grid(row=0,column=0, padx=20, pady=(0,10))
        conn = sqlite3.connect('ProjoZ_SysTest1')
        cur = conn.cursor()
        cur.execute("SELECT User_Id,First_Name,Last_Name FROM System_UserTest1")
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

        tree_user = ttk.Treeview(Lfrm_UpUserT)
        tree_user.grid()
        tree_user['columns'] = ("userId", "fname", "lname")
        tree_user.column('#0', stretch=NO, width=0)
        tree_user.column('userId', anchor=CENTER, width=100)
        tree_user.column('fname', anchor=CENTER, width=100)
        tree_user.column('lname', anchor=CENTER, width=100)

        tree_user.heading('#0', text='')
        tree_user.heading('userId', text="User Id")
        tree_user.heading('fname', text="First Name")
        tree_user.heading('lname', text="Last Name")

        i = 1
        for id,fname,lname in c:
            tree_user.tag_configure('evenrow', background="white")
            tree_user.tag_configure('oddrow', background="lightblue")
            if 1 % 2 == 0:
                tree_user.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),tags=('evenrow',))
            else:
                tree_user.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),tags=('oddrow',))
            i += 1
        conn.commit()
        conn.close()
        ys = ttk.Scrollbar(Lfrm_UpUserT, orient=VERTICAL, command=tree_user.yview)
        tree_user["yscrollcommand"] = ys.set
        ys.grid(row=0, column=1, sticky="E")

        def EditUser():
            selUser = tree_user.focus()
            userDetails = tree_user.item(selUser,'values')
            userId = userDetails[0]
            userf = userDetails[1]
            userl = userDetails[2]

            etr_userID.insert(0,userId)
            etr_ufname.insert(0,userf)
            etr_ulname.insert(0,userl)
            btn_editUser.grid_forget()
            def Edit():
                if etr_userID == '' or etr_ufname == '' or etr_ulname.get() == '' or etr_upsWord.get() == '':
                    messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                else:
                    conn = sqlite3.connect('ProjoZ_SysUserTest1')
                    cur = conn.cursor()
                    vTop = Toplevel()
                    vTop.title('Confirm You Are Admin')
                    vTop.geometry('500x350')
                    vTop.configure(bg="#ffcc5c")
                    Lfrm_top = LabelFrame(vTop, bg="#622569")
                    Lfrm_top.grid(row=1, column=0, padx=20, pady=20)
                    lbl_Aname = Label(Lfrm_top, text="Admin Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_Aname.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                    lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                          font=("times", 15, "bold"))
                    lbl_Apassword.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                    AdmnID = StringVar()
                    etr_AdmnID = Entry(Lfrm_top, textvariable=AdmnID, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"))
                    etr_AdmnID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                    AdmnPass = StringVar()
                    etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569", show="*",
                                   font=("times", 20, "bold"))
                    etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

                    def UPDATEUSER():
                        if AdmnID.get() == '' or AdmnPass.get() == '':
                            messagebox.showerror('Empty Field', 'You Must Enter Name and Password')
                        else:
                            conn = sqlite3.connect('ProjoZ_SysUserTest1')
                            cur.execute("SELECT * FROM System_AdminTest1")
                            e = cur.fetchall()
                            print(e)
                            cur.execute(
                                "SELECT User_Id,Pass_Word FROM System_UserTest1 WHERE User_Id=? AND Pass_Word=?",
                                (AdmnID.get(), AdmnPass.get()))
                            c = cur.fetchall()

                            if c:
                                cur.execute(
                                    "UPDATE System_UserTest1 SET User_Id=?, First_Name=?, Last_Name=?, Pass_Word=? WHERE User_Id=?",
                                    ((UserID.get(), UfirstName.get(), UlastName.get(), UpassWord.get(), UserID.get())))
                                conn.commit()
                                conn.close()

                                def suxMesOut():
                                    lbl_suxMes.grid_forget()
                                    vTop.destroy()
                                    etr_userID.focus()

                                selected = tree_user.focus()
                                tree_user.item(selected, text='',values=(etr_userID.get(), etr_ufname.get(), etr_ulname.get()))
                                lbl_suxMes = Label(vTop, text=etr_userID.get() + ' Successfully Added To Database',
                                                   font=("times", 10), bg="#ffcc5c", fg="#622569")
                                etr_ufname.delete(0, END)
                                etr_ulname.delete(0, END)
                                etr_userID.delete(0, END)
                                etr_upsWord.delete(0, END)
                                etr_userID.focus()
                                lbl_suxMes.grid(row=3, column=0)
                                lbl_suxMes.after(3000, suxMesOut)
                            else:
                                vTop.destroy()
                                messagebox.showerror('Wrong Entry',
                                                     'Wrong Name or Password.\n Cannot Proceed With Admin Update')

                    btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                                      activeforeground="#588c7e", font=("arial", 15, "bold"),
                                      relief="raised", borderwidth=1, command=UPDATEUSER)
                    btn_vTop.grid(row=2, column=0)



            btn_EDITUSER = Button(Lfrm_UpUserT, text="Edit User Details", bg="#588c7e", fg="#ff6f69",
                                  activebackground="#ff6f69",
                                  activeforeground="#588c7e", font=("arial", 10, "bold"),
                                  relief="raised", borderwidth=1, command=Edit)
            btn_EDITUSER.grid(row=1, column=0)




        btn_editUser = Button(Lfrm_UpUserT, text="Edit User Details", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                          activeforeground="#588c7e", font=("arial", 10, "bold"),
                          relief="raised", borderwidth=1, command=EditUser)
        btn_editUser.grid(row=1, column=0)



        Lfrm_UpUser_1 = LabelFrame(Lfrm_InC4ii, bg="#622569", padx=5, pady=5)
        Lfrm_UpUser_1.grid(row=2, column=0, padx=20, pady=(0,0))
        lbl_MidC4 = Label(frm_MidC4, text=" Update User Details", fg="#cfe0e8", bg="#622569",
                          font=("times", 10, "bold"))
        lbl_MidC4.grid(row=0, column=0)

        lbl_UserID = Label(Lfrm_UpUser_1, text="_User__I_D : ", bg="#ffcc5c", fg="#622569",
                            font=("times", 10, "bold"))
        lbl_UserID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        lbl_Ufname = Label(Lfrm_UpUser_1, text="First Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_Ufname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        lbl_Ulname = Label(Lfrm_UpUser_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_Ulname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
        lbl_Upassword = Label(Lfrm_UpUser_1, text="Password : ", bg="#ffcc5c", fg="#622569",
                              font=("times", 10, "bold"))
        lbl_Upassword.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

        UserID = StringVar()
        etr_userID = Entry(Lfrm_UpUser_1, textvariable=UserID, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_userID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
        UfirstName = StringVar()
        etr_ufname = Entry(Lfrm_UpUser_1, textvariable=UfirstName, bg="#c1946a", fg="#622569",
                           font=("times", 20, "bold"))
        etr_ufname.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
        UlastName = StringVar()
        etr_ulname = Entry(Lfrm_UpUser_1, textvariable=UlastName, bg="#c1946a", fg="#622569",
                           font=("times", 20, "bold"))
        etr_ulname.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
        UpassWord = StringVar()
        etr_upsWord = Entry(Lfrm_UpUser_1, textvariable=UpassWord, bg="#c1946a", fg="#622569",
                            font=("times", 20, "bold"),
                            show="*")
        etr_upsWord.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

        def UpdateUser():
            if etr_userID =='' or etr_ufname =='' or etr_ulname.get() =='' or etr_upsWord.get() == '':
                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
            else:
                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                cur = conn.cursor()
                vTop = Toplevel()
                vTop.title('Confirm You Are Admin')
                vTop.geometry('500x350')
                vTop.configure(bg="#ffcc5c")
                Lfrm_top = LabelFrame(vTop,bg="#622569")
                Lfrm_top.grid(row=1,column=0,padx=20,pady=20)
                lbl_Aname = Label(Lfrm_top, text="Admin Name : ", bg="#ffcc5c", fg="#622569",
                                   font=("times", 15, "bold"))
                lbl_Aname.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                lbl_Apassword.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                AdmnID = StringVar()
                etr_AdmnID = Entry(Lfrm_top, textvariable=AdmnID, bg="#c1946a", fg="#622569",
                                 font=("times", 20, "bold"))
                etr_AdmnID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                AdmnPass = StringVar()
                etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569",show="*",
                                   font=("times", 20, "bold"))
                etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                def UPDATEUSER():
                    if AdmnID.get()=='' or AdmnPass.get()=='':
                        messagebox.showerror('Empty Field','You Must Enter Name and Password')
                    else:
                        #cur.execute("SELECT * FROM System_AdminTest1")
                        #e = cur.fetchall()
                        #print(e)
                        cur.execute("SELECT Admin_Name,Pass_Word FROM System_AdminTest1 WHERE Admin_Name=? AND Pass_word=?",
                                (AdmnID.get(), AdmnPass.get()))
                        c = cur.fetchall()

                        if c:
                            conn1 = sqlite3.connect('ProjoZ_SysTest1')
                            cur1 = conn1.cursor()
                            cur1.execute("UPDATE System_UserTest1 SET User_Id=?, First_Name=?, Last_Name=?, Pass_Word=? WHERE User_Id=?",
                                ((UserID.get(), UfirstName.get(), UlastName.get(), UpassWord.get(), UserID.get())))
                            conn1.commit()
                            conn1.close()
                            conn.commit()
                            conn.close()

                            def suxMesOut():
                                lbl_suxMes.grid_forget()
                                vTop.destroy()
                                etr_userID.focus()

                            etr_ufname.delete(0, END)
                            etr_ulname.delete(0, END)
                            etr_userID.delete(0, END)
                            etr_upsWord.delete(0, END)
                            lbl_suxMes = Label(vTop, text= etr_userID.get()+' Successfully Added To Database',
                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                            lbl_suxMes.grid(row=3, column=0)
                            lbl_suxMes.after(3000, suxMesOut)
                        else:
                            vTop.destroy()
                            messagebox.showerror('Wrong Entry','Wrong Name or Password.\n Cannot Proceed With User Update')
                            etr_userID.focus()

                btn_vTop = Button(vTop,text="Confirm",bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=UPDATEUSER)
                btn_vTop.grid(row=2,column=0)



        def BackAdmin():
            Lfrm_InC4ii.grid_forget()
            Lfrm_UpUser_1.grid_forget()
            lbl_MidC4.grid_forget()
            btn_saveUser.grid_forget()
            btn_backAdmin.grid_forget()
            Lfrm_InC4.grid(row=1, column=0, columnspan=2)
            Lfrm_UpAdmin.grid(row=0, column=0, padx=20, pady=10)
            Lfrm_UpUser.grid(row=1, column=0, padx=20, pady=10)
            Lfrm_RemUser.grid(row=2, column=0, padx=20, pady=10)
            Lfrm_RemApt.grid(row=3, column=0, padx=20, pady=10)
            Lfrm_bg.grid(row=4, column=0, padx=20, pady=10)
            btn_InL2a['state'] = NORMAL
            btn_InL2b['state'] = NORMAL
            btn_InL2c['state'] = NORMAL
            btn_InL2d['state'] = NORMAL
            btn_InL2e['state'] = NORMAL

        btn_saveUser = Button(frm_MidC4, text="Update User",bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 10, "bold",),
                         relief="raised", borderwidth=1, command=UpdateUser)
        btn_saveUser.grid(row=2,column=0)
        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                               relief="raised", borderwidth=1, command=BackAdmin)
        btn_backAdmin.grid(row=2, column=1)
    Lfrm_UpUser = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
    Lfrm_UpUser.grid(row=1, column=0, padx=20, pady=10)
    btn_UpUser = Button(Lfrm_UpUser, text="     _Update_ User_ Profile_           ", bg="#cfe0e8", fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",font=("times", 20, "bold"),
                        command=UpUser)
    btn_UpUser.grid()
#================================def============Remove===============User==============================================
    def RemUser():
        Lfrm_UpAdmin.grid_forget()
        Lfrm_UpUser.grid_forget()
        Lfrm_RemUser.grid_forget()
        Lfrm_RemApt.grid_forget()
        Lfrm_bg.grid_forget()
        Lfrm_InC4.grid_forget()
        btn_InL2a['state'] = DISABLED
        btn_InL2b['state'] = DISABLED
        btn_InL2c['state'] = DISABLED
        btn_InL2d['state'] = DISABLED
        btn_InL2e['state'] = DISABLED
        Lfrm_InC4iii = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
        Lfrm_InC4iii.grid(row=1, column=0, columnspan=2)

        Lfrm_RemUser_1 = LabelFrame(Lfrm_InC4iii, bg="#622569", padx=5, pady=5)
        Lfrm_RemUser_1.grid(row=0, column=0, padx=20, pady=10)
        lbl_MidC4 = Label(frm_MidC4, text=" Remove User From System", fg="#cfe0e8", bg="#622569",
                          font=("times", 10, "bold"))
        lbl_MidC4.grid(row=0, column=0)

        lbl_IDuser = Label(Lfrm_RemUser_1, text="_User__I_D : ", bg="#ffcc5c", fg="#622569",
                           font=("times", 10, "bold"))
        lbl_IDuser.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        lbl_UnameF = Label(Lfrm_RemUser_1, text="First Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_UnameF.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        lbl_UnameL = Label(Lfrm_RemUser_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_UnameL.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

        IDuser = StringVar()
        etr_IDuser = Entry(Lfrm_RemUser_1, textvariable=IDuser, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_IDuser.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
        UnameF = StringVar()
        etr_unamef = Entry(Lfrm_RemUser_1, textvariable=UnameF, bg="#c1946a", fg="#622569",
                           font=("times", 20, "bold"))
        etr_unamef.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
        UnameL = StringVar()
        etr_unamel = Entry(Lfrm_RemUser_1, textvariable=UnameL, bg="#c1946a", fg="#622569",
                           font=("times", 20, "bold"))
        etr_unamel.grid(row=2, column=2, columnspan=2, padx=10, pady=20)

        def RemoveUser():
            if etr_IDuser =='' or etr_unamef =='' or etr_unamel.get() =='':
                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
            else:
                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                cur = conn.cursor()
                vTop = Toplevel()
                vTop.title('Confirm You Are Admin')
                vTop.geometry('500x350')
                vTop.configure(bg="#ffcc5c")
                Lfrm_top = LabelFrame(vTop,bg="#622569")
                Lfrm_top.grid(row=1,column=0,padx=20,pady=20)
                lbl_Aname = Label(Lfrm_top, text="Admin Name : ", bg="#ffcc5c", fg="#622569",
                                   font=("times", 15, "bold"))
                lbl_Aname.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                lbl_Apassword.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                AdmnID = StringVar()
                etr_AdmnID = Entry(Lfrm_top, textvariable=AdmnID, bg="#c1946a", fg="#622569",
                                 font=("times", 20, "bold"))
                etr_AdmnID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                AdmnPass = StringVar()
                etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569",show="*",
                                   font=("times", 20, "bold"))
                etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                def REMOVEUSER():
                    if AdmnID.get()=='' or AdmnPass.get()=='':
                        messagebox.showerror('Empty Field','You Must Enter Name and Password')
                    else:
                        #cur.execute("SELECT * FROM System_AdminTest1")
                        #e = cur.fetchall()
                        #print(e)
                        cur.execute("SELECT Admin_Name,Pass_Word FROM System_AdminTest1 WHERE Admin_Name=? AND Pass_word=?",
                                (AdmnID.get(), AdmnPass.get()))
                        c = cur.fetchall()

                        if c:
                            conn1 = sqlite3.connect('ProjoZ_SysTest1')
                            cur1 = conn1.cursor()
                            cur1.execute("DELETE FROM System_UserTest1 WHERE User_Id=? AND First_Name=? AND Last_Name=?",((IDuser.get(), UnameF.get(), UnameL.get())))
                            conn1.commit()
                            conn1.close()
                            conn.commit()
                            conn.close()

                            def suxMesOut():
                                lbl_suxMes.grid_forget()
                                vTop.destroy()
                                etr_IDuser.focus()

                            etr_unamef.delete(0, END)
                            etr_unamel.delete(0, END)
                            etr_IDuser.delete(0, END)
                            lbl_suxMes = Label(vTop, text= etr_IDuser.get()+' Has Been Removed And Will No Longer Have Access To System',
                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                            lbl_suxMes.grid(row=3, column=0)
                            lbl_suxMes.after(3000, suxMesOut)
                        else:
                            vTop.destroy()
                            messagebox.showerror('Wrong Entry','Wrong Name or Password.\n Cannot Proceed With Removal')
                            etr_IDuser.focus()

                btn_vTop = Button(vTop,text="Remove",bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",activeforeground="#588c7e", font=("arial", 15, "bold"),
                         relief="raised", borderwidth=1, command=REMOVEUSER)
                btn_vTop.grid(row=2,column=0)
        def BackAdmin():
            Lfrm_InC4iii.grid_forget()
            Lfrm_RemUser_1.grid_forget()
            lbl_MidC4.grid_forget()
            btn_remUser.grid_forget()
            btn_backAdmin.grid_forget()
            Lfrm_InC4.grid(row=1, column=0, columnspan=2)
            Lfrm_UpAdmin.grid(row=0, column=0, padx=20, pady=10)
            Lfrm_UpUser.grid(row=1, column=0, padx=20, pady=10)
            Lfrm_RemUser.grid(row=2, column=0, padx=20, pady=10)
            Lfrm_RemApt.grid(row=3, column=0, padx=20, pady=10)
            Lfrm_bg.grid(row=4, column=0, padx=20, pady=10)
            btn_InL2a['state'] = NORMAL
            btn_InL2b['state'] = NORMAL
            btn_InL2c['state'] = NORMAL
            btn_InL2d['state'] = NORMAL
            btn_InL2e['state'] = NORMAL


        btn_remUser = Button(frm_MidC4, text="Remove User", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                              activeforeground="#588c7e", font=("arial", 10, "bold",),
                              relief="raised", borderwidth=1, command=RemoveUser)
        btn_remUser.grid(row=2, column=0)
        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                               relief="raised", borderwidth=1, command=BackAdmin)
        btn_backAdmin.grid(row=2, column=1)


    Lfrm_RemUser = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
    Lfrm_RemUser.grid(row=2, column=0, padx=20, pady=10)
    btn_RemUser = Button(Lfrm_RemUser, text="_Remove_ User_ From_ System_  ", bg="#cfe0e8", fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",font=("times", 20, "bold"),
                         command=RemUser)
    btn_RemUser.grid()

    Lfrm_RemApt = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
    Lfrm_RemApt.grid(row=3, column=0, padx=20, pady=10)
    btn_RemApt = Button(Lfrm_RemApt, text="Remove Apartment From System_", bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#cfe0e8",font=("times", 20, "bold"))
    btn_RemApt.grid()

    Lfrm_bg = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
    Lfrm_bg.grid(row=4, column=0, padx=20, pady=10)
    btn_bg = Button(Lfrm_bg, text="  _Change_System_Background_   ", bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#cfe0e8",font=("times", 20, "bold"))
    btn_bg.grid()







Lfrm_OutL1 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=40,pady=40)
Lfrm_OutL1.grid(row=1, column=0,padx=(15,50), pady=10)
frm_MidL1 = Frame(Lfrm_OutL1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL1.grid(row=1, column=0, padx=60,pady=15)
lbl_pageAd = Label(Lfrm_OutL1, text="Administrator_", bg="#ffcc5c", fg="#622569", font=("times",18))
lbl_pageAd.grid(row=0, column=0)

house = StringVar()
opt_select = OptionMenu(frm_MidL1, house, "Mimi","Mumu")
opt_select.grid(row=1, column=0, padx=20,pady=(5,80))

Lfrm_OutL2 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutL2.grid(row=2, column=0,padx=(5,50),pady=50)
frm_MidL2 = Frame(Lfrm_OutL2, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL2.grid(padx=15,pady=15)
Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InL2.grid()

btn_InL2a = Button(Lfrm_InL2,text="Create New Apartment", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                   command=createNewApartment)
btn_InL2a.grid(padx=10, pady=10)
btn_InL2b = Button(Lfrm_InL2,text="  Add___New__User  ", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                   command=addNewUser)
btn_InL2b.grid(padx=10, pady=10)
btn_InL2c = Button(Lfrm_InL2,text=" H_o_u_s_e_Accounts", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2c.grid(padx=10, pady=10)
btn_InL2d = Button(Lfrm_InL2,text="  B_i_l_l_Man_age_r_", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InL2d.grid(padx=10, pady=10)
btn_InL2e = Button(Lfrm_InL2,text=" A_d_m_i_n_Office    ", font=("times",15), bg="#cfe0e8", fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                   command=Office)
btn_InL2e.grid(padx=10, pady=10)


frm_Right = Frame(master,bg="#cfe0e8", padx=0, pady=0)
frm_Right.grid(row=1, column=4, rowspan=2, pady=(20,10), padx=(20,20))
Lfrm_OutR1 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR1.grid(row=1, column=0,padx=(50,0),pady=(20,10))
frm_MidR1 = Frame(Lfrm_OutR1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR1.grid(padx=8,pady=8)
Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR1.grid()
btn_InR1 = Button(Lfrm_InR1,text="To Do List", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR1.grid(padx=10, pady=10)

Lfrm_OutR2 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR2.grid(row=2, column=0,padx=(50,0),pady=(20,10))
frm_MidR2 = Frame(Lfrm_OutR2, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR2.grid(padx=8,pady=8)
Lfrm_InR2 = LabelFrame(frm_MidR2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR2.grid()
btn_InR2 = Button(Lfrm_InR2,text="Set Reminder", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR2.grid(padx=10, pady=10)

Lfrm_OutR3 = LabelFrame(frm_Right,relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR3.grid(row=3, column=0,padx=(50,0),pady=(20,10))
frm_MidR3 = Frame(Lfrm_OutR3, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR3.grid(padx=8,pady=8)
Lfrm_InR3 = LabelFrame(frm_MidR3, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR3.grid()
btn_InR3 = Button(Lfrm_InR3,text="Sticky Note", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR3.grid(padx=10, pady=10)

Lfrm_OutR4 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR4.grid(row=4, column=0,padx=(50,0),pady=(20,10))
frm_MidR4 = Frame(Lfrm_OutR4, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR4.grid(padx=8,pady=8)
Lfrm_InR4 = LabelFrame(frm_MidR4, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR4.grid()
btn_InR4 = Button(Lfrm_InR4,text="Tenant Box", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_InR4.grid(padx=10, pady=10)

mainloop()