import tkinter
from tkinter import *
from tkinter import ttk
import tkcalendar
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import random


master = Tk()
master.title('WELCOME TO GRACIOUS APARTMENTS')
sW = master.winfo_screenwidth()
sH = master.winfo_screenheight()
aW = sW - 200
aH = sH - 100
posx = (sW/2) - (aW/2)
posy = (sH/2) - (aH/2)
master.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
master.configure(background="#cfe0e8")



def expandBlueG():
    lbl_Introg.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introg.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introg.after(5000, shrinkNormal)
Lfrm_Gracious = LabelFrame(master, relief="groove", bg="#ffcc5c")
Lfrm_Gracious.grid(padx=100,pady=50)
lbl_Introg = Label(Lfrm_Gracious, text="G", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)
lbl_Introg.after(3000, expandBlueG)



#lbl_Intror = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1,column=4)
def expandBlueR():
    lbl_Intror.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intror.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introg.after(5000, shrinkNormal)
lbl_Intror = Label(Lfrm_Gracious, text="R", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intror.grid(row=1, column=4)
lbl_Intror.after(4000, expandBlueR)

#lbl_Introa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=5)
def expandBlueA():
    lbl_Introa.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introa.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introa.after(5000, shrinkNormal)
lbl_Introa = Label(Lfrm_Gracious, text="A", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introa.grid(row=1, column=5)
lbl_Introa.after(5000, expandBlueA)

#lbl_Introc = Label(frm_Intro, text="C", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=6)
def expandBlueC():
    lbl_Introc.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introc.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introc.after(5000, shrinkNormal)
lbl_Introc = Label(Lfrm_Gracious, text="C", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introc.grid(row=1, column=6)
lbl_Introc.after(6000, expandBlueC)

#lbl_Introi = Label(frm_Intro, text="I", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=7)
def expandBlueI():
    lbl_Introi.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introi.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introi.after(5000, shrinkNormal)
lbl_Introi = Label(Lfrm_Gracious, text="I", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introi.grid(row=1, column=7)
lbl_Introi.after(7000, expandBlueI)

#lbl_Introo = Label(frm_Intro, text="O", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=8)
def expandBlueO():
    lbl_Introo.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introo.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introo.after(5000, shrinkNormal)
lbl_Introo = Label(Lfrm_Gracious, text="O", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introo.grid(row=1, column=8)
lbl_Introo.after(8000, expandBlueO)

#lbl_Introu = Label(frm_Intro, text="U", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=9)
def expandBlueU():
    lbl_Introu.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introu.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introu.after(5000, shrinkNormal)
lbl_Introu = Label(Lfrm_Gracious, text="U", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introu.grid(row=1, column=9)
lbl_Introu.after(9000, expandBlueU)

#lbl_Intros = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=10)
def expandBlueS():
    lbl_Intros.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intros.configure(font=("times",85), fg="#cfe0e8")
    lbl_Intros.after(5000, shrinkNormal)
lbl_Intros = Label(Lfrm_Gracious, text="S", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intros.grid(row=1, column=10)
lbl_Intros.after(10000, expandBlueS)
#===================================================apartments======================================================
#lbl_Introap = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=2)
def expandBlueAP():
    lbl_Introap.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introap.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introap.after(4000, shrinkNormal)
lbl_Introap = Label(Lfrm_Gracious, text="   A", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introap.grid(row=1, column=11)
lbl_Introap.after(10000, expandBlueAP)

#lbl_Introp = Label(frm_Intro, text="P", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=3)
def expandBlueP():
    lbl_Introp.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introp.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introp.after(4000, shrinkNormal)
lbl_Introp = Label(Lfrm_Gracious, text="P", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introp.grid(row=1, column=12)
lbl_Introp.after(9000, expandBlueP)

#lbl_Introsa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=4)
def expandBlueSA():
    lbl_Introsa.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsa.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsa.after(4000, shrinkNormal)
lbl_Introsa = Label(Lfrm_Gracious, text="A", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsa.grid(row=1, column=13)
lbl_Introsa.after(8000, expandBlueSA)

#lbl_Introsr = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=5)
def expandBlueSR():
    lbl_Introsr.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsr.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsr.after(4000, shrinkNormal)
lbl_Introsr = Label(Lfrm_Gracious, text="R", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsr.grid(row=1, column=14)
lbl_Introsr.after(7000, expandBlueSR)

#lbl_Introst = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=6)
def expandBlueST():
    lbl_Introst.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introst.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introst.after(4000, shrinkNormal)
lbl_Introst = Label(Lfrm_Gracious, text="T", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introst.grid(row=1, column=15)
lbl_Introst.after(6000, expandBlueST)

#lbl_Intros = Label(frm_Intro, text="M", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=7)
def expandBlueM():
    lbl_Introm.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introm.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introm.after(4000, shrinkNormal)
lbl_Introm = Label(Lfrm_Gracious, text="M", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introm.grid(row=1, column=16)
lbl_Introm.after(5000, expandBlueM)

#lbl_Introse = Label(frm_Intro, text="E", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=8)
def expandBlueSE():
    lbl_Introse.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introse.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introse.after(4000, shrinkNormal)
lbl_Introse = Label(Lfrm_Gracious, text="E", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introse.grid(row=1, column=17)
lbl_Introse.after(4000, expandBlueSE)

#lbl_Introsn = Label(frm_Intro, text="N", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=9)
def expandBlueSN():
    lbl_Introsn.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsn.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsn.after(4000, shrinkNormal)
lbl_Introsn = Label(Lfrm_Gracious, text="N", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsn.grid(row=1, column=18)
lbl_Introsn.after(3000, expandBlueSN)

#lbl_Introsx = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=10)
def expandBlueSX():
    lbl_Introsx.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsx.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsx.after(4000, shrinkNormal)
lbl_Introsx = Label(Lfrm_Gracious, text="T", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsx.grid(row=1, column=19)
lbl_Introsx.after(2000, expandBlueSX)

#lbl_Intross = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=11)
def expandBlueSS():
    lbl_Intross.configure(font=("arial",90,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intross.configure(font=("times",85), fg="#cfe0e8")
    lbl_Intross.after(4000, shrinkNormal)
lbl_Intross = Label(Lfrm_Gracious, text="S", font=("futura",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intross.grid(row=1, column=20)
lbl_Intross.after(1000, expandBlueSS)





Lfrm_Out = LabelFrame(master, text="Welcome Grace",font=("arial",5), relief="raised", borderwidth=5, bg="#ffcc5c",padx=20,pady=20)
Lfrm_Out.grid(padx=500, pady=100)
frm_Mid = Frame(Lfrm_Out, relief="raised", borderwidth=5, bg="#cfe0e8",padx=10,pady=10)
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#ffcc5c")
Lfrm_In.grid()

lbl_User = Label(Lfrm_In, text="User_Name: ", bg="#ffcc5c", fg="#622569", font=("times",20,"bold"))
lbl_User.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
lbl_Pass = Label(Lfrm_In, text="Pass_Word: ", bg="#ffcc5c", fg="#622569", font=("times",20,"bold"))
lbl_Pass.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

User_Name = StringVar()
etr_User = Entry(Lfrm_In, textvariable=User_Name, bg="#cfe0e8", fg="#622569", font=("times",20,"bold"))
etr_User.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
Pass_Word = StringVar()
etr_Pass = Entry(Lfrm_In, textvariable=Pass_Word, bg="#cfe0e8", fg="#622569", font=("times",20,"bold"), show='*')
etr_Pass.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

def Validate():
    if User_Name.get()=='' or Pass_Word.get()=='':
        messagebox.showerror('Empty Fields','User Name and Password Must Be Filled')
    else:
        conn = sqlite3.connect('User_Data')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        a = cur.fetchall()
        #print(a)
        cur.execute("SELECT * FROM user WHERE user_id=? AND password=?",(User_Name.get(), Pass_Word.get()))
        c= cur.fetchall()
        if c:
            print('Login Successful')
        else:
            print('Login Failed!!')

        conn.commit()
        conn.close()

btn_Login = Button(frm_Mid, text="Log In", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69", activeforeground="#588c7e", font=("arial",15,"bold"), command=Validate)
btn_Login.grid(padx=2, pady=4)








mainloop()