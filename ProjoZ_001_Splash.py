from tkinter import *
from tkinter import ttk
from tkcalendar import *
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import datetime
import tempfile
import os

mainframe = Tk()
mainframe.title('WELCOME TO GRACIOUS APARTMENTS')
sW = mainframe.winfo_screenwidth()
sH = mainframe.winfo_screenheight()
aW = sW - 200
aH = sH - 100
posx = (sW/2) - (aW/2)
posy = (sH/2) - (aH/2)
mainframe.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
mainframe.configure(background="#ffcc5c")

def expandBlueG():
    lbl_Introg.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introg.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introg.after(5000, shrinkNormal)
frm_Intro = Frame(mainframe,bg="#ffcc5c")
frm_Intro.grid(padx=(500,500), pady=(300,10))
lbl_Introg = Label(frm_Intro, text="G", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)
lbl_Introg.after(3000, expandBlueG)



#lbl_Intror = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1,column=4)
def expandBlueR():
    lbl_Intror.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intror.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introg.after(5000, shrinkNormal)
lbl_Intror = Label(frm_Intro, text="R", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intror.grid(row=1, column=4)
lbl_Intror.after(4000, expandBlueR)

#lbl_Introa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=5)
def expandBlueA():
    lbl_Introa.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introa.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introa.after(5000, shrinkNormal)
lbl_Introa = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introa.grid(row=1, column=5)
lbl_Introa.after(5000, expandBlueA)

#lbl_Introc = Label(frm_Intro, text="C", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=6)
def expandBlueC():
    lbl_Introc.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introc.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introc.after(5000, shrinkNormal)
lbl_Introc = Label(frm_Intro, text="C", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introc.grid(row=1, column=6)
lbl_Introc.after(6000, expandBlueC)

#lbl_Introi = Label(frm_Intro, text="I", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=7)
def expandBlueI():
    lbl_Introi.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introi.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introi.after(5000, shrinkNormal)
lbl_Introi = Label(frm_Intro, text="I", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introi.grid(row=1, column=7)
lbl_Introi.after(7000, expandBlueI)

#lbl_Introo = Label(frm_Intro, text="O", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=8)
def expandBlueO():
    lbl_Introo.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introo.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introo.after(5000, shrinkNormal)
lbl_Introo = Label(frm_Intro, text="O", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introo.grid(row=1, column=8)
lbl_Introo.after(8000, expandBlueO)

#lbl_Introu = Label(frm_Intro, text="U", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=9)
def expandBlueU():
    lbl_Introu.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introu.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introu.after(5000, shrinkNormal)
lbl_Introu = Label(frm_Intro, text="U", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introu.grid(row=1, column=9)
lbl_Introu.after(9000, expandBlueU)

#lbl_Intros = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=10)
def expandBlueS():
    lbl_Intros.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intros.configure(font=("times",85), fg="#cfe0e8")
    lbl_Intros.after(5000, shrinkNormal)
lbl_Intros = Label(frm_Intro, text="S", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intros.grid(row=1, column=10)
lbl_Intros.after(10000, expandBlueS)
#===================================================apartments======================================================
#lbl_Introap = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=2)
def expandBlueAP():
    lbl_Introap.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introap.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introap.after(4000, shrinkNormal)
lbl_Introap = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introap.grid(row=2, column=2)
lbl_Introap.after(10000, expandBlueAP)

#lbl_Introp = Label(frm_Intro, text="P", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=3)
def expandBlueP():
    lbl_Introp.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introp.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introp.after(4000, shrinkNormal)
lbl_Introp = Label(frm_Intro, text="P", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introp.grid(row=2, column=3)
lbl_Introp.after(9000, expandBlueP)

#lbl_Introsa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=4)
def expandBlueSA():
    lbl_Introsa.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsa.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsa.after(4000, shrinkNormal)
lbl_Introsa = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsa.grid(row=2, column=4)
lbl_Introsa.after(8000, expandBlueSA)

#lbl_Introsr = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=5)
def expandBlueSR():
    lbl_Introsr.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsr.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsr.after(4000, shrinkNormal)
lbl_Introsr = Label(frm_Intro, text="R", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsr.grid(row=2, column=5)
lbl_Introsr.after(7000, expandBlueSR)

#lbl_Introst = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=6)
def expandBlueST():
    lbl_Introst.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introst.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introst.after(4000, shrinkNormal)
lbl_Introst = Label(frm_Intro, text="T", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introst.grid(row=2, column=6)
lbl_Introst.after(6000, expandBlueST)

#lbl_Intros = Label(frm_Intro, text="M", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=7)
def expandBlueM():
    lbl_Introm.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introm.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introm.after(4000, shrinkNormal)
lbl_Introm = Label(frm_Intro, text="M", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introm.grid(row=2, column=7)
lbl_Introm.after(5000, expandBlueM)

#lbl_Introse = Label(frm_Intro, text="E", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=8)
def expandBlueSE():
    lbl_Introse.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introse.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introse.after(4000, shrinkNormal)
lbl_Introse = Label(frm_Intro, text="E", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introse.grid(row=2, column=8)
lbl_Introse.after(4000, expandBlueSE)

#lbl_Introsn = Label(frm_Intro, text="N", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=9)
def expandBlueSN():
    lbl_Introsn.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsn.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsn.after(4000, shrinkNormal)
lbl_Introsn = Label(frm_Intro, text="N", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsn.grid(row=2, column=9)
lbl_Introsn.after(3000, expandBlueSN)

#lbl_Introsx = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=10)
def expandBlueSX():
    lbl_Introsx.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Introsx.configure(font=("times",85), fg="#cfe0e8")
    lbl_Introsx.after(4000, shrinkNormal)
lbl_Introsx = Label(frm_Intro, text="T", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introsx.grid(row=2, column=10)
lbl_Introsx.after(2000, expandBlueSX)

#lbl_Intross = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=11)
def expandBlueSS():
    lbl_Intross.configure(font=("arial",100,"bold"), fg="#622569")
    def shrinkNormal():
        lbl_Intross.configure(font=("times",85), fg="#cfe0e8")
    lbl_Intross.after(4000, shrinkNormal)
lbl_Intross = Label(frm_Intro, text="S", font=("times",85), bg="#ffcc5c", fg="#cfe0e8")
lbl_Intross.grid(row=2, column=11)
lbl_Intross.after(1000, expandBlueSS)

def logIn():
    mainframe.destroy()
    master = Tk()
    master.title('WELCOME TO GRACIOUS APARTMENTS')
    sW = master.winfo_screenwidth()
    sH = master.winfo_screenheight()
    aW = sW - 200
    aH = sH - 100
    posx = (sW / 2) - (aW / 2)
    posy = (sH / 2) - (aH / 2)
    master.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
    master.configure(background="#cfe0e8")

    def expandBlueG():
        lbl_Introg.configure(font=("arial", 100, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introg.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introg.after(5000, shrinkNormal)

    Lfrm_Gracious = LabelFrame(master, relief="groove", bg="#ffcc5c")
    Lfrm_Gracious.grid(padx=100, pady=50)
    lbl_Introg = Label(Lfrm_Gracious, text="G", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introg.grid(row=1, column=3)
    lbl_Introg.after(3000, expandBlueG)

    # lbl_Intror = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1,column=4)
    def expandBlueR():
        lbl_Intror.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Intror.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introg.after(5000, shrinkNormal)

    lbl_Intror = Label(Lfrm_Gracious, text="R", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Intror.grid(row=1, column=4)
    lbl_Intror.after(4000, expandBlueR)

    # lbl_Introa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=5)
    def expandBlueA():
        lbl_Introa.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introa.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introa.after(5000, shrinkNormal)

    lbl_Introa = Label(Lfrm_Gracious, text="A", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introa.grid(row=1, column=5)
    lbl_Introa.after(5000, expandBlueA)

    # lbl_Introc = Label(frm_Intro, text="C", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=6)
    def expandBlueC():
        lbl_Introc.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introc.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introc.after(5000, shrinkNormal)

    lbl_Introc = Label(Lfrm_Gracious, text="C", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introc.grid(row=1, column=6)
    lbl_Introc.after(6000, expandBlueC)

    # lbl_Introi = Label(frm_Intro, text="I", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=7)
    def expandBlueI():
        lbl_Introi.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introi.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introi.after(5000, shrinkNormal)

    lbl_Introi = Label(Lfrm_Gracious, text="I", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introi.grid(row=1, column=7)
    lbl_Introi.after(7000, expandBlueI)

    # lbl_Introo = Label(frm_Intro, text="O", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=8)
    def expandBlueO():
        lbl_Introo.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introo.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introo.after(5000, shrinkNormal)

    lbl_Introo = Label(Lfrm_Gracious, text="O", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introo.grid(row=1, column=8)
    lbl_Introo.after(8000, expandBlueO)

    # lbl_Introu = Label(frm_Intro, text="U", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=9)
    def expandBlueU():
        lbl_Introu.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introu.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introu.after(5000, shrinkNormal)

    lbl_Introu = Label(Lfrm_Gracious, text="U", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introu.grid(row=1, column=9)
    lbl_Introu.after(9000, expandBlueU)

    # lbl_Intros = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=1, column=10)
    def expandBlueS():
        lbl_Intros.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Intros.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Intros.after(5000, shrinkNormal)

    lbl_Intros = Label(Lfrm_Gracious, text="S", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Intros.grid(row=1, column=10)
    lbl_Intros.after(10000, expandBlueS)

    # ===================================================apartments======================================================
    # lbl_Introap = Label(frm_Intro, text="A", font=("times",85), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=2)
    def expandBlueAP():
        lbl_Introap.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introap.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introap.after(4000, shrinkNormal)

    lbl_Introap = Label(Lfrm_Gracious, text="   A", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introap.grid(row=1, column=11)
    lbl_Introap.after(10000, expandBlueAP)

    # lbl_Introp = Label(frm_Intro, text="P", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=3)
    def expandBlueP():
        lbl_Introp.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introp.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introp.after(4000, shrinkNormal)

    lbl_Introp = Label(Lfrm_Gracious, text="P", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introp.grid(row=1, column=12)
    lbl_Introp.after(9000, expandBlueP)

    # lbl_Introsa = Label(frm_Intro, text="A", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=4)
    def expandBlueSA():
        lbl_Introsa.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introsa.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introsa.after(4000, shrinkNormal)

    lbl_Introsa = Label(Lfrm_Gracious, text="A", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introsa.grid(row=1, column=13)
    lbl_Introsa.after(8000, expandBlueSA)

    # lbl_Introsr = Label(frm_Intro, text="R", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=5)
    def expandBlueSR():
        lbl_Introsr.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introsr.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introsr.after(4000, shrinkNormal)

    lbl_Introsr = Label(Lfrm_Gracious, text="R", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introsr.grid(row=1, column=14)
    lbl_Introsr.after(7000, expandBlueSR)

    # lbl_Introst = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=6)
    def expandBlueST():
        lbl_Introst.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introst.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introst.after(4000, shrinkNormal)

    lbl_Introst = Label(Lfrm_Gracious, text="T", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introst.grid(row=1, column=15)
    lbl_Introst.after(6000, expandBlueST)

    # lbl_Intros = Label(frm_Intro, text="M", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=7)
    def expandBlueM():
        lbl_Introm.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introm.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introm.after(4000, shrinkNormal)

    lbl_Introm = Label(Lfrm_Gracious, text="M", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introm.grid(row=1, column=16)
    lbl_Introm.after(5000, expandBlueM)

    # lbl_Introse = Label(frm_Intro, text="E", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=8)
    def expandBlueSE():
        lbl_Introse.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introse.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introse.after(4000, shrinkNormal)

    lbl_Introse = Label(Lfrm_Gracious, text="E", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introse.grid(row=1, column=17)
    lbl_Introse.after(4000, expandBlueSE)

    # lbl_Introsn = Label(frm_Intro, text="N", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=9)
    def expandBlueSN():
        lbl_Introsn.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introsn.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introsn.after(4000, shrinkNormal)

    lbl_Introsn = Label(Lfrm_Gracious, text="N", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introsn.grid(row=1, column=18)
    lbl_Introsn.after(3000, expandBlueSN)

    # lbl_Introsx = Label(frm_Intro, text="T", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=10)
    def expandBlueSX():
        lbl_Introsx.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Introsx.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Introsx.after(4000, shrinkNormal)

    lbl_Introsx = Label(Lfrm_Gracious, text="T", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Introsx.grid(row=1, column=19)
    lbl_Introsx.after(2000, expandBlueSX)

    # lbl_Intross = Label(frm_Intro, text="S", font=("times",65, "bold"), bg="#ffcc5c", fg="#cfe0e8").grid(row=2, column=11)
    def expandBlueSS():
        lbl_Intross.configure(font=("arial", 90, "bold"), fg="#622569")

        def shrinkNormal():
            lbl_Intross.configure(font=("times", 85), fg="#cfe0e8")

        lbl_Intross.after(4000, shrinkNormal)

    lbl_Intross = Label(Lfrm_Gracious, text="S", font=("futura", 85), bg="#ffcc5c", fg="#cfe0e8")
    lbl_Intross.grid(row=1, column=20)
    lbl_Intross.after(1000, expandBlueSS)

    Lfrm_Outlogin = LabelFrame(master, text="Welcome Grace", font=("arial", 5), relief="raised", borderwidth=5, bg="#ffcc5c",
                          padx=20, pady=20)
    Lfrm_Outlogin.grid(padx=500, pady=100)
    frm_Mid = Frame(Lfrm_Outlogin, relief="raised", borderwidth=5, bg="#cfe0e8", padx=10, pady=10)
    frm_Mid.grid()
    Lfrm_In = LabelFrame(frm_Mid, bg="#ffcc5c")
    Lfrm_In.grid()

    lbl_User = Label(Lfrm_In, text="User_Name: ", bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
    lbl_User.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
    lbl_Pass = Label(Lfrm_In, text="Pass_Word: ", bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
    lbl_Pass.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

    User_Name = StringVar()
    etr_User = Entry(Lfrm_In, textvariable=User_Name, bg="#cfe0e8", fg="#622569", font=("times", 20, "bold"))
    etr_User.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
    Pass_Word = StringVar()
    etr_Pass = Entry(Lfrm_In, textvariable=Pass_Word, bg="#cfe0e8", fg="#622569", font=("times", 20, "bold"), show='*')
    etr_Pass.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

    def homePage():
        Lfrm_Outlogin.grid_forget()
        Lfrm_Gracious.grid_forget()
        Lfrm_Graciousmaster = LabelFrame(master, relief="groove", bg="#ffcc5c")
        Lfrm_Graciousmaster.grid(padx=150, pady=20,row=0,column=0, columnspan=5)
        lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura", 85,), bg="#ffcc5c",
                           fg="#cfe0e8")
        lbl_Introg.grid(row=0, column=3)
        def logout():
            Lfrm_Outhpage.grid_forget()
            Lfrm_Graciousmaster.grid_forget()
            '''Lfrm_Graciouslg = LabelFrame(master, relief="groove", bg="#ffcc5c")
            Lfrm_Graciouslg.grid(padx=100, pady=50)
            lbl_Introglg = Label(Lfrm_Graciouslg, text="GRACIOUS APARTMENTS", font=("futura", 85,), bg="#ffcc5c",
                               fg="#cfe0e8")
            lbl_Introglg.grid(row=1, column=3)'''
            Lfrm_Gracious.grid(row=0,column=0, columnspan=5,padx=150,pady=20)
            Lfrm_Outlogin.grid(row=1,column=2,padx=500,pady=200)


        Lfrm_Outhpage = LabelFrame(master, text="Welcome Grace", font=("arial", 5), relief="raised", borderwidth=5,
                                   bg="#ffcc5c", padx=40, pady=20)
        Lfrm_Outhpage.grid(row=2, column=2,padx=500, pady=50)
        frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
        frm_Mid.grid()
        btn_LogOut = Button(Lfrm_Outhpage, text=" Log_ Out ", pady=10, command=logout, activebackground="#ff6f69",activeforeground="#588c7e",
                              font=("times", 10, "bold"), fg="blue", bg="pink")
        btn_LogOut.grid()
        Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=15, pady=20)
        Lfrm_In.grid()

        def houseCommand():
            frm_house.configure(bg="#ffcc5c", padx=0, pady=0)
            btn_house.configure(font=("times", 40), bg="#ffcc5c", fg="#622569")
            btn_house.grid_configure(padx=0, pady=0)
            Lfrm_Gracious = LabelFrame(master, relief="groove", bg="#ffcc5c")
            Lfrm_Gracious.grid(row=0, column=0, columnspan=5, padx=150, pady=20)
            lbl_Introg = Label(Lfrm_Gracious, text="GRACIOUS APARTMENTS", font=("futura", 85,), bg="#ffcc5c",
                               fg="#cfe0e8")
            lbl_Introg.grid(row=0, column=3)

            Lfrm_OutCacc = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
            Lfrm_OutCacc.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
            frm_MidC = Frame(Lfrm_OutCacc, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
            frm_MidC.grid(row=1, column=0)
            Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
            Lfrm_InC.grid(row=0, column=0, columnspan=2)

            Lfrm_OutL1acc = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
            Lfrm_OutL1acc.grid(row=1, column=0, padx=(15, 50), pady=10)
            frm_MidL1 = Frame(Lfrm_OutL1acc, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
            frm_MidL1.grid(row=1, column=0, padx=60, pady=15)
            lbl_pageAd = Label(Lfrm_OutL1acc, text="_Select_ Apartment_", bg="#ffcc5c", fg="#622569",
                               font=("times", 18))
            lbl_pageAd.grid(row=0, column=0)
            def houseAccounts():
                Lfrm_Outhpage.grid_forget()
                class Apartment:
                    def __init__(self, hseName, location, num_units, numFloors):
                        self.hseName = hseName
                        self.location = location
                        self.num_units = num_units
                        self.numFloors = numFloors

                # =================================Page Apartment Details===============================================================
                def ApartmentDetails():
                    Lfrm_OutCacc.grid_forget()
                    Lfrm_OutL1acc.grid_forget()
                    Lfrm_OutL2acc.grid_forget()
                    frm_Rightacc.grid_forget()

                    conn = sqlite3.connect('Gracious_Data')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Apartment WHERE House_Name=?", (house.get(),))
                    d = cur.fetchall()
                    print(d)
                    # Apart = d[0]
                    House_Name = d[0][0]
                    Location = d[0][1]
                    Num_Units = d[0][2]
                    Floors = d[0][3]
                    selectedApt = Apartment(House_Name, Location, Num_Units, Floors)
                    conn.commit()
                    conn.close()

                    Lfrm_OutL1A = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
                    Lfrm_OutL1A.grid(row=1, column=0, padx=(15, 5), pady=10)
                    frm_MidL1 = Frame(Lfrm_OutL1A, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                    frm_MidL1.grid(row=1, column=0, padx=60, pady=15)
                    lbl_pageAdh = Label(Lfrm_OutL1A, text=selectedApt.hseName, bg="#ffcc5c", fg="#622569", font=("times", 25))
                    lbl_pageAdh.grid(row=0, column=0)
                    lbl_pageAdl = Label(Lfrm_OutL1A, text="City/Town " + selectedApt.location, bg="#ffcc5c", fg="#622569",
                                        font=("times", 10))
                    lbl_pageAdl.grid(row=1, column=0)
                    lbl_pageAdnm = Label(Lfrm_OutL1A, text="No.of Units " + str(selectedApt.num_units), bg="#ffcc5c", fg="#622569",
                                         font=("times", 10))
                    lbl_pageAdnm.grid(row=2, column=0)
                    lbl_pageAdf = Label(Lfrm_OutL1A, text="No.of Floors " + str(selectedApt.numFloors), bg="#ffcc5c", fg="#622569",
                                        font=("times", 10))
                    lbl_pageAdf.grid(row=3, column=0)

                    Lfrm_OutL2A = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                    Lfrm_OutL2A.grid(row=2, column=0, padx=(5, 50), pady=10, rowspan=2)
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
                        # Lfrm_OutC = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
                        Lfrm_OutCacc.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                        # Lfrm_OutL1 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
                        Lfrm_OutL1acc.grid(row=1, column=0, padx=(15, 50), pady=10)
                        # Lfrm_OutL2 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                        Lfrm_OutL2acc.grid(row=2, column=0, padx=(5, 50), pady=50)
                        # frm_Right = Frame(master, bg="#cfe0e8", padx=0, pady=0)
                        frm_Rightacc.grid(row=1, column=4, rowspan=2, pady=(20, 10), padx=(20, 20))

                    Lfrm_btnL2A = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
                    Lfrm_btnL2A.grid(pady=(0, 10))
                    btn_InL2a = Button(Lfrm_btnL2A, text="B_A_C_K_ H_o_m_e_", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                                       command=BackHouse)
                    btn_InL2a.grid()

                    def viewTenants():
                        conn = sqlite3.connect('Gracious_Data')
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

                        cur.execute(
                            "SELECT House_No,First_Name, Last_Name, Id_No, Contact FROM Apartment_Tenants WHERE Apart_Name=?",
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
                            tree_ten.item(selected, text='', values=(
                            etr_hsNo.get(), etr_fname.get(), etr_lname.get(), etr_id.get(), etr_contact.get()))

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

                        btn_reset = Button(frame_treeten, text="_Reset/Clear_", pady=10, command=resetField,
                                           activebackground="#ff6f69",
                                           activeforeground="#588c7e",
                                           font=("times", 10, "bold"), fg="blue", bg="pink")
                        btn_reset.grid(row=3, column=0, pady=10)
                        btn_editTree = Button(frame_treeten, text="Click On Record To Edit.", pady=10, command=EditSelected,
                                              activebackground="#ff6f69", activeforeground="#588c7e",
                                              font=("times", 10, "bold"), fg="blue", bg="pink")
                        btn_editTree.grid(row=3, column=1, pady=10)
                        btn_exitTree = Button(frame_treeten, text=" E_X_I_T ", pady=10, command=exitTree,
                                              activebackground="#ff6f69",
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
                        conn = sqlite3.connect('Gracious_Data')
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

                        for hsno, mtrno in hm:
                            treemtr.tag_configure('evenrow', background="white")
                            treemtr.tag_configure('oddrow', background="lightblue")
                            line = 0
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
                    Lfrm_btnL2B.grid(pady=(10, 10))
                    btn_InL2b = Button(Lfrm_btnL2B, text="View " + selectedApt.hseName + " Tenants", font=("times", 15),
                                       bg="#cfe0e8", fg="#622569",
                                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                                       command=viewTenants)
                    btn_InL2b.grid()
                    Lfrm_btnL2C = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
                    Lfrm_btnL2C.grid(pady=(0, 10))
                    btn_InL2c = Button(Lfrm_btnL2C, text="View Meter Numbers", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                                       command=ViewMeter)
                    btn_InL2c.grid()
                    Lfrm_btnL2D = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
                    Lfrm_btnL2D.grid(pady=(0, 10))
                    btn_InL2d = Button(Lfrm_btnL2D, text="_V_i_e_w_  _Houses", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                    btn_InL2d.grid()
                    Lfrm_btnL2E = LabelFrame(Lfrm_InL2A, bg="#622569", padx=5, pady=5)
                    Lfrm_btnL2E.grid(pady=(0, 10))
                    btn_InL2e = Button(Lfrm_btnL2E, text="_A-g_e_n_t _Report", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                       activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                    btn_InL2e.grid()

                    Lfrm_OutCt = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=10)
                    Lfrm_OutCt.grid(row=1, column=1, rowspan=2, columnspan=1, padx=(5, 10), pady=10)
                    frm_MidCt = Frame(Lfrm_OutCt, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                    frm_MidCt.grid(row=1, column=0)
                    Lfrm_InCt = LabelFrame(frm_MidCt, bg="#cfe0e8", padx=15, pady=20)
                    Lfrm_InCt.grid(row=1, column=0, columnspan=2)

                    Lfrm_OutCb = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=10)
                    Lfrm_OutCb.grid(row=3, column=1, rowspan=1, columnspan=1, padx=(5, 10), pady=10)
                    frm_MidCb = Frame(Lfrm_OutCb, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                    frm_MidCb.grid(row=1, column=0)
                    Lfrm_InCb = LabelFrame(frm_MidCb, bg="#cfe0e8", padx=15, pady=20)
                    Lfrm_InCb.grid(row=1, column=0, columnspan=2)

                    frm_RightA = Frame(master, bg="#cfe0e8", padx=0, pady=0)
                    frm_RightA.grid(row=1, column=2, rowspan=3, pady=10, padx=(5, 10))
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

                    lbl_OutCt = Label(Lfrm_OutCt, text="Add Tenant Details To Apartment_", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_OutCt.grid(row=0, column=0)

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
                    radio_phone = Radiobutton(Lfrm_InCt, text="Phone", variable=info, value="Phone", bg="#c1946a", fg="#622569",
                                              font=("times", 10, "bold"))
                    radio_phone.grid(row=5, column=1, columnspan=2, padx=10, pady=2)
                    radio_email = Radiobutton(Lfrm_InCt, text="Email", variable=info, value="Email", bg="#c1946a", fg="#622569",
                                              font=("times", 10, "bold"))
                    radio_email.grid(row=5, column=2, columnspan=2, padx=10, pady=2)
                    contact = StringVar()
                    etr_contact = Entry(Lfrm_InCt, textvariable=contact, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
                    etr_contact.grid(row=6, column=1, columnspan=2, padx=10, pady=2)

                    etr_hse.delete(0, END)
                    etr_hse.insert(END, house.get())
                    etr_hse.configure(state=DISABLED)

                    def AddTenant():
                        if hsNo.get() == '':
                            messagebox.showerror('No Entry', 'House No must be filled')
                        elif etr_fname.get() == '':
                            etr_fname.insert(END, 'xxxx')
                        elif etr_lname.get() == '':
                            etr_lname.insert(END, 'xxxx')
                        elif etr_id.get() == '':
                            etr_id.insert(END, 'xxxx')
                        elif etr_contact.get() == '':
                            etr_contact.insert(END, 'xxxx@xxx.com')

                        else:
                            '''file_op = open("tenants_info.txt", "a")
                                file_op.write(entry_hse.get() + '|' + entry_f.get() + '|' + entry_l.get() + '|' + str(
                                    entry_id.get()) + '|' + entry_cont.get() + '\n')
                                file_op.close()'''
                            # save to database
                            conn = sqlite3.connect('Gracious_Data')
                            cur = conn.cursor()
                            cur.execute("""CREATE TABLE IF NOT EXISTS Apartment_Tenants
                                                (Apart_Name text,
                                                House_No text,
                                                First_Name text,
                                                Last_Name text,
                                                Id_No integer,
                                                Contact text)               
                                                """)
                            cur.execute(
                                "INSERT INTO Apartment_Tenants(Apart_Name,House_No,First_Name,Last_Name,Id_No,Contact) VALUES(?,?,?,?,?,?)",
                                (Hse.get(), hsNo.get(), etr_fname.get(), etr_lname.get(), etr_id.get(), etr_contact.get()))
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

                            cur.execute(
                                "SELECT House_No,First_Name, Last_Name, Id_No, Contact FROM Apartment_Tenants WHERE Apart_Name=?",
                                (house.get(),))
                            info = cur.fetchall()

                            line = 1
                            for hseno, fname, lname, idno, contact in info:
                                tree_ten.tag_configure('evenrow', background="white")
                                tree_ten.tag_configure('oddrow', background="lightblue")
                                if line % 2 == 0:
                                    tree_ten.insert(parent='', index='end', iid=str(line),
                                                    values=(hseno, fname, lname, idno, contact), tags=('evenrow',))
                                else:
                                    tree_ten.insert(parent='', index='end', iid=str(line),
                                                    values=(hseno, fname, lname, idno, contact), tags=('oddrow',))
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
                                tree_ten.item(selected, text='', values=(
                                etr_hsNo.get(), etr_fname.get(), etr_lname.get(), etr_id.get(), etr_contact.get()))

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

                            btn_reset = Button(frame_treeten, text="_Reset/Clear_", pady=10, command=resetField,
                                               activebackground="#ff6f69", activeforeground="#588c7e",
                                               font=("times", 10, "bold"), fg="blue", bg="pink")
                            btn_reset.grid(row=3, column=0, pady=10)
                            btn_editTree = Button(frame_treeten, text="Click On Record To Edit.", pady=10, command=EditSelected,
                                                  activebackground="#ff6f69", activeforeground="#588c7e",
                                                  font=("times", 10, "bold"), fg="blue", bg="pink")
                            btn_editTree.grid(row=3, column=1, pady=10)
                            btn_exitTree = Button(frame_treeten, text=" E_X_I_T ", pady=10, command=exitTree,
                                                  activebackground="#ff6f69", activeforeground="#588c7e",
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

                    btn_addtenant = Button(frm_MidCt, text="Add Tenant", background="#588c7e", fg="#ff6f69",
                                           activebackground="#ff6f69", activeforeground="#588c7e", font=("arial", 15, "bold"),
                                           command=AddTenant)
                    btn_addtenant.grid(row=2, column=0)
                    btn_exitenant = Button(frm_MidCt, text=" _E_X_I_T_ ", background="#588c7e", fg="#ff6f69",
                                           activebackground="#ff6f69",
                                           activeforeground="#588c7e", font=("arial", 15, "bold"),
                                           command=ExitTenant)
                    btn_exitenant.grid(row=2, column=1)

                    lbl_OutCb = Label(Lfrm_OutCb, text="Add/Update Water Meter_", bg="#ffcc5c", fg="#622569",
                                      font=("times", 10, "bold"))
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

                    conn = sqlite3.connect('Gracious_Data')
                    cur = conn.cursor()
                    cur.execute("SELECT House_No FROM Apartment_Tenants WHERE Apart_Name=?", (house.get(),))
                    c = cur.fetchall()
                    # print(c)
                    unitsInApt = []
                    for units in c:
                        unitsInApt.append(units)

                    hseNo = StringVar()
                    opt_hseNo = OptionMenu(Lfrm_InCb, hseNo, *unitsInApt)
                    opt_hseNo.grid(row=0, column=1, columnspan=2, padx=10, pady=2)
                    meter = StringVar()
                    etr_meter = Entry(Lfrm_InCb, textvariable=meter, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
                    etr_meter.grid(row=1, column=1, columnspan=2, padx=10, pady=2)
                    conn.commit()
                    conn.close()

                    def SaveMeter():
                        if hseNo.get() == '' or meter.get() == '':
                            messagebox.showerror('Empty Field', 'Must Select House No. And Fill In Meter No To Save!')


                        else:
                            conn = sqlite3.connect('Gracious_Data')
                            cur = conn.cursor()
                            cur.execute("""CREATE TABLE IF NOT EXISTS Apartment_MeterNo
                                                (Apart_Name text,
                                                 Hse_No text,
                                                 Meter_No text)
                                                """)
                            cur.execute("SELECT Apart_Name,Hse_No FROM Apartment_MeterNo WHERE Apart_Name=? AND Hse_No=?",
                                        (house.get(), hseNo.get()))
                            h = cur.fetchall()
                            cur.execute("SELECT Hse_No,Meter_No FROM Apartment_MeterNo WHERE Meter_No=? AND Apart_Name=?",
                                        (meter.get(), house.get()))
                            m = cur.fetchall()
                            if h:
                                que = messagebox.askyesno('Meter Record Already Exists For This House!',
                                                          'Would You Like To Edit Meter No. For This House?')
                                if que > 0:
                                    cur.execute("UPDATE Apartment_MeterNo SET Meter_No=? WHERE Hse_No=?",
                                                (meter.get(), hseNo.get()))
                                    print('Updated Successfully')
                                    hseNo.set('')
                                    etr_meter.delete(0, END)

                                    def lbl_suxUpMeterOut():
                                        lbl_suxUpMeter.grid_forget()

                                    lbl_suxUpMeter = Label(Lfrm_OutCb,
                                                           text=str(meter.get()) + " For " + str(
                                                               hseNo.get()) + " Updated Successfully.",
                                                           font=("times", 10), bg="#ffcc5c", fg="#622569")
                                    lbl_suxUpMeter.grid(row=2, column=0)
                                    lbl_suxUpMeter.after(3000, lbl_suxUpMeterOut)
                                else:
                                    print('Meter No. Not Updated')

                                    def lbl_suxNMeterOut():
                                        lbl_suxNMeter.grid_forget()

                                    lbl_suxNMeter = Label(Lfrm_OutCb,
                                                          text=str(meter.get()) + " For " + str(hseNo.get()) + " Not Updated.",
                                                          font=("times", 10), bg="#ffcc5c", fg="#622569")
                                    lbl_suxNMeter.grid(row=2, column=0)
                                    lbl_suxNMeter.after(3000, lbl_suxNMeterOut)
                            elif m:
                                messagebox.showerror('Meter No Already Exists In This Apartment!',
                                                     'Cannot Save This Meter No For This House')
                            else:
                                cur.execute("INSERT INTO Apartment_MeterNo VALUES(?,?,?)", (house.get(), hseNo.get(), meter.get()))
                                print('House Meter No Added Successfully')
                                hseNo.set('')
                                etr_meter.delete(0, END)

                                def lbl_suxMeterOut():
                                    lbl_suxMeter.grid_forget()

                                lbl_suxMeter = Label(Lfrm_OutCb,
                                                     text=str(meter.get()) + " For " + str(hseNo.get()) + " Added Successfully.",
                                                     font=("times", 10), bg="#ffcc5c", fg="#622569")
                                lbl_suxMeter.grid(row=2, column=0)
                                lbl_suxMeter.after(3000, lbl_suxMeterOut)
                            conn.commit()
                            conn.close()

                    btn_meter = Button(frm_MidCb, text="Save Meter", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                                       activeforeground="#588c7e", font=("arial", 15, "bold"),
                                       command=SaveMeter)
                    btn_meter.grid(row=2, column=0)
                    btn_exitmtr = Button(frm_MidCb, text=" _E_X_I_T_ ", background="#588c7e", fg="#ff6f69",
                                         activebackground="#ff6f69",
                                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                                         command=ExitMtr)
                    btn_exitmtr.grid(row=2, column=1)

    # ================================End Of Apartment Details==============================================================

                def hseLogin():
                    if house.get() == '':
                        messagebox.showerror('Apartment Not Selected', 'You Must Select Apartment')
                    else:
                        lbl_OutC = Label(Lfrm_OutCacc, text="Admin/User Log In", font=("times", 15, "bold"), bg="#ffcc5c",
                                         fg="#622569")
                        lbl_OutC.grid(row=0, column=0)
                        lbl_hsName = Label(Lfrm_InC, text="_User_Id_ : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                        lbl_hsName.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                        lbl_pass = Label(Lfrm_InC, text="_Password_: ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                        lbl_pass.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                        User_Name = StringVar()
                        etr_name = Entry(Lfrm_InC, textvariable=User_Name, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
                        etr_name.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                        password = StringVar()
                        etr_password = Entry(Lfrm_InC, textvariable=password, bg="#c1946a", fg="#622569",
                                             font=("times", 20, "bold"))
                        etr_password.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

                        def Validate():
                            if User_Name.get() == '' or password.get() == '':
                                messagebox.showerror('Empty Fields', 'User Id and Password Must Be Filled')
                            else:
                                conn = sqlite3.connect('Gracious_Data')
                                cur = conn.cursor()
                                cur.execute("SELECT Admin_Id, Password FROM Administrator WHERE Admin_id=? AND Password=?",(User_Name.get(), password.get()))
                                a = cur.fetchall()
                                #print(a)
                                cur.execute("SELECT * FROM User WHERE User_Id=? AND Password=?",(User_Name.get(), password.get()))
                                c = cur.fetchall()
                                if c or a:
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
                        btn_exitLog = Button(frm_MidC, text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                             activebackground="#ff6f69",
                                             activeforeground="#588c7e", font=("arial", 15, "bold"), command=ExitLog)
                        btn_exitLog.grid(row=1, column=1, pady=5)

                conn = sqlite3.connect('Gracious_Data')
                cur = conn.cursor()
                try:
                    cur.execute("SELECT * FROM Apartment")
                    c = cur.fetchall()
                    AptName = []
                    # print(c[0])
                    # print(c[1])
                    # count = 1
                    if c:
                        for name, location, units, floors in c:
                            AptName.append(name)
                        house = StringVar()
                        opt_select = OptionMenu(frm_MidL1, house, *AptName)
                        opt_select.grid(row=1, column=0, padx=20, pady=(5, 10))
                        btn_select = Button(Lfrm_OutL1acc, text="Select Apartment", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                            activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                                            command=hseLogin)
                        btn_select.grid(row=2, column=0)
                        conn.commit()
                        conn.close()
                    else:
                        pass
                except:
                    lbl_select = Label(Lfrm_OutL1acc, text="Go To Admin To Create Apartment", font=("times", 10), bg="#cfe0e8",
                                        fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised",
                                        borderwidth=1)
                    lbl_select.grid(row=3, column=0)

                def BackHome():
                    Lfrm_Outhpage.grid(row=2,column=2,padx=500,pady=50)
                    Lfrm_OutL1acc.grid_forget()
                    Lfrm_OutL2acc.grid_forget()
                    Lfrm_OutCacc.grid_forget()
                    frm_Rightacc.grid_forget()

                Lfrm_OutL2acc = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutL2acc.grid(row=2, column=0, padx=(5, 50), pady=50)
                frm_MidL2 = Frame(Lfrm_OutL2acc, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidL2.grid(padx=15, pady=15)
                Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InL2.grid()

                btn_InL2a = Button(Lfrm_InL2, text="B_A_C_K_HOME", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                                   command=BackHome)
                btn_InL2a.grid(padx=10, pady=10)
                btn_InL2b = Button(Lfrm_InL2, text="_C_a_r_e_t_a_k_e_r", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2b.grid(padx=10, pady=10)
                btn_InL2c = Button(Lfrm_InL2, text="_U_p_l_o_a_d_Image", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2c.grid(padx=10, pady=10)
                btn_InL2d = Button(Lfrm_InL2, text="_V_i_e_w_  _Houses", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2d.grid(padx=10, pady=10)
                btn_InL2e = Button(Lfrm_InL2, text="_A-g_e_n_t _Report", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2e.grid(padx=10, pady=10)

                frm_Rightacc = Frame(master, bg="#cfe0e8", padx=0, pady=0)
                frm_Rightacc.grid(row=1, column=4, rowspan=2, pady=(20, 10), padx=(20, 20))
                Lfrm_OutR1 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR1.grid(row=1, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR1 = Frame(Lfrm_OutR1, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR1.grid(padx=8, pady=8)
                Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR1.grid()
                btn_InR1 = Button(Lfrm_InR1, text="To Do List", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InR1.grid(padx=10, pady=10)

                Lfrm_OutR2 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR2.grid(row=2, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR2 = Frame(Lfrm_OutR2, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR2.grid(padx=8, pady=8)
                Lfrm_InR2 = LabelFrame(frm_MidR2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR2.grid()
                btn_InR2 = Button(Lfrm_InR2, text="Set Reminder", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InR2.grid(padx=10, pady=10)

                Lfrm_OutR3 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR3.grid(row=3, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR3 = Frame(Lfrm_OutR3, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR3.grid(padx=8, pady=8)
                Lfrm_InR3 = LabelFrame(frm_MidR3, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR3.grid()
                btn_InR3 = Button(Lfrm_InR3, text="Sticky Note", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InR3.grid(padx=10, pady=10)

                Lfrm_OutR4 = LabelFrame(frm_Rightacc, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR4.grid(row=4, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR4 = Frame(Lfrm_OutR4, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR4.grid(padx=8, pady=8)
                Lfrm_InR4 = LabelFrame(frm_MidR4, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR4.grid()
                btn_InR4 = Button(Lfrm_InR4, text="Tenant Box", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InR4.grid(padx=10, pady=10)


            def shrink():
                frm_house.configure(bg="#622569", padx=10, pady=10)

            def normal():
                btn_house.configure(font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569")
                btn_house.grid_configure(padx=5, pady=5)
                houseAccounts()

            frm_house.after(1000, shrink)
            btn_house.after(1000, normal)

        frm_house = Frame(Lfrm_In, bg="#622569", padx=10, pady=10)
        frm_house.grid(row=1, rowspan=2, columnspan=3, column=0, padx=10, pady=10)
        btn_house = Button(frm_house, text="H_o_u_s_e Accounts", font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569",
                           relief="raised", borderwidth=3, command=houseCommand)
        btn_house.grid(padx=5, pady=5)

        def billCommand():
            frm_bill.configure(bg="#ffcc5c", padx=0, pady=0)
            btn_bill.configure(font=("times", 40), bg="#ffcc5c", fg="#622569")
            btn_bill.grid_configure(padx=0, pady=0)
            def billManager():
                Lfrm_Outhpage.grid_forget()
                Lfrm_OutCwat = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=30)
                Lfrm_OutCwat.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                frm_MidC = Frame(Lfrm_OutCwat, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                frm_MidC.grid(row=1, column=0)
                Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC.grid(row=0, column=0, columnspan=2)

                '''Lfrm_OutC1 = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
                Lfrm_OutC1.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                frm_MidC1 = Frame(Lfrm_OutC1, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                frm_MidC1.grid(row=1, column=0)
                Lfrm_InC1 = LabelFrame(frm_MidC1, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC1.grid(row=0, column=0, columnspan=2)

                frm_MidC2 = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
                frm_MidC2.grid(row=1, column=0)
                Lfrm_InC2 = LabelFrame(frm_MidC2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC2.grid(row=0, column=0,columnspan=2)

                frm_MidC3 = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
                frm_MidC3.grid(row=0, column=0)
                Lfrm_InC3 = LabelFrame(frm_MidC3, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC3.grid(row=0, column=0,columnspan=2)

                Lfrm_OutC4 = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
                Lfrm_OutC4.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                frm_MidC4 = Frame(Lfrm_OutC4, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
                frm_MidC4.grid(row=1, column=0)
                Lfrm_InC4 = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC4.grid(row=1, column=0,columnspan=2)'''

                Lfrm_OutL1wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
                Lfrm_OutL1wat.grid(row=1, column=0, padx=(15, 50), pady=10)
                frm_MidL1 = Frame(Lfrm_OutL1wat, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidL1.grid(row=1, column=0, padx=60, pady=15)
                lbl_pageAd = Label(Lfrm_OutL1wat, text="View_ And_ Process_ Bills", bg="#ffcc5c", fg="#622569",
                                   font=("times", 18))
                lbl_pageAd.grid(row=0, column=0)
                conn = sqlite3.connect('Gracious_Data')
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS Water_Bills
                                                     (Apart_Name text,
                                                      House_No text,
                                                      Meter_No text,
                                                      Bil_Month text,
                                                      Bill_Date date,
                                                      Iss_Date date,
                                                      Due_Date date,
                                                      Previous integer,
                                                      Current integer,
                                                      Units integer,
                                                      Amount integer,
                                                      Year integer,
                                                      Month text,
                                                      Date_Time text)
                                                    """)
                cur.execute("""CREATE TABLE IF NOT EXISTS Prev_Readings
                                                       (Apart_Name text,
                                                        Previous integer)
                                                       """)
                conn.commit()
                conn.close()

                def HseLogin():
                    if housebill.get() == '':
                        messagebox.showerror('Apartment Not Selected', 'You Must Select Apartment')
                    else:
                        lbl_OutC = Label(Lfrm_OutCwat, text="Admin/User Log In", font=("times", 15, "bold"),
                                         bg="#ffcc5c", fg="#622569")
                        lbl_OutC.grid(row=0, column=0)
                        lbl_usid = Label(Lfrm_InC, text="_User_Id_ : ", bg="#ffcc5c", fg="#622569",
                                         font=("times", 10, "bold"))
                        lbl_usid.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                        lbl_passw = Label(Lfrm_InC, text="_Password_: ", bg="#ffcc5c", fg="#622569",
                                          font=("times", 10, "bold"))
                        lbl_passw.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

                        UserName = StringVar()
                        etr_usid = Entry(Lfrm_InC, textvariable=UserName, bg="#c1946a", fg="#622569",
                                         font=("times", 20, "bold"))
                        etr_usid.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                        passw = StringVar()
                        etr_passw = Entry(Lfrm_InC, textvariable=passw, bg="#c1946a", fg="#622569",
                                          font=("times", 20, "bold"), show='*')
                        etr_passw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

                        def BillDetails():
                            Lfrm_OutL1wat.grid_forget()
                            Lfrm_OutL2wat.grid_forget()
                            Lfrm_OutCwat.grid_forget()
                            Lfrm_OutR1wat.grid_forget()

                            conn = sqlite3.connect('Gracious_Data')
                            cur = conn.cursor()
                            cur.execute("SELECT Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?", (housebill.get(),))
                            c = cur.fetchall()
                            num = len(c)

                            Lfrm_OutL1Bd = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40,
                                                      pady=40)
                            Lfrm_OutL1Bd.grid(row=1, column=0, padx=(15, 50), pady=10)
                            frm_MidL1Bd = Frame(Lfrm_OutL1Bd, relief="raised", borderwidth=3, bg="#622569", padx=3,
                                                pady=3)
                            frm_MidL1Bd.grid(row=1, column=0, padx=60, pady=15)
                            lbl_pageAdBd = Label(Lfrm_OutL1Bd, text=housebill.get(), bg="#ffcc5c", fg="#622569",
                                                 font=("times", 18))
                            lbl_pageAdBd.grid(row=0, column=0)
                            lbl_pageAdBdnum = Label(Lfrm_OutL1Bd, text="Number of Meters: " + str(num), bg="#ffcc5c",
                                                    fg="#622569", font=("times", 10))
                            lbl_pageAdBdnum.grid(row=1, column=0)
                            conn.commit()
                            conn.close()

                            Lfrm_OutL2Bd = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10,
                                                      pady=10)
                            Lfrm_OutL2Bd.grid(row=2, column=0, padx=(5, 50), pady=50, rowspan=2)
                            frm_MidL2Bd = Frame(Lfrm_OutL2Bd, relief="raised", borderwidth=3, bg="#622569", padx=3,
                                                pady=3)
                            frm_MidL2Bd.grid(padx=15, pady=15)
                            Lfrm_InL2Bd = LabelFrame(frm_MidL2Bd, bg="#cfe0e8", padx=15, pady=20)
                            Lfrm_InL2Bd.grid()

                            Lfrm_OutCBd = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10,
                                                     pady=30)
                            Lfrm_OutCBd.grid(row=1, column=1, rowspan=3, columnspan=5, padx=20)
                            frm_MidCBd = Frame(Lfrm_OutCBd, relief="raised", borderwidth=5, bg="#622569", padx=10,
                                               pady=10)
                            frm_MidCBd.grid(row=1, column=0)
                            Lfrm_InCBd = LabelFrame(frm_MidCBd, bg="#cfe0e8", padx=15, pady=20)
                            Lfrm_InCBd.grid(row=0, column=0, columnspan=2)

                            def ProcessBills():
                                btn_InL2Bdview.configure(state=DISABLED)
                                btn_InL2BdPro.configure(state=DISABLED)
                                conn = sqlite3.connect('Gracious_Data')
                                cur = conn.cursor()
                                try:
                                    cur.execute("SELECT Hse_No,Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?",
                                            (housebill.get(),))
                                    c = cur.fetchall()
                                except:
                                    lb_select = Label(Lfrm_OutL1wat, text="Go To Admin To Create Apartment", font=("times", 10),
                                                        bg="#cfe0e8",fg="#622569", activebackground="#ff6f69",activeforeground="#588c7e",
                                                        relief="raised", borderwidth=1)
                                    lb_select.grid(row=2, column=0)
                                frm_readings = Frame(Lfrm_InCBd, bg="#622569", padx=5, pady=5)
                                frm_readings.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
                                lbl_hsnum = Label(frm_readings, text="House No", bg="#ffcc5c", fg="#622569",
                                                  font=("times", 10, "bold"))
                                lbl_hsnum.grid(row=0, column=1)
                                lbl_mtrnum = Label(frm_readings, text="Meter No", bg="#ffcc5c", fg="#622569",
                                                   font=("times", 10, "bold"))
                                lbl_mtrnum.grid(row=0, column=2)
                                lbl_prev = Label(frm_readings, text="Previous Reading", bg="#ffcc5c", fg="#622569",
                                                 font=("times", 10, "bold"))
                                lbl_prev.grid(row=0, column=3)
                                lbl_curr = Label(frm_readings, text="Current Reading", bg="#ffcc5c", fg="#622569",
                                                 font=("times", 10, "bold"))
                                lbl_curr.grid(row=0, column=4)

                                def Bilday():
                                    cal2.grid_forget()
                                    cal3.grid_forget()

                                    def Savebil():
                                        btn_bilday.configure(fg="green", bg="yellow")
                                        bil = str(cal1.get_date())
                                        lbl_bil.configure(text=bil)
                                        cal1.grid_forget()
                                        btn_cal1.grid_forget()
                                        btn_res1.grid_forget()

                                    def Resbil():
                                        lbl_bil.configure(text='')

                                    btn_bilday.configure(bg="green", fg="yellow")
                                    cal1.grid(row=1, column=1, columnspan=3)
                                    btn_cal1 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10),
                                                      command=Savebil)
                                    btn_cal1.grid(row=2, column=1)
                                    btn_res1 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue",
                                                      font=("arial", 10), command=Resbil)
                                    btn_res1.grid(row=2, column=2)

                                def Issday():
                                    cal1.grid_forget()
                                    cal3.grid_forget()

                                    def Saveiss():
                                        btn_issday.configure(fg="green", bg="yellow")
                                        iss = str(cal2.get_date())
                                        lbl_iss.configure(text=iss)
                                        cal2.grid_forget()
                                        btn_cal2.grid_forget()
                                        btn_res2.grid_forget()

                                    def Resiss():
                                        lbl_iss.configure(text='')

                                    btn_issday.configure(bg="green", fg="yellow")
                                    cal2.grid(row=1, column=1, columnspan=3)
                                    btn_cal2 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10),
                                                      command=Saveiss)
                                    btn_cal2.grid(row=2, column=1)
                                    btn_res2 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue",
                                                      font=("arial", 10), command=Resiss)
                                    btn_res2.grid(row=2, column=2)

                                def Dueday():
                                    cal1.grid_forget()
                                    cal2.grid_forget()

                                    def Savedue():
                                        btn_dueday.configure(fg="green", bg="yellow")
                                        due = str(cal3.get_date())
                                        lbl_due.configure(text=due)
                                        cal3.grid_forget()
                                        btn_cal3.grid_forget()
                                        btn_res3.grid_forget()

                                    def Resdue():
                                        lbl_due.configure(text='')

                                    btn_dueday.configure(bg="green", fg="yellow")
                                    cal3.grid(row=1, column=1, columnspan=3)
                                    btn_cal3 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10),
                                                      command=Savedue)
                                    btn_cal3.grid(row=2, column=1)
                                    btn_res3 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue",
                                                      font=("arial", 10), command=Resdue)
                                    btn_res3.grid(row=2, column=2)

                                Lfrm_cal = LabelFrame(frm_readings, bg="#ffcc5c", padx=10, pady=10, borderwidth=5)
                                Lfrm_cal.grid(row=1, column=0)
                                Lfrm_UnitEtr = LabelFrame(frm_readings, fg="#622569", bg="#ffcc5c", padx=10, pady=10)
                                Lfrm_UnitEtr.grid(row=2, column=0)
                                lbl_UnitEtr = Label(Lfrm_UnitEtr, text="Price Per Unit: ", bg="#ffcc5c", fg="#622569",
                                                    font=("times", 15))
                                lbl_UnitEtr.grid(row=0, column=0, padx=5, pady=10)
                                UnitEtr = IntVar()
                                etr_UnitEtr = Entry(Lfrm_UnitEtr, textvariable=UnitEtr, bg="#cfe0e8", fg="#622569",
                                                    font=("times", 10, "bold"), justify=RIGHT)
                                etr_UnitEtr.grid(row=0, column=1, padx=5, pady=10, columnspan=2)
                                etr_UnitEtr.delete(0, END)

                                Lfrm_opt = LabelFrame(Lfrm_cal, bg="#622569", padx=5, pady=5)
                                Lfrm_opt.grid(row=0, column=0, padx=5)
                                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
                                          'Dec']
                                lbl_mon = Label(Lfrm_opt, text="Month", bg="yellow", fg="green", font=("times", 10))
                                lbl_mon.grid(row=0, column=0, pady=1)
                                bilmon = StringVar()
                                opt_bilmon = OptionMenu(Lfrm_opt, bilmon, *months)
                                opt_bilmon.grid(row=1, column=0)

                                Lfrm_btn1 = LabelFrame(Lfrm_cal, bg="#622569", padx=3, pady=3)
                                Lfrm_btn1.grid(row=0, column=1, padx=5)
                                btn_bilday = Button(Lfrm_btn1, text="Bill Day", bg="yellow", fg="green",
                                                    activeforeground="yellow",
                                                    command=Bilday, font=("helvetica", 10, "bold"),
                                                    activebackground="green", relief="raised")
                                btn_bilday.grid(row=0, column=0)
                                lbl_bil = Label(Lfrm_btn1, text="", bg="#ffcc5c", fg="#622569", font=("times", 10))
                                lbl_bil.grid(row=1, column=0)
                                tex1 = datetime.datetime.today()
                                cal1 = Calendar(Lfrm_cal, selectmode="day", year=tex1.year, month=tex1.month,
                                                day=tex1.day)
                                cal1.grid_forget()
                                '''e, r, t = str(cal1.get_date()).split('/')
                                tq = int(t) + 2000
                                w = datetime.datetime(int(tq), int(e), int(r))
                                cal1floaty = w.strftime("%Y")
                                cal1floatw = w.strftime("%W")
                                cal1floatd = w.strftime("%d")
                                cal1floatj = w.strftime("%j")
                                cal1floatm = w.strftime("%m")
                                # print(w.strftime("%Y"))
                                # print(w.strftime("%W"))'''

                                Lfrm_btn2 = LabelFrame(Lfrm_cal, bg="#622569", padx=3, pady=3)
                                Lfrm_btn2.grid(row=0, column=2, padx=5)
                                btn_issday = Button(Lfrm_btn2, text="Issue Day", bg="yellow", fg="green",
                                                    activeforeground="yellow",
                                                    command=Issday, font=("helvetica", 10, "bold"),
                                                    activebackground="green", relief="raised")
                                btn_issday.grid(row=0, column=0)
                                lbl_iss = Label(Lfrm_btn2, text="", bg="#ffcc5c", fg="#622569", font=("times", 10))
                                lbl_iss.grid(row=1, column=0)
                                tex2 = datetime.datetime.today()
                                # datetime
                                cal2 = Calendar(Lfrm_cal, selectmode="day", year=tex2.year, month=tex2.month,
                                                day=tex2.day)
                                cal2.grid_forget()

                                Lfrm_btn3 = LabelFrame(Lfrm_cal, bg="#622569", padx=3, pady=3)
                                Lfrm_btn3.grid(row=0, column=3, padx=5)
                                btn_dueday = Button(Lfrm_btn3, text="Due Day", bg="yellow", fg="green",
                                                    activeforeground="yellow",
                                                    command=Dueday, font=("helvetica", 10, "bold"),
                                                    activebackground="green", relief="raised")
                                btn_dueday.grid(row=0, column=0)
                                lbl_due = Label(Lfrm_btn3, text="", bg="#ffcc5c", fg="#622569", font=("times", 10))
                                lbl_due.grid(row=1, column=0)
                                tex3 = datetime.datetime.today()
                                cal3 = Calendar(Lfrm_cal, selectmode="day", year=tex3.year, month=tex3.month,
                                                day=tex3.day)
                                cal3.grid_forget()

                                e, r, t = str(cal1.get_date()).split('/')
                                tq = int(t) + 2000
                                w = datetime.datetime(int(tq), int(e), int(r))
                                cal1floaty = w.strftime("%Y")
                                cal1floatw = w.strftime("%W")
                                cal1floatd = w.strftime("%d")
                                cal1floatj = w.strftime("%j")
                                cal1floatm = w.strftime("%m")
                                # print(w.strftime("%Y"))
                                # print(w.strftime("%W"))

                                u, g, k = str(cal2.get_date()).split('/')
                                ks = int(k) + 2000
                                s = datetime.datetime(int(ks), int(u), int(g))
                                cal2floaty = s.strftime("%Y")
                                cal2floatw = s.strftime("%W")
                                cal2floatd = s.strftime("%d")
                                cal2floatj = s.strftime("%j")
                                cal2floatm = s.strftime("%m")
                                # print(s.strftime("%Y"))
                                # print(s.strftime("%W"))

                                i, o, p = str(cal3.get_date()).split('/')
                                pd = int(p) + 2000
                                d = datetime.datetime(int(pd), int(i), int(o))
                                cal3floaty = d.strftime("%Y")
                                cal3floatw = d.strftime("%W")
                                cal3floatd = d.strftime("%d")
                                cal3floatj = d.strftime("%j")
                                cal3floatb = d.strftime("%b")
                                cal3floatm = d.strftime("%m")
                                # print(d.strftime("%Y"))
                                # print(d.strftime("%W"))
                                z = int(cal1floatm) - 1
                                a = int(cal3floaty) - 1

                                LFrm_readings = LabelFrame(frm_readings, bg="#cfe0e8", padx=5, pady=5, borderwidth=5)
                                LFrm_readings.grid(row=1, column=1, columnspan=4, padx=10)
                                con = sqlite3.connect('ProjoZ_SysAdminTest1')
                                br = con.cursor()
                                br.execute("SELECT Previous FROM Prev_Readings WHERE Apart_Name=?", (housebill.get(),))
                                bills = br.fetchall()
                                print(bills)
                                count = 0
                                Previous = []
                                Current = []
                                try:
                                    if bills:
                                        for hs, mtr in c:
                                            lbl_hs = Label(LFrm_readings, text=hs, bg="#ffcc5c", fg="#622569",
                                                           font=("times", 10, "bold"))
                                            lbl_hs.grid(row=count, column=0)
                                            lbl_mtr = Label(LFrm_readings, text=mtr, bg="#ffcc5c", fg="#622569",
                                                            font=("times", 10, "bold"))
                                            lbl_mtr.grid(row=count, column=1)
                                            Prev = IntVar()
                                            etr_prev = Entry(LFrm_readings, textvariable=Prev, bg="#c1946a",
                                                             fg="#622569", font=("times", 15, "bold"), justify=RIGHT)
                                            etr_prev.grid(row=count, column=2)
                                            try:
                                                etr_prev.insert(END, bills[count])
                                                etr_prev.configure(state=DISABLED)
                                            except:
                                                etr_prev.insert(END, '')
                                            Previous.append(etr_prev)
                                            Curr = IntVar()
                                            etr_curr = Entry(LFrm_readings, textvariable=Curr, bg="#c1946a",
                                                             fg="#622569",
                                                             font=("times", 15, "bold"), justify=RIGHT)
                                            etr_curr.grid(row=count, column=3)
                                            etr_curr.delete(0, END)
                                            Current.append(etr_curr)
                                            count += 1
                                    else:
                                        for hs, mtr in c:
                                            lbl_hs = Label(LFrm_readings, text=hs, bg="#ffcc5c", fg="#622569",
                                                           font=("times", 10, "bold"))
                                            lbl_hs.grid(row=count, column=0)
                                            lbl_mtr = Label(LFrm_readings, text=mtr, bg="#ffcc5c", fg="#622569",
                                                            font=("times", 10, "bold"))
                                            lbl_mtr.grid(row=count, column=1)
                                            Prev = IntVar()
                                            etr_prev = Entry(LFrm_readings, textvariable=Prev, bg="#c1946a",
                                                             fg="#622569", font=("times", 15, "bold"), justify=RIGHT)
                                            etr_prev.grid(row=count, column=2)
                                            etr_prev.delete(0, END)
                                            Previous.append(etr_prev)
                                            Curr = IntVar()
                                            etr_curr = Entry(LFrm_readings, textvariable=Curr, bg="#c1946a",
                                                             fg="#622569",
                                                             font=("times", 15, "bold"), justify=RIGHT)
                                            etr_curr.grid(row=count, column=3)
                                            etr_curr.delete(0, END)
                                            Current.append(etr_curr)
                                            count += 1
                                except:
                                    pass
                                con.commit()
                                con.close()
                                conn.commit()
                                conn.close()

                                '''elif cal2.get_date()< cal1.get_date() or cal3.get_date()<cal2.get_date():
                                                        messagebox.showerror('Invalid Date','Due Date Cannot Come Before\n Bill Or Issue Date')'''

                                '''# Printing the table
                                text_receipt = Text(Lfrm_readingsP, width=70, height=30, bg="#daebe8", fg="blue", font=("times",15,"bold"))
                                    text_receipt.grid(row=0,column=0,columnspan=11)

                                    text_receipt.insert(END,"__________________________________________________________________________________________")
                                    text_receipt.insert(END,"|  Bill Date  |\t Issue Date |\tDue Date |\tPrevious |\tCurrent |\t House No. |\tMeter No. |\tUnits |\tPrice |\tAmount|\n"
                                                           +"__________________________________________________________________________________________\n"
                                                           +"|   "+cal1.get_date()+"  "+"\t"+ "|    "+cal2.get_date()+"     "+"\t"+ " |    "+cal3.get_date()+"   "+"|\t"+ "   "+str(prev1.get())+"   "+"      |\t"
                                                           +"    "+str(curr1.get())+"  "+"  |\t\t"+str(apr[0])+" "+"|  \t"+str(mtr[0])+"\t"+"   |   "+str(unit1)+"    |\t"+"  "+str(price.get())
                                                           +"  |   "+"\t"+str(bill1)+"  |\n"
                                                           +"__________________________________________________________________________________________")

                                    scr_bar = ttk.Scrollbar(frame_text, orient=VERTICAL, command=text_receipt.yview)
                                    text_receipt['yscrollcommand'] =scr_bar.set
                                    scr_bar.grid(row=0,column=6, sticky="E")

                                    def print():
                                        text_receipt.grid_forget()
                                        btn_print.grid_forget()
                                        text_print = Text(frame_text, width=90, height=20, bg="#87bdd8", fg="blue",
                                                            font=("futura", 20, "bold"))
                                        text_print.grid(row=0, column=1, columnspan=5)

                                        text_print.insert(END,
                                                            "__________________________________________________________________________________________")
                                        text_print.insert(END,"|  Bill Date  |\t Issue Date |\tDue Date |\tPrevious |\tCurrent |\t House No. |\tMeter No. |\tUnits |\tPrice |\tAmount|\n"
                                                            + "__________________________________________________________________________________________\n"
                                                            + "|   " + cal.get_date() + "    " + "\t" + "|    " + cal1.get_date() + "     " + "\t" + " |    " + cal2.get_date() + "   " + "|\t" + "   " + str(prev1.get()) + "   " + "      |\t"
                                                            + "    " + str(curr1.get()) + "    " + "  |\t\t" + str(apr[0]) + " " + "|  \t" + str(mtr[0]) + "\t" + "   |   " + str(unit1) + "    |\t" + "  " + str(price.get())
                                                            + "  |   " + "\t" + str(bill1) + "  |\n"
                                                            + "__________________________________________________________________________________________")
                                        text_print.insert(END,"                        NB/Your supply shall be liable for disconnection if not settled within 5 days       "
                                                              "                                                                       from the date of issue without any further notice.     "
                                                              "                                                                                    In addition you will pay a reconnection fee of Kshs 1000")

                                        scr_bar = ttk.Scrollbar(frame_text, orient=VERTICAL, command=text_print.yview)
                                        text_print['yscrollcommand'] = scr_bar.set
                                        scr_bar.grid(row=0, column=6, sticky="E")

                                        text_print.configure(state='disabled')

                                        def docx():
                                            print_file = text_print.get("1.0","end-1c")
                                            filename = tempfile.mktemp(".doc")
                                            open(filename, "w").write(print_file)
                                            os.startfile(filename,"print")

                                        btn_docx = Button(frame_text, text="Print as DocX File", bg="yellow", fg="blue", relief="solid", anchor="se",command=docx, activebackground="green", activeforeground="purple" )
                                        btn_docx.grid(row=1, column=1)


                                    btn_print = Button(frame_text, text="Save and Print", bg="yellow", fg="blue", relief="solid", anchor="se",command=print, activebackground="green", activeforeground="purple" )
                                    btn_print.grid(row=1,column=1)'''

                                def readProcess():
                                    j = int(cal2floaty) - int(cal1floaty)
                                    f = int(cal3floaty) - int(cal1floaty)
                                    dtn = datetime.datetime.now()
                                    tz = dtn.strftime("%c")

                                    if bilmon.get() == '':
                                        messagebox.showerror('Month Not Selected', 'Select The Month Of The Bill.')
                                    if cal1floaty == cal2floaty == cal3floaty:
                                        if cal1floatj == cal2floatj == cal3floatj:
                                            messagebox.showerror('No Entry',
                                                                 'Fill All Entries Required To Process Bill.')
                                        elif cal1floatj > cal2floatj:
                                            messagebox.showerror('Invalid Date',
                                                                 'Bill Date Cannot Be Later Than Issue Date.')
                                        elif cal2floatj > cal3floatj:
                                            messagebox.showerror('Invalid Date',
                                                                 'Issue Date Cannot Be Later Than Due Date.')
                                        elif cal1floatj > cal3floatj:
                                            messagebox.showerror('Invalid Date',
                                                                 'Bill Date Cannot Be Later Than Due Date.')
                                    if cal1floaty < cal2floaty or cal1floaty < cal3floaty:
                                        if cal1floatm != str(12) or j > 1 or f > 1:
                                            messagebox.showerror('Invalid Date', 'Cannot Allow To Process This Bill.')
                                    if UnitEtr.get() == 0:
                                        messagebox.showerror('Missing Entry', 'Fill in Unit Price')
                                    else:
                                        conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                        cur = conn.cursor()
                                        cur.execute("SELECT Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?",
                                                    (housebill.get(),))
                                        c = cur.fetchall()
                                        cur.execute("SELECT Hse_No FROM Apartment_MeterNo WHERE Apart_Name=?",
                                                    (housebill.get(),))
                                        h = cur.fetchall()
                                        l = len(c)
                                        lbl_hsnum.grid_forget()
                                        lbl_mtrnum.grid_forget()
                                        lbl_prev.grid_forget()
                                        lbl_curr.grid_forget()
                                        Lfrm_cal.grid_forget()
                                        LFrm_readings.grid_forget()
                                        Lfrm_UnitEtr.grid_forget()
                                        btn_readProcess.grid_forget()
                                        LFrm_readingsE = LabelFrame(frm_readings, bg="#cfe0e8", padx=5, pady=5,
                                                                    borderwidth=5)
                                        LFrm_readingsE.grid(row=1, column=0, columnspan=11, padx=10)
                                        p = len(Previous)
                                        cr = len(Current)
                                        '''dayone = date.today().replace(day=1)
                                        daylastmon = dayone - timedelta(days=1)
                                        lastmon = daylastmon.strftime('%b')'''

                                        def printProcess():
                                            con = sqlite3.connect('ProjoZ_SysAdminTest1')
                                            cr = con.cursor()
                                            cr.execute("DELETE FROM Prev_Readings WHERE Apart_Name=?",
                                                       (housebill.get(),))

                                            LFrm_readingsE.grid_forget()
                                            # btn_readEdit.grid_forget()
                                            # btn_printProcess.grid_forget()
                                            btn_readExit.grid_forget()
                                            LFrm_readingsP = LabelFrame(frm_readings, bg="#cfe0e8", padx=5, pady=5,
                                                                        borderwidth=5)
                                            LFrm_readingsP.grid(row=1, column=0, columnspan=12, padx=10)

                                            # ===============================Text Area=================================================
                                            text_receipt = Text(LFrm_readingsP, width=56, bg="#daebe8", fg="blue",
                                                                font=("times", 15, "bold"))
                                            text_receipt.grid(row=0, column=0, columnspan=11)

                                            x = 0
                                            f = open(housebill.get() + bilmon.get() + str(tex1.year) + ".txt", 'w')
                                            fA = open(housebill.get() + bilmon.get() + str(tex1.year) + "agent.txt",
                                                      'w')
                                            fA.write("   " + housebill.get().upper() + " " + bilmon.get() + " " + str(
                                                tex1.year) + "\n")
                                            fA.write("|House No|Meter No|Previous|Current|Units|Amount|\n")
                                            for mtr in c:
                                                used = int(Current[x].get()) - int(Previous[x].get())
                                                usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                pvx = str(Previous[x].get())
                                                pvxE = str(prevEdit[x].get())
                                                cvx = str(Current[x].get())
                                                cvxE = str(currEdit[x].get())
                                                amt = used * UnitEtr.get()
                                                amtE = usedE * UnitEtr.get()
                                                if inRed:
                                                    text_receipt.insert(END, " House No.- " + str(
                                                        h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                                    text_receipt.insert(END,
                                                                        "_____________________________________________\n")
                                                    text_receipt.insert(END,
                                                                        "| Month | Bill Date | Issue Date | Due Date |\n")
                                                    text_receipt.insert(END,
                                                                        "------------------------------------------------\n")
                                                    text_receipt.insert(END,
                                                                        "|  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                                    text_receipt.insert(END,
                                                                        "_______________________________________________\n")
                                                    text_receipt.insert(END,
                                                                        "| Previous | Current | Units | Price | Amount |\n")
                                                    text_receipt.insert(END,
                                                                        "------------------------------------------------\n")
                                                    text_receipt.insert(END,
                                                                        "|     " + pvxE + "   |     " + cvxE + "  |    " + str(
                                                                            usedE) + "  |    " + str(
                                                                            etr_UnitEtr.get()) + " |   " + str(
                                                                            amtE) + "  |\n")
                                                    text_receipt.insert(END,
                                                                        "________________________________________________________\n\n\n\n\n")
                                                    cr.execute("SELECT Year,Month FROM Water_Bills WHERE Apart_Name=?",
                                                               (housebill.get(),))
                                                    ym = cr.fetchall()
                                                    existing = []
                                                    mas = datetime.datetime.now()
                                                    masaa = mas.strftime("%c")
                                                    mwaka = mas.strftime("%Y")
                                                    siku = mas.strftime("%j")
                                                    for yr, mt in ym:
                                                        if yr == cal3floaty and mt == cal3floatb:
                                                            existing.append(yr)
                                                    if existing:
                                                        messagebox.showerror('Existing Record',
                                                                             'The Bill for This Month And Year Already Exists\nWater Bill Once Processed Cannot Be Changed.')
                                                        print(existing)
                                                    if cal1floaty == mwaka:
                                                        if cal1floatj > siku:
                                                            messagebox.showerror('Invalid Date',
                                                                                 'Cannot Allow Processing Of Bill Due To Wrong Bill Date.')
                                                    else:
                                                        cr.execute(
                                                            "INSERT INTO Water_Bills VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                            (housebill.get(), str(h[x]), str(c[x]), bilmon.get(),
                                                             cal1.get_date(), cal2.get_date(), cal3.get_date(), pvxE,
                                                             cvxE, str(usedE), str(amtE), cal3floaty, cal3floatb, tz))
                                                        cr.execute("INSERT INTO Prev_Readings VALUES(?,?)",
                                                                   (housebill.get(), cvxE))
                                                        f.write(str(h[x]) + '-' + str(c[
                                                                                          x]) + '-' + bilmon.get() + '-' + cal1.get_date() + '-' + cal2.get_date() + '-' + cal3.get_date() + '-' + pvxE + '-' + cvxE + '-' + str(
                                                            usedE) + '-' + str(
                                                            amtE) + '-' + cal3floaty + '-' + cal3floatb + '-' + tz + '\n')
                                                        fA.write(str(h[x]) + ' | ' + str(
                                                            c[x]) + ' | ' + pvxE + ' | ' + cvxE + ' | ' + str(
                                                            usedE) + ' | ' + str(amtE) + '\n')
                                                        # print("Done 'n Dusted")
                                                else:
                                                    text_receipt.insert(END, " House No.- " + str(
                                                        h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                                    text_receipt.insert(END,
                                                                        "_____________________________________________\n")
                                                    text_receipt.insert(END,
                                                                        "| Month | Bill Date | Issue Date | Due Date |\n")
                                                    text_receipt.insert(END,
                                                                        "------------------------------------------------\n")
                                                    text_receipt.insert(END,
                                                                        "|  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                                    text_receipt.insert(END,
                                                                        "_______________________________________________\n")
                                                    text_receipt.insert(END,
                                                                        "| Previous | Current | Units | Price | Amount |\n")
                                                    text_receipt.insert(END,
                                                                        "------------------------------------------------\n")
                                                    text_receipt.insert(END,
                                                                        "|     " + pvx + "   |     " + cvx + "  |    " + str(
                                                                            used) + "  |    " + str(
                                                                            etr_UnitEtr.get()) + " |   " + str(
                                                                            amt) + "  |\n")
                                                    text_receipt.insert(END,
                                                                        "________________________________________________________\n\n\n\n\n")
                                                    cr.execute(
                                                        "INSERT INTO Water_Bills VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                        (housebill.get(), str(h[x]), str(c[x]), bilmon.get(),
                                                         cal1.get_date(), cal2.get_date(), cal3.get_date(), pvx, cvx,
                                                         str(used), str(amt), cal3floaty, cal3floatb, tz))
                                                    cr.execute("INSERT INTO Prev_Readings VALUES(?,?)",
                                                               (housebill.get(), cvx))
                                                    f.write(str(h[x]) + '-' + str(c[
                                                                                      x]) + '-' + bilmon.get() + '-' + cal1.get_date() + '-' + cal2.get_date() + '-' + cal3.get_date() + '-' + pvx + '-' + cvx + '-' + str(
                                                        used) + '-' + str() + '-' + cal3floaty + '-' + cal3floatb + '-' + tz + '\n')
                                                    fA.write(str(h[x]) + ' | ' + str(
                                                        c[x]) + ' | ' + pvx + ' | ' + cvx + ' | ' + str(
                                                        used) + ' | ' + str(amtE) + '\n')
                                                    # print("Done 'n Done")
                                                x += 1
                                            f.close()
                                            fA.close()
                                            con.commit()
                                            con.close()
                                            text_receipt.configure(state=DISABLED)

                                            scr_bar = ttk.Scrollbar(LFrm_readingsP, orient=VERTICAL,
                                                                    command=text_receipt.yview)
                                            text_receipt['yscrollcommand'] = scr_bar.set
                                            scr_bar.grid(row=0, column=11, sticky="E")

                                            def SaveForFiling():
                                                btn_printFile.grid_forget()
                                                btn_printProcessE.grid_forget()

                                                def sffOut():
                                                    lbl_sff.grid_forget()

                                                lbl_sff = Label(Lfrm_InCBd,
                                                                text="Saved Successfully! You Can Go To 'View Bills' To View.",
                                                                font=("times", 10, "bold"), bg="#ffcc5c", fg="#622569")
                                                lbl_sff.grid(row=1, column=1)
                                                lbl_sff.after(5000, sffOut)
                                                '''print_file = text_receipt.get("1.0", "end-1c")
                                                filename = open(housebill.get()+bilmon.get()+str(tex1.year)+".txt", 'w')
                                                filename.write(print_file+'\n')
                                                filename.close()
                                                pdf = tempfile.mktemp(".doc")
                                                open(pdf,"w").write(print_file)
                                                os.startfile(pdf, "print")
                                                btn_printFile.grid_forget()
                                                btn_printExit.grid_forget()'''

                                                def PrintForBilling():
                                                    btn_printBill.grid_forget()
                                                    btn_readProcess.grid_forget()
                                                    text_receipt.grid_forget()
                                                    scr_bar.grid_forget()
                                                    text_bills = Text(LFrm_readingsP, width=56, bg="#daebe8", fg="blue",
                                                                      font=("times", 15, "bold"))
                                                    text_bills.grid(row=0, column=0, columnspan=11)
                                                    inRed.clear()

                                                    x = 0
                                                    for mtr in c:
                                                        usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                        used = int(Current[x].get()) - int(Previous[x].get())
                                                        pvx = str(Previous[x].get())
                                                        pvxE = str(prevEdit[x].get())
                                                        cvx = str(Current[x].get())
                                                        cvxE = str(currEdit[x].get())
                                                        amt = used * UnitEtr.get()
                                                        amtE = usedE * UnitEtr.get()

                                                        if inRed:
                                                            text_bills.insert(END,
                                                                              "      " + housebill.get().upper() + "   APARTMENTS   \n")
                                                            text_bills.insert(END,
                                                                              "   ______________________________________________\n")
                                                            text_bills.insert(END, "    House No.- " + str(
                                                                h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "   | Month | Bill Date | Issue Date | Due Date |\n")
                                                            text_bills.insert(END,
                                                                              "   ------------------------------------------------\n")
                                                            text_bills.insert(END,
                                                                              "   |  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                                            text_bills.insert(END,
                                                                              "   _______________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "   | Previous | Current | Units | Price | Amount |\n")
                                                            text_bills.insert(END,
                                                                              "   ------------------------------------------------\n")
                                                            text_bills.insert(END,
                                                                              "   |     " + pvxE + "   |     " + cvxE + "  |    " + str(
                                                                                  usedE) + "  |    " + str(
                                                                                  etr_UnitEtr.get()) + " |   " + str(
                                                                                  amtE) + "  |\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "    NB/Your supply shall be liable for disconnection \n    if not settled within 5 days from the date of issue \n    without any further notice. \n   In addition you will pay a reconnection fee of Kshs 1000\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________________\n\n")
                                                        else:
                                                            text_bills.insert(END,
                                                                              "      " + housebill.get().upper() + "   APARTMENTS   \n")
                                                            text_bills.insert(END,
                                                                              "   ______________________________________________\n")
                                                            text_bills.insert(END, "    House No.- " + str(
                                                                h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "   | Month | Bill Date | Issue Date | Due Date |\n")
                                                            text_bills.insert(END,
                                                                              "   ------------------------------------------------\n")
                                                            text_bills.insert(END,
                                                                              "   |  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                                            text_bills.insert(END,
                                                                              "   _______________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "   | Previous | Current | Units | Price | Amount |\n")
                                                            text_bills.insert(END,
                                                                              "   ------------------------------------------------\n")
                                                            text_bills.insert(END,
                                                                              "   |  " + pvx + "   |     " + cvx + "  |    " + str(
                                                                                  used) + "  |    " + str(
                                                                                  etr_UnitEtr.get()) + " |   " + str(
                                                                                  amt) + "  |\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________________\n")
                                                            text_bills.insert(END,
                                                                              "    NB/Your supply shall be liable for disconnection \n    if not settled within 5 days from the date of issue \n    without any further notice. \n   In addition you will pay a reconnection fee of Kshs 1000\n")
                                                            text_bills.insert(END,
                                                                              "   _____________________________________________________\n\n")
                                                        x += 1
                                                    text_bills.configure(state=DISABLED)

                                                    scr_barB = ttk.Scrollbar(LFrm_readingsP, orient=VERTICAL,
                                                                             command=text_bills.yview)
                                                    text_bills['yscrollcommand'] = scr_barB.set
                                                    scr_barB.grid(row=0, column=11, sticky="E")

                                                    print_bill = text_bills.get("1.0", "end-1c")
                                                    pdfB = tempfile.mktemp(".doc")
                                                    open(pdfB, "w").write(print_bill)
                                                    os.startfile(pdfB, "print")
                                                    btn_printBill.grid_forget()

                                                def billExit():
                                                    frm_readings.grid_forget()
                                                    btn_InL2Bdview.configure(state=NORMAL)
                                                    btn_InL2BdPro.configure(state=NORMAL)

                                                btn_printBill = Button(frm_readings, text="Print Bills",
                                                                       background="#588c7e",
                                                                       fg="#ff6f69",
                                                                       command=PrintForBilling,
                                                                       activebackground="#ff6f69",
                                                                       activeforeground="#588c7e",
                                                                       font=("arial", 15, "bold"))
                                                btn_printBill.grid(row=2, column=3)
                                                btn_billExit = Button(frm_readings, text="E_X_I_T",
                                                                      background="#588c7e", fg="#ff6f69",
                                                                      command=billExit, activebackground="#ff6f69",
                                                                      activeforeground="#588c7e",
                                                                      font=("arial", 15, "bold"))
                                                btn_billExit.grid(row=2, column=4)

                                            def printExit():
                                                frm_readings.grid_forget()
                                                btn_InL2Bdview.configure(state=NORMAL)
                                                btn_InL2BdPro.configure(state=NORMAL)

                                            # =========================================================================================

                                            btn_printFile = Button(frm_readings, text="Save For Filing",
                                                                   background="#588c7e", fg="#ff6f69",
                                                                   command=SaveForFiling, activebackground="#ff6f69",
                                                                   activeforeground="#588c7e",
                                                                   font=("arial", 15, "bold"))
                                            btn_printFile.grid(row=2, column=3)
                                            btn_printExit = Button(frm_readings, text="E_X_I_T", background="#588c7e",
                                                                   fg="#ff6f69",
                                                                   command=printExit, activebackground="#ff6f69",
                                                                   activeforeground="#588c7e",
                                                                   font=("arial", 15, "bold"))
                                            btn_printExit.grid(row=2, column=4)

                                        if p == cr:
                                            x = 0
                                            msg = ''
                                            lbl_bilmon = Label(frm_readings, text="Month", bg="#ffcc5c", fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_bilmon.grid(row=0, column=0)

                                            lbl_bilday = Label(frm_readings, text="Bill_Day", bg="#ffcc5c",
                                                               fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_bilday.grid(row=0, column=1)

                                            lbl_issday = Label(frm_readings, text="Issue_Day", bg="#ffcc5c",
                                                               fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_issday.grid(row=0, column=2)

                                            lbl_dueday = Label(frm_readings, text="Due_ Day", bg="#ffcc5c",
                                                               fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_dueday.grid(row=0, column=3)

                                            lbl_hsnumP = Label(frm_readings, text="House_No", bg="#ffcc5c",
                                                               fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_hsnumP.grid(row=0, column=4)

                                            lbl_mtrnumP = Label(frm_readings, text="Meter_No", bg="#ffcc5c",
                                                                fg="#622569",
                                                                font=("times", 10, "bold"))
                                            lbl_mtrnumP.grid(row=0, column=5)

                                            lbl_PrevP = Label(frm_readings, text="Previous", bg="#ffcc5c", fg="#622569",
                                                              font=("times", 10, "bold"))
                                            lbl_PrevP.grid(row=0, column=6)

                                            lbl_currP = Label(frm_readings, text="Current", bg="#ffcc5c", fg="#622569",
                                                              font=("times", 10, "bold"))
                                            lbl_currP.grid(row=0, column=7)

                                            lbl_unitsP = Label(frm_readings, text="Units", bg="#ffcc5c", fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_unitsP.grid(row=0, column=8)

                                            lbl_PriceP = Label(frm_readings, text="Price", bg="#ffcc5c", fg="#622569",
                                                               font=("times", 10, "bold"))
                                            lbl_PriceP.grid(row=0, column=9)

                                            lbl_amountP = Label(frm_readings, text="Amount", bg="#ffcc5c", fg="#622569",
                                                                font=("times", 10, "bold"))
                                            lbl_amountP.grid(row=0, column=10)

                                            inRed = []
                                            prevEdit = []
                                            currEdit = []
                                            for mtr in c:
                                                try:
                                                    if Current[x].get() < Previous[x].get():
                                                        msg += str(Current[x].get()) + ' is less than ' + str(
                                                            Previous[x].get()) + '\n'
                                                        used = int(Current[x].get()) - int(Previous[x].get())
                                                        px = str(Previous[x].get())
                                                        cx = str(Current[x].get())
                                                        # print(used)
                                                        mon = tex1.month
                                                        amt = used * UnitEtr.get()
                                                        etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"), justify=RIGHT,
                                                                          width=10)
                                                        etr_Month.grid(row=x, column=0)
                                                        etr_Month.insert(END, bilmon.get())
                                                        etr_Month.configure(state=DISABLED)

                                                        etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"), justify=RIGHT,
                                                                         width=10)
                                                        etr_BilE.grid(row=x, column=1)
                                                        etr_BilE.insert(END, str(cal1.get_date()))
                                                        etr_BilE.configure(state=DISABLED)

                                                        etr_IssE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"),
                                                                         justify=RIGHT, width=10)
                                                        etr_IssE.grid(row=x, column=2)
                                                        etr_IssE.insert(END, str(cal2.get_date()))
                                                        etr_IssE.configure(state=DISABLED)

                                                        etr_DueE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"),
                                                                         justify=RIGHT, width=10)
                                                        etr_DueE.grid(row=x, column=3)
                                                        etr_DueE.insert(END, str(cal3.get_date()))
                                                        etr_DueE.configure(state=DISABLED)

                                                        etr_Hno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Hno.grid(row=x, column=4)
                                                        etr_Hno.insert(END, h[x])
                                                        etr_Hno.configure(state=DISABLED)

                                                        etr_Mno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Mno.grid(row=x, column=5)
                                                        etr_Mno.insert(END, c[x])
                                                        etr_Mno.configure(state=DISABLED)

                                                        etr_Pread = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Pread.grid(row=x, column=6)
                                                        etr_Pread.insert(END, px)
                                                        etr_Pread.configure(state=NORMAL)
                                                        prevEdit.append(etr_Pread)

                                                        etr_Cread = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Cread.grid(row=x, column=7)
                                                        etr_Cread.insert(END, cx)
                                                        etr_Cread.configure(state=NORMAL)
                                                        currEdit.append(etr_Cread)

                                                        etr_Qtt = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Qtt.grid(row=x, column=8)
                                                        etr_Qtt.insert(END, str(used))
                                                        etr_Qtt.configure(state=DISABLED)

                                                        etr_Price = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Price.grid(row=x, column=9)
                                                        etr_Price.insert(END, str(etr_UnitEtr.get()))
                                                        etr_Price.configure(state=DISABLED)

                                                        etr_Amount = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
                                                                           font=("times", 10, "bold"),
                                                                           justify=RIGHT, width=10)
                                                        etr_Amount.grid(row=x, column=10)
                                                        etr_Amount.insert(END, str(amt))
                                                        etr_Amount.configure(state=DISABLED)
                                                        print('Current Reading Cannot Be Less Than Previous: ' + msg)
                                                        inRed.append(Previous[x])
                                                    else:
                                                        usedE = int(Current[x].get()) - int(Previous[x].get())
                                                        px = str(Previous[x].get())
                                                        cx = str(Current[x].get())
                                                        # print(used)
                                                        mon = tex1.month
                                                        amtE = usedE * UnitEtr.get()
                                                        etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"), justify=RIGHT,
                                                                          width=10)
                                                        etr_Month.grid(row=x, column=0)
                                                        etr_Month.insert(END, bilmon.get())
                                                        etr_Month.configure(state=DISABLED)

                                                        etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"), justify=RIGHT,
                                                                         width=10)
                                                        etr_BilE.grid(row=x, column=1)
                                                        etr_BilE.insert(END, str(cal1.get_date()))
                                                        etr_BilE.configure(state=DISABLED)

                                                        etr_IssE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"),
                                                                         justify=RIGHT, width=10)
                                                        etr_IssE.grid(row=x, column=2)
                                                        etr_IssE.insert(END, str(cal2.get_date()))
                                                        etr_IssE.configure(state=DISABLED)

                                                        etr_DueE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                         font=("times", 10, "bold"),
                                                                         justify=RIGHT, width=10)
                                                        etr_DueE.grid(row=x, column=3)
                                                        etr_DueE.insert(END, str(cal3.get_date()))
                                                        etr_DueE.configure(state=DISABLED)

                                                        etr_Hno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Hno.grid(row=x, column=4)
                                                        etr_Hno.insert(END, h[x])
                                                        etr_Hno.configure(state=DISABLED)

                                                        etr_Mno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Mno.grid(row=x, column=5)
                                                        etr_Mno.insert(END, c[x])
                                                        etr_Mno.configure(state=DISABLED)

                                                        etr_Pread = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Pread.grid(row=x, column=6)
                                                        etr_Pread.insert(END, px)
                                                        etr_Pread.configure(state=DISABLED)
                                                        prevEdit.append(etr_Pread)

                                                        etr_Cread = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Cread.grid(row=x, column=7)
                                                        etr_Cread.insert(END, cx)
                                                        etr_Cread.configure(state=DISABLED)
                                                        currEdit.append(etr_Cread)

                                                        etr_Qtt = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                        font=("times", 10, "bold"),
                                                                        justify=RIGHT, width=10)
                                                        etr_Qtt.grid(row=x, column=8)
                                                        etr_Qtt.insert(END, str(usedE))
                                                        etr_Qtt.configure(state=DISABLED)

                                                        etr_Price = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                          font=("times", 10, "bold"),
                                                                          justify=RIGHT, width=10)
                                                        etr_Price.grid(row=x, column=9)
                                                        etr_Price.insert(END, str(etr_UnitEtr.get()))
                                                        etr_Price.configure(state=DISABLED)

                                                        etr_Amount = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                           font=("times", 10, "bold"),
                                                                           justify=RIGHT, width=10)
                                                        etr_Amount.grid(row=x, column=10)
                                                        etr_Amount.insert(END, str(amtE))
                                                        etr_Amount.configure(state=DISABLED)
                                                    x += 1
                                                except:
                                                    messagebox.showerror('Invalid Entry',
                                                                         'Insert "0" If Their Is No Reading On Current Meter No Or No Unit Price.')

                                            if inRed:
                                                inRed2 = []

                                                def readEdit():
                                                    x = 0
                                                    msgE = ''
                                                    for mtr in prevEdit:
                                                        try:
                                                            if currEdit[x].get() < prevEdit[x].get():
                                                                msgE += str(currEdit[x].get()) + ' is less than ' + str(
                                                                    prevEdit[x].get()) + '\n'
                                                                usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                                pvx = str(prevEdit[x].get())
                                                                cvx = str(currEdit[x].get())
                                                                # print(usedE)
                                                                mon = tex1.month
                                                                amtE = usedE * UnitEtr.get()
                                                                etr_Month = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Month.grid(row=x, column=0)
                                                                etr_Month.insert(END, bilmon.get())
                                                                etr_Month.configure(state=DISABLED)

                                                                etr_BilE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_BilE.grid(row=x, column=1)
                                                                etr_BilE.insert(END, str(cal1.get_date()))
                                                                etr_BilE.configure(state=DISABLED)

                                                                etr_IssE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_IssE.grid(row=x, column=2)
                                                                etr_IssE.insert(END, str(cal2.get_date()))
                                                                etr_IssE.configure(state=DISABLED)

                                                                etr_DueE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_DueE.grid(row=x, column=3)
                                                                etr_DueE.insert(END, str(cal3.get_date()))
                                                                etr_DueE.configure(state=DISABLED)

                                                                etr_Hno = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                fg="#622569",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Hno.grid(row=x, column=4)
                                                                etr_Hno.insert(END, h[x])
                                                                etr_Hno.configure(state=DISABLED)

                                                                etr_Mno = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                fg="#622569",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Mno.grid(row=x, column=5)
                                                                etr_Mno.insert(END, c[x])
                                                                etr_Mno.configure(state=DISABLED)

                                                                etr_Pread = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="red",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Pread.grid(row=x, column=6)
                                                                etr_Pread.insert(END, pvx)
                                                                etr_Pread.configure(state=NORMAL)
                                                                prevEdit.clear()
                                                                prevEdit.append(etr_Pread)

                                                                etr_Cread = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="red",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Cread.grid(row=x, column=7)
                                                                etr_Cread.insert(END, cvx)
                                                                etr_Cread.configure(state=NORMAL)
                                                                currEdit.clear()
                                                                currEdit.append(etr_Cread)

                                                                etr_Qtt = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Qtt.grid(row=x, column=8)
                                                                etr_Qtt.insert(END, str(usedE))
                                                                etr_Qtt.configure(state=NORMAL)

                                                                etr_Price = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Price.grid(row=x, column=9)
                                                                etr_Price.insert(END, str(etr_UnitEtr.get()))
                                                                etr_Price.configure(state=DISABLED)

                                                                etr_Amount = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                   fg="red",
                                                                                   font=("times", 10, "bold"),
                                                                                   justify=RIGHT, width=10)
                                                                etr_Amount.grid(row=x, column=10)
                                                                etr_Amount.insert(END, str(amtE))
                                                                etr_Amount.configure(state=NORMAL)
                                                                print(
                                                                    'Current Reading Cannot Be Less Than Previous: ' + msgE)
                                                                inRed2.append(currEdit[x])
                                                                btn_readEdit.grid_forget()
                                                            else:
                                                                usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                                pvx = str(prevEdit[x].get())
                                                                cvx = str(currEdit[x].get())
                                                                # print(used)
                                                                mon = tex1.month
                                                                amtE = usedE * UnitEtr.get()
                                                                etr_Month = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Month.grid(row=x, column=0)
                                                                etr_Month.insert(END, bilmon.get())
                                                                etr_Month.configure(state=DISABLED)

                                                                etr_BilE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_BilE.grid(row=x, column=1)
                                                                etr_BilE.insert(END, str(cal1.get_date()))
                                                                etr_BilE.configure(state=DISABLED)

                                                                etr_IssE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_IssE.grid(row=x, column=2)
                                                                etr_IssE.insert(END, str(cal2.get_date()))
                                                                etr_IssE.configure(state=DISABLED)

                                                                etr_DueE = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                 fg="#622569",
                                                                                 font=("times", 10, "bold"),
                                                                                 justify=RIGHT, width=10)
                                                                etr_DueE.grid(row=x, column=3)
                                                                etr_DueE.insert(END, str(cal3.get_date()))
                                                                etr_DueE.configure(state=DISABLED)

                                                                etr_Hno = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                fg="#622569",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Hno.grid(row=x, column=4)
                                                                etr_Hno.insert(END, h[x])
                                                                etr_Hno.configure(state=DISABLED)

                                                                etr_Mno = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                fg="#622569",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Mno.grid(row=x, column=5)
                                                                etr_Mno.insert(END, c[x])
                                                                etr_Mno.configure(state=DISABLED)

                                                                etr_Pread = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Pread.grid(row=x, column=6)
                                                                etr_Pread.insert(END, pvx)
                                                                etr_Pread.configure(state=DISABLED)

                                                                etr_Cread = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Cread.grid(row=x, column=7)
                                                                etr_Cread.insert(END, cvx)
                                                                etr_Cread.configure(state=DISABLED)

                                                                etr_Qtt = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                fg="#622569",
                                                                                font=("times", 10, "bold"),
                                                                                justify=RIGHT, width=10)
                                                                etr_Qtt.grid(row=x, column=8)
                                                                etr_Qtt.insert(END, str(usedE))
                                                                etr_Qtt.configure(state=DISABLED)

                                                                etr_Price = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                  fg="#622569",
                                                                                  font=("times", 10, "bold"),
                                                                                  justify=RIGHT, width=10)
                                                                etr_Price.grid(row=x, column=9)
                                                                etr_Price.insert(END, str(etr_UnitEtr.get()))
                                                                etr_Price.configure(state=DISABLED)

                                                                etr_Amount = Entry(LFrm_readingsE, bg="#c1946a",
                                                                                   fg="#622569",
                                                                                   font=("times", 10, "bold"),
                                                                                   justify=RIGHT, width=10)
                                                                etr_Amount.grid(row=x, column=10)
                                                                etr_Amount.insert(END, str(amtE))
                                                                etr_Amount.configure(state=DISABLED)

                                                            x += 1
                                                        except:
                                                            messagebox.showerror('Invalid Entry',
                                                                                 'Insert "0" If Their Is No Reading On Current Meter No Or No Unit Price.')
                                                    if inRed2:
                                                        pass
                                                    else:
                                                        btn_readEdit.grid_forget()
                                                        btn_printProcessE = Button(frm_readings, text="Process_ Bill",
                                                                                   background="#588c7e",
                                                                                   fg="#ff6f69",
                                                                                   command=printProcess,
                                                                                   activebackground="#ff6f69",
                                                                                   activeforeground="#588c7e",
                                                                                   font=("arial", 15, "bold"))
                                                        btn_printProcessE.grid(row=2, column=3)

                                                btn_readEdit = Button(frm_readings, text="E_D_I_T",
                                                                      background="#588c7e", fg="#ff6f69",
                                                                      command=readEdit, activebackground="#ff6f69",
                                                                      activeforeground="#588c7e",
                                                                      font=("arial", 15, "bold"))
                                                btn_readEdit.grid(row=2, column=2)
                                            else:
                                                btn_printProcessE = Button(frm_readings, text="Process_ Bill",
                                                                           background="#588c7e",
                                                                           fg="#ff6f69",
                                                                           command=printProcess,
                                                                           activebackground="#ff6f69",
                                                                           activeforeground="#588c7e",
                                                                           font=("arial", 15, "bold"))
                                                btn_printProcessE.grid(row=2, column=3)

                                                # print(Previous[0].get())
                                                # print(Current[0].get()
                                        conn.commit()
                                        conn.close()

                                        '''if p == cr:
                                           elif etr_prev.get()>etr_curr.get():
                                                messagebox.showerror('Invalid Entry','Current Reading Cannot Be Less Than Previous Reading')'''
                                        '''else:
                                                etr_prev.configure(state=DISABLED)
                                                etr_curr.configure(state=DISABLED)
                                                used = Curr.get() - Prev.get()
                                                print(used)

                                        else:
                                            messagebox.showerror('No Meters','Cannot Process Bills')'''

                                def readExit():
                                    frm_readings.grid_forget()
                                    LFrm_readings.grid_forget()
                                    btn_readProcess.grid_forget()
                                    btn_readExit.grid_forget()
                                    btn_InL2Bdview.configure(state=NORMAL)
                                    btn_InL2BdPro.configure(state=NORMAL)

                                btn_readProcess = Button(frm_readings, text="Process_ Bill", background="#588c7e",
                                                         fg="#ff6f69",
                                                         command=readProcess, activebackground="#ff6f69",
                                                         activeforeground="#588c7e",
                                                         font=("arial", 15, "bold"))
                                btn_readProcess.grid(row=2, column=3)
                                btn_readExit = Button(frm_readings, text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                                      command=readExit,
                                                      activebackground="#ff6f69", activeforeground="#588c7e",
                                                      font=("arial", 15, "bold"))
                                btn_readExit.grid(row=2, column=4)

                            def BackSelect():
                                Lfrm_OutL1Bd.grid_forget()
                                Lfrm_OutL2Bd.grid_forget()
                                Lfrm_OutCBd.grid_forget()
                                Lfrm_OutL1wat.grid(row=1, column=0, padx=(15, 50), pady=10)
                                Lfrm_OutL2wat.grid(row=2, column=0, padx=(5, 50), pady=50)
                                Lfrm_OutCwat.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                                Lfrm_OutR1wat.grid(row=1, column=4, padx=(10, 20), pady=(20, 10))

                            def ViewBills():
                                btn_InL2Bdview.configure(state=DISABLED)
                                btn_InL2BdPro.configure(state=DISABLED)
                                Lfrm_Vbills = LabelFrame(Lfrm_InCBd, relief="raised", borderwidth=3, bg="#622569",
                                                         padx=5, pady=5)
                                Lfrm_Vbills.grid(row=1, column=0)
                                lbl_nodata = Label(Lfrm_Vbills, text="No Data Available For Selected Year And Month",
                                                   bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
                                lbl_nodata.grid_forget()
                                janlist = []
                                feblist = []
                                marlist = []
                                aprlist = []
                                maylist = []
                                junlist = []
                                jullist = []
                                auglist = []
                                seplist = []
                                octlist = []
                                novlist = []
                                declist = []

                                # ===============================Jan===============Button====================================================================================================================================
                                def jan():
                                    janlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_jan.configure(bg="green", fg="yellow")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")

                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Jan'))
                                    vjan = cur.fetchall()
                                    janlist.append(vjan)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vjan = ttk.Treeview(Lfrm_Vbills)
                                    tree_vjan.grid(row=1, column=2)
                                    tree_vjan['columns'] = (
                                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                    'amount')
                                    tree_vjan.column('#0', stretch=NO, width=0)
                                    tree_vjan.column('n', anchor=CENTER, width=20)
                                    tree_vjan.column('hsno', anchor=CENTER, width=60)
                                    tree_vjan.column('mtrno', anchor=CENTER, width=60)
                                    tree_vjan.column('bilm', anchor=CENTER, width=60)
                                    tree_vjan.column('billd', anchor=CENTER, width=60)
                                    tree_vjan.column('issd', anchor=CENTER, width=60)
                                    tree_vjan.column('dued', anchor=CENTER, width=60)
                                    tree_vjan.column('prev', anchor=CENTER, width=60)
                                    tree_vjan.column('curr', anchor=CENTER, width=60)
                                    tree_vjan.column('units', anchor=CENTER, width=60)
                                    tree_vjan.column('amount', anchor=CENTER, width=60)

                                    tree_vjan.heading('#0', text='')
                                    tree_vjan.heading('n', text='')
                                    tree_vjan.heading('hsno', text='House No')
                                    tree_vjan.heading('mtrno', text='Meter No')
                                    tree_vjan.heading('bilm', text='Month')
                                    tree_vjan.heading('billd', text='Bill Date')
                                    tree_vjan.heading('issd', text='Issue Date')
                                    tree_vjan.heading('dued', text='Due Date')
                                    tree_vjan.heading('prev', text='Previous')
                                    tree_vjan.heading('curr', text='Current')
                                    tree_vjan.heading('units', text='Units')
                                    tree_vjan.heading('amount', text='Amount')
                                    if janlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vjan:
                                            tree_vjan.tag_configure('evenrow', background="white")
                                            tree_vjan.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vjan.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vjan.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vjan.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # =================================Feb===============Button==============================================================================================================================
                                def feb():
                                    feblist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_feb.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), ''))
                                    vfeb = cur.fetchall()
                                    feblist.append(vfeb)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vfeb = ttk.Treeview(Lfrm_Vbills)
                                    tree_vfeb.grid(row=1, column=2)
                                    tree_vfeb['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vfeb.column('#0', stretch=NO, width=0)
                                    tree_vfeb.column('n', anchor=CENTER, width=20)
                                    tree_vfeb.column('hsno', anchor=CENTER, width=60)
                                    tree_vfeb.column('mtrno', anchor=CENTER, width=60)
                                    tree_vfeb.column('bilm', anchor=CENTER, width=60)
                                    tree_vfeb.column('billd', anchor=CENTER, width=60)
                                    tree_vfeb.column('issd', anchor=CENTER, width=60)
                                    tree_vfeb.column('dued', anchor=CENTER, width=60)
                                    tree_vfeb.column('prev', anchor=CENTER, width=60)
                                    tree_vfeb.column('curr', anchor=CENTER, width=60)
                                    tree_vfeb.column('units', anchor=CENTER, width=60)
                                    tree_vfeb.column('amount', anchor=CENTER, width=60)

                                    tree_vfeb.heading('#0', text='')
                                    tree_vfeb.heading('n', text='')
                                    tree_vfeb.heading('hsno', text='House No')
                                    tree_vfeb.heading('mtrno', text='Meter No')
                                    tree_vfeb.heading('bilm', text='Month')
                                    tree_vfeb.heading('billd', text='Bill Date')
                                    tree_vfeb.heading('issd', text='Issue Date')
                                    tree_vfeb.heading('dued', text='Due Date')
                                    tree_vfeb.heading('prev', text='Previous')
                                    tree_vfeb.heading('curr', text='Current')
                                    tree_vfeb.heading('units', text='Units')
                                    tree_vfeb.heading('amount', text='Amount')
                                    if feblist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vfeb:
                                            tree_vfeb.tag_configure('evenrow', background="white")
                                            tree_vfeb.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vfeb.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vfeb.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vfeb.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ==================================March====================Button==========================================================================================================
                                def mar():
                                    marlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_mar.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Mar'))
                                    vmar = cur.fetchall()
                                    marlist.append(vmar)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vmar = ttk.Treeview(Lfrm_Vbills)
                                    tree_vmar.grid(row=1, column=2)
                                    tree_vmar['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vmar.column('#0', stretch=NO, width=0)
                                    tree_vmar.column('n', anchor=CENTER, width=20)
                                    tree_vmar.column('hsno', anchor=CENTER, width=60)
                                    tree_vmar.column('mtrno', anchor=CENTER, width=60)
                                    tree_vmar.column('bilm', anchor=CENTER, width=60)
                                    tree_vmar.column('billd', anchor=CENTER, width=60)
                                    tree_vmar.column('issd', anchor=CENTER, width=60)
                                    tree_vmar.column('dued', anchor=CENTER, width=60)
                                    tree_vmar.column('prev', anchor=CENTER, width=60)
                                    tree_vmar.column('curr', anchor=CENTER, width=60)
                                    tree_vmar.column('units', anchor=CENTER, width=60)
                                    tree_vmar.column('amount', anchor=CENTER, width=60)

                                    tree_vmar.heading('#0', text='')
                                    tree_vmar.heading('n', text='')
                                    tree_vmar.heading('hsno', text='House No')
                                    tree_vmar.heading('mtrno', text='Meter No')
                                    tree_vmar.heading('bilm', text='Month')
                                    tree_vmar.heading('billd', text='Bill Date')
                                    tree_vmar.heading('issd', text='Issue Date')
                                    tree_vmar.heading('dued', text='Due Date')
                                    tree_vmar.heading('prev', text='Previous')
                                    tree_vmar.heading('curr', text='Current')
                                    tree_vmar.heading('units', text='Units')
                                    tree_vmar.heading('amount', text='Amount')
                                    if marlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vmar:
                                            tree_vmar.tag_configure('evenrow', background="white")
                                            tree_vmar.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vmar.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vmar.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vmar.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ==============================April===============But=======================================================================================================================
                                def apr():
                                    aprlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_apr.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Apr'))
                                    vapr = cur.fetchall()
                                    aprlist.append(vapr)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vapr = ttk.Treeview(Lfrm_Vbills)
                                    tree_vapr.grid(row=1, column=2)
                                    tree_vapr['columns'] = (
                                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                    'amount')
                                    tree_vapr.column('#0', stretch=NO, width=0)
                                    tree_vapr.column('n', anchor=CENTER, width=20)
                                    tree_vapr.column('hsno', anchor=CENTER, width=60)
                                    tree_vapr.column('mtrno', anchor=CENTER, width=60)
                                    tree_vapr.column('bilm', anchor=CENTER, width=60)
                                    tree_vapr.column('billd', anchor=CENTER, width=60)
                                    tree_vapr.column('issd', anchor=CENTER, width=60)
                                    tree_vapr.column('dued', anchor=CENTER, width=60)
                                    tree_vapr.column('prev', anchor=CENTER, width=60)
                                    tree_vapr.column('curr', anchor=CENTER, width=60)
                                    tree_vapr.column('units', anchor=CENTER, width=60)
                                    tree_vapr.column('amount', anchor=CENTER, width=60)

                                    tree_vapr.heading('#0', text='')
                                    tree_vapr.heading('n', text='')
                                    tree_vapr.heading('hsno', text='House No')
                                    tree_vapr.heading('mtrno', text='Meter No')
                                    tree_vapr.heading('bilm', text='Month')
                                    tree_vapr.heading('billd', text='Bill Date')
                                    tree_vapr.heading('issd', text='Issue Date')
                                    tree_vapr.heading('dued', text='Due Date')
                                    tree_vapr.heading('prev', text='Previous')
                                    tree_vapr.heading('curr', text='Current')
                                    tree_vapr.heading('units', text='Units')
                                    tree_vapr.heading('amount', text='Amount')
                                    if aprlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vapr:
                                            tree_vapr.tag_configure('evenrow', background="white")
                                            tree_vapr.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vapr.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vapr.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vapr.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ==================================May==================But=====================================================================================================================
                                def may():
                                    maylist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_may.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'May'))
                                    vmay = cur.fetchall()
                                    maylist.append(vmay)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vmay = ttk.Treeview(Lfrm_Vbills)
                                    tree_vmay.grid(row=1, column=2)
                                    tree_vmay['columns'] = (
                                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                    'amount')
                                    tree_vmay.column('#0', stretch=NO, width=0)
                                    tree_vmay.column('n', anchor=CENTER, width=20)
                                    tree_vmay.column('hsno', anchor=CENTER, width=60)
                                    tree_vmay.column('mtrno', anchor=CENTER, width=60)
                                    tree_vmay.column('bilm', anchor=CENTER, width=60)
                                    tree_vmay.column('billd', anchor=CENTER, width=60)
                                    tree_vmay.column('issd', anchor=CENTER, width=60)
                                    tree_vmay.column('dued', anchor=CENTER, width=60)
                                    tree_vmay.column('prev', anchor=CENTER, width=60)
                                    tree_vmay.column('curr', anchor=CENTER, width=60)
                                    tree_vmay.column('units', anchor=CENTER, width=60)
                                    tree_vmay.column('amount', anchor=CENTER, width=60)

                                    tree_vmay.heading('#0', text='')
                                    tree_vmay.heading('n', text='')
                                    tree_vmay.heading('hsno', text='House No')
                                    tree_vmay.heading('mtrno', text='Meter No')
                                    tree_vmay.heading('bilm', text='Month')
                                    tree_vmay.heading('billd', text='Bill Date')
                                    tree_vmay.heading('issd', text='Issue Date')
                                    tree_vmay.heading('dued', text='Due Date')
                                    tree_vmay.heading('prev', text='Previous')
                                    tree_vmay.heading('curr', text='Current')
                                    tree_vmay.heading('units', text='Units')
                                    tree_vmay.heading('amount', text='Amount')
                                    if maylist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vmay:
                                            tree_vmay.tag_configure('evenrow', background="white")
                                            tree_vmay.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vmay.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vmay.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vmay.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # =============================================June=================But===================================================================================================================
                                def jun():
                                    junlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_jun.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Jun'))
                                    vjun = cur.fetchall()
                                    junlist.append(vjun)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vjun = ttk.Treeview(Lfrm_Vbills)
                                    tree_vjun.grid(row=1, column=2)
                                    tree_vjun['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vjun.column('#0', stretch=NO, width=0)
                                    tree_vjun.column('n', anchor=CENTER, width=20)
                                    tree_vjun.column('hsno', anchor=CENTER, width=60)
                                    tree_vjun.column('mtrno', anchor=CENTER, width=60)
                                    tree_vjun.column('bilm', anchor=CENTER, width=60)
                                    tree_vjun.column('billd', anchor=CENTER, width=60)
                                    tree_vjun.column('issd', anchor=CENTER, width=60)
                                    tree_vjun.column('dued', anchor=CENTER, width=60)
                                    tree_vjun.column('prev', anchor=CENTER, width=60)
                                    tree_vjun.column('curr', anchor=CENTER, width=60)
                                    tree_vjun.column('units', anchor=CENTER, width=60)
                                    tree_vjun.column('amount', anchor=CENTER, width=60)

                                    tree_vjun.heading('#0', text='')
                                    tree_vjun.heading('n', text='')
                                    tree_vjun.heading('hsno', text='House No')
                                    tree_vjun.heading('mtrno', text='Meter No')
                                    tree_vjun.heading('bilm', text='Month')
                                    tree_vjun.heading('billd', text='Bill Date')
                                    tree_vjun.heading('issd', text='Issue Date')
                                    tree_vjun.heading('dued', text='Due Date')
                                    tree_vjun.heading('prev', text='Previous')
                                    tree_vjun.heading('curr', text='Current')
                                    tree_vjun.heading('units', text='Units')
                                    tree_vjun.heading('amount', text='Amount')
                                    if junlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vjun:
                                            tree_vjun.tag_configure('evenrow', background="white")
                                            tree_vjun.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vjun.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vjun.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vjun.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # =================================July==================But=================================================================================================================
                                def jul():
                                    jullist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_jul.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Jul'))
                                    vjul = cur.fetchall()
                                    jullist.append(vjul)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vjul = ttk.Treeview(Lfrm_Vbills)
                                    tree_vjul.grid(row=1, column=2)
                                    tree_vjul['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vjul.column('#0', stretch=NO, width=0)
                                    tree_vjul.column('n', anchor=CENTER, width=20)
                                    tree_vjul.column('hsno', anchor=CENTER, width=60)
                                    tree_vjul.column('mtrno', anchor=CENTER, width=60)
                                    tree_vjul.column('bilm', anchor=CENTER, width=60)
                                    tree_vjul.column('billd', anchor=CENTER, width=60)
                                    tree_vjul.column('issd', anchor=CENTER, width=60)
                                    tree_vjul.column('dued', anchor=CENTER, width=60)
                                    tree_vjul.column('prev', anchor=CENTER, width=60)
                                    tree_vjul.column('curr', anchor=CENTER, width=60)
                                    tree_vjul.column('units', anchor=CENTER, width=60)
                                    tree_vjul.column('amount', anchor=CENTER, width=60)

                                    tree_vjul.heading('#0', text='')
                                    tree_vjul.heading('n', text='')
                                    tree_vjul.heading('hsno', text='House No')
                                    tree_vjul.heading('mtrno', text='Meter No')
                                    tree_vjul.heading('bilm', text='Month')
                                    tree_vjul.heading('billd', text='Bill Date')
                                    tree_vjul.heading('issd', text='Issue Date')
                                    tree_vjul.heading('dued', text='Due Date')
                                    tree_vjul.heading('prev', text='Previous')
                                    tree_vjul.heading('curr', text='Current')
                                    tree_vjul.heading('units', text='Units')
                                    tree_vjul.heading('amount', text='Amount')
                                    if jullist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vjul:
                                            tree_vjul.tag_configure('evenrow', background="white")
                                            tree_vjul.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vjul.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vjul.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vjul.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ================================Aug===================But====================================================================================================================
                                def aug():
                                    auglist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_aug.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Aug'))
                                    vaug = cur.fetchall()
                                    auglist.append(vaug)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vaug = ttk.Treeview(Lfrm_Vbills)
                                    tree_vaug.grid(row=1, column=2)
                                    tree_vaug['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vaug.column('#0', stretch=NO, width=0)
                                    tree_vaug.column('n', anchor=CENTER, width=20)
                                    tree_vaug.column('hsno', anchor=CENTER, width=60)
                                    tree_vaug.column('mtrno', anchor=CENTER, width=60)
                                    tree_vaug.column('bilm', anchor=CENTER, width=60)
                                    tree_vaug.column('billd', anchor=CENTER, width=60)
                                    tree_vaug.column('issd', anchor=CENTER, width=60)
                                    tree_vaug.column('dued', anchor=CENTER, width=60)
                                    tree_vaug.column('prev', anchor=CENTER, width=60)
                                    tree_vaug.column('curr', anchor=CENTER, width=60)
                                    tree_vaug.column('units', anchor=CENTER, width=60)
                                    tree_vaug.column('amount', anchor=CENTER, width=60)

                                    tree_vaug.heading('#0', text='')
                                    tree_vaug.heading('n', text='')
                                    tree_vaug.heading('hsno', text='House No')
                                    tree_vaug.heading('mtrno', text='Meter No')
                                    tree_vaug.heading('bilm', text='Month')
                                    tree_vaug.heading('billd', text='Bill Date')
                                    tree_vaug.heading('issd', text='Issue Date')
                                    tree_vaug.heading('dued', text='Due Date')
                                    tree_vaug.heading('prev', text='Previous')
                                    tree_vaug.heading('curr', text='Current')
                                    tree_vaug.heading('units', text='Units')
                                    tree_vaug.heading('amount', text='Amount')
                                    if auglist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vaug:
                                            tree_vaug.tag_configure('evenrow', background="white")
                                            tree_vaug.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vaug.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vaug.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vaug.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ============================================September=======But============================================================================================================
                                def sep():
                                    seplist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_sep.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Sep'))
                                    vsep = cur.fetchall()
                                    seplist.append(vsep)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vsep = ttk.Treeview(Lfrm_Vbills)
                                    tree_vsep.grid(row=1, column=2)
                                    tree_vsep['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vsep.column('#0', stretch=NO, width=0)
                                    tree_vsep.column('n', anchor=CENTER, width=20)
                                    tree_vsep.column('hsno', anchor=CENTER, width=60)
                                    tree_vsep.column('mtrno', anchor=CENTER, width=60)
                                    tree_vsep.column('bilm', anchor=CENTER, width=60)
                                    tree_vsep.column('billd', anchor=CENTER, width=60)
                                    tree_vsep.column('issd', anchor=CENTER, width=60)
                                    tree_vsep.column('dued', anchor=CENTER, width=60)
                                    tree_vsep.column('prev', anchor=CENTER, width=60)
                                    tree_vsep.column('curr', anchor=CENTER, width=60)
                                    tree_vsep.column('units', anchor=CENTER, width=60)
                                    tree_vsep.column('amount', anchor=CENTER, width=60)

                                    tree_vsep.heading('#0', text='')
                                    tree_vsep.heading('n', text='')
                                    tree_vsep.heading('hsno', text='House No')
                                    tree_vsep.heading('mtrno', text='Meter No')
                                    tree_vsep.heading('bilm', text='Month')
                                    tree_vsep.heading('billd', text='Bill Date')
                                    tree_vsep.heading('issd', text='Issue Date')
                                    tree_vsep.heading('dued', text='Due Date')
                                    tree_vsep.heading('prev', text='Previous')
                                    tree_vsep.heading('curr', text='Current')
                                    tree_vsep.heading('units', text='Units')
                                    tree_vsep.heading('amount', text='Amount')
                                    if seplist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vsep:
                                            tree_vsep.tag_configure('evenrow', background="white")
                                            tree_vsep.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vsep.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vsep.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vsep.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ==================================October==================But==================================================================================================================
                                def oct():
                                    octlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_oct.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Oct'))
                                    voct = cur.fetchall()
                                    octlist.append(voct)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_voct = ttk.Treeview(Lfrm_Vbills)
                                    tree_voct.grid(row=1, column=2)
                                    tree_voct['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_voct.column('#0', stretch=NO, width=0)
                                    tree_voct.column('n', anchor=CENTER, width=20)
                                    tree_voct.column('hsno', anchor=CENTER, width=60)
                                    tree_voct.column('mtrno', anchor=CENTER, width=60)
                                    tree_voct.column('bilm', anchor=CENTER, width=60)
                                    tree_voct.column('billd', anchor=CENTER, width=60)
                                    tree_voct.column('issd', anchor=CENTER, width=60)
                                    tree_voct.column('dued', anchor=CENTER, width=60)
                                    tree_voct.column('prev', anchor=CENTER, width=60)
                                    tree_voct.column('curr', anchor=CENTER, width=60)
                                    tree_voct.column('units', anchor=CENTER, width=60)
                                    tree_voct.column('amount', anchor=CENTER, width=60)

                                    tree_voct.heading('#0', text='')
                                    tree_voct.heading('n', text='')
                                    tree_voct.heading('hsno', text='House No')
                                    tree_voct.heading('mtrno', text='Meter No')
                                    tree_voct.heading('bilm', text='Month')
                                    tree_voct.heading('billd', text='Bill Date')
                                    tree_voct.heading('issd', text='Issue Date')
                                    tree_voct.heading('dued', text='Due Date')
                                    tree_voct.heading('prev', text='Previous')
                                    tree_voct.heading('curr', text='Current')
                                    tree_voct.heading('units', text='Units')
                                    tree_voct.heading('amount', text='Amount')
                                    if octlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in voct:
                                            tree_voct.tag_configure('evenrow', background="white")
                                            tree_voct.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_voct.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_voct.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_voct.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # =================================November====================But==============================================================================================================
                                def nov():
                                    novlist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_nov.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_dec.configure(bg="yellow", fg="green")
                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Nov'))
                                    vnov = cur.fetchall()
                                    novlist.append(vnov)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vnov = ttk.Treeview(Lfrm_Vbills)
                                    tree_vnov.grid(row=1, column=2)
                                    tree_vnov['columns'] = (
                                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                    'amount')
                                    tree_vnov.column('#0', stretch=NO, width=0)
                                    tree_vnov.column('n', anchor=CENTER, width=20)
                                    tree_vnov.column('hsno', anchor=CENTER, width=60)
                                    tree_vnov.column('mtrno', anchor=CENTER, width=60)
                                    tree_vnov.column('bilm', anchor=CENTER, width=60)
                                    tree_vnov.column('billd', anchor=CENTER, width=60)
                                    tree_vnov.column('issd', anchor=CENTER, width=60)
                                    tree_vnov.column('dued', anchor=CENTER, width=60)
                                    tree_vnov.column('prev', anchor=CENTER, width=60)
                                    tree_vnov.column('curr', anchor=CENTER, width=60)
                                    tree_vnov.column('units', anchor=CENTER, width=60)
                                    tree_vnov.column('amount', anchor=CENTER, width=60)

                                    tree_vnov.heading('#0', text='')
                                    tree_vnov.heading('n', text='')
                                    tree_vnov.heading('hsno', text='House No')
                                    tree_vnov.heading('mtrno', text='Meter No')
                                    tree_vnov.heading('bilm', text='Month')
                                    tree_vnov.heading('billd', text='Bill Date')
                                    tree_vnov.heading('issd', text='Issue Date')
                                    tree_vnov.heading('dued', text='Due Date')
                                    tree_vnov.heading('prev', text='Previous')
                                    tree_vnov.heading('curr', text='Current')
                                    tree_vnov.heading('units', text='Units')
                                    tree_vnov.heading('amount', text='Amount')
                                    if novlist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vnov:
                                            tree_vnov.tag_configure('evenrow', background="white")
                                            tree_vnov.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vnov.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vnov.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vnov.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # ================================December======================But================================================================================================================
                                def dec():
                                    declist.clear()
                                    # lbl_nodata.grid_forget()
                                    btn_dec.configure(bg="green", fg="yellow")
                                    btn_jan.configure(bg="yellow", fg="green")
                                    btn_feb.configure(bg="yellow", fg="green")
                                    btn_mar.configure(bg="yellow", fg="green")
                                    btn_apr.configure(bg="yellow", fg="green")
                                    btn_may.configure(bg="yellow", fg="green")
                                    btn_jun.configure(bg="yellow", fg="green")
                                    btn_jul.configure(bg="yellow", fg="green")
                                    btn_aug.configure(bg="yellow", fg="green")
                                    btn_sep.configure(bg="yellow", fg="green")
                                    btn_oct.configure(bg="yellow", fg="green")
                                    btn_nov.configure(bg="yellow", fg="green")

                                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                    cur = conn.cursor()
                                    cur.execute(
                                        "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                        (housebill.get(), Year.get(), 'Dec'))
                                    vdec = cur.fetchall()
                                    declist.append(vdec)
                                    style = ttk.Style()
                                    style.theme_use("default")
                                    style.configure("Treeview",
                                                    background="#D3D3D3",
                                                    foreground="black",
                                                    rowheight="25",
                                                    fieldbackground="#D3D3D3"
                                                    )
                                    style.map('Treeview', background=[('selected', 'pink')],
                                              foreground=[('selected', 'blue')])
                                    tree_vdec = ttk.Treeview(Lfrm_Vbills)
                                    tree_vdec.grid(row=1, column=2)
                                    tree_vdec['columns'] = (
                                        'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                        'amount')
                                    tree_vdec.column('#0', stretch=NO, width=0)
                                    tree_vdec.column('n', anchor=CENTER, width=20)
                                    tree_vdec.column('hsno', anchor=CENTER, width=60)
                                    tree_vdec.column('mtrno', anchor=CENTER, width=60)
                                    tree_vdec.column('bilm', anchor=CENTER, width=60)
                                    tree_vdec.column('billd', anchor=CENTER, width=60)
                                    tree_vdec.column('issd', anchor=CENTER, width=60)
                                    tree_vdec.column('dued', anchor=CENTER, width=60)
                                    tree_vdec.column('prev', anchor=CENTER, width=60)
                                    tree_vdec.column('curr', anchor=CENTER, width=60)
                                    tree_vdec.column('units', anchor=CENTER, width=60)
                                    tree_vdec.column('amount', anchor=CENTER, width=60)

                                    tree_vdec.heading('#0', text='')
                                    tree_vdec.heading('n', text='')
                                    tree_vdec.heading('hsno', text='House No')
                                    tree_vdec.heading('mtrno', text='Meter No')
                                    tree_vdec.heading('bilm', text='Month')
                                    tree_vdec.heading('billd', text='Bill Date')
                                    tree_vdec.heading('issd', text='Issue Date')
                                    tree_vdec.heading('dued', text='Due Date')
                                    tree_vdec.heading('prev', text='Previous')
                                    tree_vdec.heading('curr', text='Current')
                                    tree_vdec.heading('units', text='Units')
                                    tree_vdec.heading('amount', text='Amount')
                                    if declist:
                                        lbl_nodata.grid_forget()
                                        tree_vbills.grid_forget()
                                        num = 0
                                        n = 1
                                        for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vdec:
                                            tree_vdec.tag_configure('evenrow', background="white")
                                            tree_vdec.tag_configure('oddrow', background="lightblue")
                                            if num % 2 == 0:
                                                tree_vdec.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('evenrow',))
                                            else:
                                                tree_vdec.insert(parent='', index=END, iid=str(num), values=(
                                                n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                                 tags=('oddrow',))
                                            num += 1
                                            n += 1
                                    else:
                                        tree_vbills.grid_forget()
                                        tree_vdec.grid_forget()
                                        lbl_nodata.grid(row=2, column=2)
                                    conn.commit()
                                    conn.close()

                                # =====================================================================================================================================================================================
                                def exitVbills():
                                    Lfrm_Vbills.grid_forget()
                                    btn_exitVbills.grid_forget()
                                    btn_InL2Bdview.configure(state=NORMAL)
                                    btn_InL2BdPro.configure(state=NORMAL)

                                btn_exitVbills = Button(Lfrm_InCBd, relief="raised", text="E_X_I_T",
                                                        background="#588c7e", fg="#ff6f69",
                                                        command=exitVbills, activebackground="#ff6f69",
                                                        activeforeground="#588c7e", font=("arial", 15, "bold"))
                                btn_exitVbills.grid(row=2, column=0)

                                frm_months = Frame(Lfrm_Vbills, bg="#ffcc5c", pady=5, padx=5)
                                frm_months.grid(row=1, column=0)
                                btn_jan = Button(frm_months, text="Jan", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=jan, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_jan.grid(row=0, column=0)
                                btn_feb = Button(frm_months, text="Feb", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=feb, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_feb.grid(row=1, column=0)
                                btn_mar = Button(frm_months, text="Mar", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=mar, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_mar.grid(row=2, column=0)
                                btn_apr = Button(frm_months, text="Apr", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=apr, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_apr.grid(row=3, column=0)
                                btn_may = Button(frm_months, text="May", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=may, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_may.grid(row=4, column=0)
                                btn_jun = Button(frm_months, text="Jun", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=jun, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_jun.grid(row=5, column=0)
                                btn_jul = Button(frm_months, text="Jul", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=jul, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_jul.grid(row=6, column=0)
                                btn_aug = Button(frm_months, text="Aug", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=aug, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_aug.grid(row=7, column=0)
                                btn_sep = Button(frm_months, text="Sep", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=sep, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_sep.grid(row=8, column=0)
                                btn_oct = Button(frm_months, text="Oct", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=oct, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_oct.grid(row=9, column=0)
                                btn_nov = Button(frm_months, text="Nov", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=nov, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_nov.grid(row=10, column=0)
                                btn_dec = Button(frm_months, text="Dec", bg="yellow", fg="green",
                                                 activeforeground="yellow", command=dec, font=("helvetica", 10, "bold"),
                                                 activebackground="green", relief="raised")
                                btn_dec.grid(row=11, column=0)

                                frm_year = Frame(Lfrm_Vbills, bg="#622569", pady=10, padx=10)
                                frm_year.grid(row=1, column=1)
                                yr = datetime.datetime.today()
                                ry = str(yr.strftime("%Y"))
                                md = str(yr.strftime("%b"))
                                Year = IntVar()
                                etr_year = Entry(frm_year, textvariable=Year, bg="#c1946a", fg="#622569",
                                                 font=("times", 15, "bold"), justify=RIGHT, width=5)
                                etr_year.grid(row=1)
                                etr_year.delete(0, END)
                                etr_year.insert(END, ry)

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
                                tree_vbills = ttk.Treeview(Lfrm_Vbills)
                                tree_vbills.grid(row=1, column=2)
                                tree_vbills['columns'] = (
                                'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units',
                                'amount')
                                tree_vbills.column('#0', stretch=NO, width=0)
                                tree_vbills.column('n', anchor=CENTER, width=20)
                                tree_vbills.column('hsno', anchor=CENTER, width=60)
                                tree_vbills.column('mtrno', anchor=CENTER, width=60)
                                tree_vbills.column('bilm', anchor=CENTER, width=60)
                                tree_vbills.column('billd', anchor=CENTER, width=60)
                                tree_vbills.column('issd', anchor=CENTER, width=60)
                                tree_vbills.column('dued', anchor=CENTER, width=60)
                                tree_vbills.column('prev', anchor=CENTER, width=60)
                                tree_vbills.column('curr', anchor=CENTER, width=60)
                                tree_vbills.column('units', anchor=CENTER, width=60)
                                tree_vbills.column('amount', anchor=CENTER, width=60)

                                tree_vbills.heading('#0', text='')
                                tree_vbills.heading('n', text='')
                                tree_vbills.heading('hsno', text='House No')
                                tree_vbills.heading('mtrno', text='Meter No')
                                tree_vbills.heading('bilm', text='Month')
                                tree_vbills.heading('billd', text='Bill Date')
                                tree_vbills.heading('issd', text='Issue Date')
                                tree_vbills.heading('dued', text='Due Date')
                                tree_vbills.heading('prev', text='Previous')
                                tree_vbills.heading('curr', text='Current')
                                tree_vbills.heading('units', text='Units')
                                tree_vbills.heading('amount', text='Amount')

                                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                cur = conn.cursor()
                                cur.execute(
                                    "SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Month=?",
                                    (housebill.get(), ry, md))
                                vb = cur.fetchall()
                                if vb:
                                    num = 0
                                    n = 1
                                    for hs, mtr, bil, bill, iss, due, prev, curr, unit, amount in vb:
                                        tree_vbills.tag_configure('evenrow', background="white")
                                        tree_vbills.tag_configure('oddrow', background="lightblue")
                                        if num % 2 == 0:
                                            tree_vbills.insert(parent='', index=END, iid=str(num), values=(
                                            n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                               tags=('evenrow',))
                                        else:
                                            tree_vbills.insert(parent='', index=END, iid=str(num), values=(
                                            n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),
                                                               tags=('oddrow',))
                                        num += 1
                                        n += 1
                                else:
                                    tree_vbills.grid_forget()
                                    lbl_nodata.grid(row=1, column=2)
                                conn.commit()
                                conn.close()

                            btn_InL2Bd = Button(Lfrm_InL2Bd, text="B_A_C_K_ T_O_ S_E_L_E_C_T", font=("times", 10),
                                                bg="#cfe0e8", fg="#622569",
                                                command=BackSelect, activebackground="#ff6f69",
                                                activeforeground="#588c7e", relief="raised", borderwidth=1, )
                            btn_InL2Bd.grid(padx=10, pady=10)

                            btn_InL2BdPro = Button(Lfrm_InL2Bd, text="P_R_O_C_E_S_S_ B_I_L_L_S_ ", font=("times", 10),
                                                   bg="#cfe0e8", fg="#622569",
                                                   command=ProcessBills, activebackground="#ff6f69",
                                                   activeforeground="#588c7e", relief="raised", borderwidth=1, )
                            btn_InL2BdPro.grid(padx=10, pady=10)

                            btn_InL2Bdview = Button(Lfrm_InL2Bd, text="V_I_E_W_ B_I_L_L_S_ ", font=("times", 10),
                                                    bg="#cfe0e8", fg="#622569",
                                                    command=ViewBills, activebackground="#ff6f69",
                                                    activeforeground="#588c7e",
                                                    relief="raised", borderwidth=1, )
                            btn_InL2Bdview.grid(padx=10, pady=10)

                        def Validate():
                            if UserName.get() == '' or passw.get() == '':
                                messagebox.showerror('Empty Fields', 'User Id and Password Must Be Filled')
                            else:
                                conn = sqlite3.connect('Gracious_Data')
                                cur = conn.cursor()
                                # cur.execute("SELECT * FROM System_UserTest1")
                                cur.execute("SELECT Admin_Id,Password FROM Administrator WHERE Admin_Id=? AND Password=?",
                                    (UserName.get(), passw.get()))
                                c = cur.fetchall()
                                # a = cur.fetchall()
                                # print(a)
                                cur.execute("SELECT * FROM User WHERE User_Id=? AND Password=?",
                                            (UserName.get(), passw.get()))
                                a = cur.fetchall()
                                if c or a:
                                    etr_usid.delete(0, END)
                                    etr_passw.delete(0, END)
                                    etr_usid.focus()
                                    print('Log In Successful')
                                    print(housebill.get())
                                    BillDetails()
                                else:
                                    def failOut():
                                        lbl_fail.grid_forget()

                                    etr_usid.delete(0, END)
                                    etr_passw.delete(0, END)
                                    etr_usid.focus()
                                    lbl_fail = Label(Lfrm_OutCwat, text='Log In Failed!!', bg="#ffcc5c", fg="#622569",
                                                     font=("times", 10, "bold"))
                                    lbl_fail.grid(row=2, column=0)
                                    lbl_fail.after(3000, failOut)
                                conn.commit()
                                conn.close()

                        def ExitLog():
                            lbl_OutC.grid_forget()
                            lbl_passw.grid_forget()
                            lbl_usid.grid_forget()
                            etr_passw.grid_forget()
                            etr_usid.grid_forget()
                            btn_usLogin.grid_forget()
                            btn_exitusLog.grid_forget()
                            opt_select.configure(housebill.set(''))

                        btn_usLogin = Button(frm_MidC, text="Log In", background="#588c7e", fg="#ff6f69",
                                             activebackground="#ff6f69",
                                             activeforeground="#588c7e", font=("arial", 15, "bold"), command=Validate)
                        btn_usLogin.grid(row=1, column=0, pady=5)
                        btn_exitusLog = Button(frm_MidC, text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                               activebackground="#ff6f69",
                                               activeforeground="#588c7e", font=("arial", 15, "bold"), command=ExitLog)
                        btn_exitusLog.grid(row=1, column=1, pady=5)

                conn = sqlite3.connect('Gracious_Data')
                cur = conn.cursor()
                try:
                    cur.execute("SELECT * FROM Apartment")
                    c = cur.fetchall()
                    AptName = []
                    # print(c[0])
                    # print(c[1])
                    # count = 1
                    for name, location, units, floors in c:
                        AptName.append(name)

                    housebill = StringVar()
                    opt_select = OptionMenu(frm_MidL1, housebill, *AptName)
                    opt_select.grid(row=1, column=0, padx=20, pady=(5, 10))
                    btn_select = Button(Lfrm_OutL1wat, text="Select Apartment", font=("times", 10), bg="#cfe0e8",
                                        fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                        relief="raised", borderwidth=1,
                                        command=HseLogin)
                    btn_select.grid(row=2, column=0)
                    conn.commit()
                    conn.close()
                except:
                    lbl_select = Label(Lfrm_OutL1wat, text="Go To Admin To Create Apartment", font=("times", 10), bg="#cfe0e8",
                                        fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",relief="raised", borderwidth=1,)
                    lbl_select.grid(row=2, column=0)

                Lfrm_OutL2wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutL2wat.grid(row=2, column=0, padx=(5, 50), pady=50)
                frm_MidL2 = Frame(Lfrm_OutL2wat, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidL2.grid(padx=15, pady=15)
                Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InL2.grid()

                def backBill():
                    Lfrm_OutL1wat.grid_forget()
                    Lfrm_OutL2wat.grid_forget()
                    Lfrm_OutR1wat.grid_forget()
                    Lfrm_OutCwat.grid_forget()
                    Lfrm_Outhpage.grid(row=2, column=2, padx=500, pady=50)

                btn_InL2a = Button(Lfrm_InL2, text="_B_A_C_K_HOME_", font=("times", 15), bg="#cfe0e8", fg="#622569",
                                   command=backBill, activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1, )
                btn_InL2a.grid(padx=10, pady=10)
                '''btn_InL2b = Button(Lfrm_InL2,text="  Add___New__User  ", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,)
                btn_InL2b.grid(padx=10, pady=10)
                btn_InL2c = Button(Lfrm_InL2,text=" H_o_u_s_e_Accounts", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2c.grid(padx=10, pady=10)
                btn_InL2d = Button(Lfrm_InL2,text="  B_i_l_l_Man_age_r_", font=("times",15), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
                btn_InL2d.grid(padx=10, pady=10)
                btn_InL2e = Button(Lfrm_InL2,text=" A_d_m_i_n_Office    ", font=("times",15), bg="#cfe0e8", fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,)
                btn_InL2e.grid(padx=10, pady=10)
                frm_Right = Frame(master,bg="#cfe0e8", padx=0, pady=0)
                frm_Right.grid(row=1, column=4, rowspan=2, pady=(20,10), padx=(20,20))'''

                Lfrm_OutR1wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR1wat.grid(row=1, column=4, padx=(10, 20), pady=(20, 10))
                frm_MidR1 = Frame(Lfrm_OutR1wat, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR1.grid(padx=8, pady=8)
                Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR1.grid()
                tex = datetime.datetime.today()
                cal = Calendar(Lfrm_InR1, selectmode="day", year=tex.year, month=tex.month, day=tex.day)
                cal.grid(padx=20, pady=20)
                y = cal.get_date()
                c, v, b = y.split('/')
                x = datetime.datetime(int(b), int(c), int(v))
                print(x.strftime("%f"))

                '''Lfrm_OutR2 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
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
                btn_InR4.grid(padx=10, pady=10)'''

            def shrink():
                frm_bill.configure(bg="#622569", padx=10, pady=10)

            def normal():
                btn_bill.configure(font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569")
                btn_bill.grid_configure(padx=5, pady=5)
                billManager()

            frm_bill.after(1000, shrink)
            btn_bill.after(1000, normal)

        frm_bill = Frame(Lfrm_In, bg="#622569", padx=10, pady=10)
        frm_bill.grid(row=3, rowspan=2, columnspan=3, column=0, padx=10, pady=10)
        btn_bill = Button(frm_bill, text="B_i_l_l Man_age_r_", font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569",
                          relief="raised", borderwidth=3, command=billCommand)
        btn_bill.grid(padx=5, pady=5)

        def adminCommand():
            frm_Admin.configure(bg="#ffcc5c", padx=0, pady=0)
            btn_Admin.configure(font=("times", 40), bg="#ffcc5c", fg="#622569")
            btn_Admin.grid_configure(padx=0, pady=0)
            def administration():
                Lfrm_Outhpage.grid_forget()

                Lfrm_OutC = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=40, pady=40)
                Lfrm_OutC.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
                frm_MidC = Frame(Lfrm_OutC, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                frm_MidC.grid(row=1, column=0)
                Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC.grid(row=0, column=0, columnspan=2)

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
                frm_MidC4 = Frame(Lfrm_OutC4, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
                frm_MidC4.grid(row=1, column=0)
                Lfrm_InC4 = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InC4.grid(row=1, column=0, columnspan=2)

                def createNewApartment():
                    class Apartment:
                        def __init__(self, hseName, location, numFloors):
                            self.hseName = hseName
                            self.location = location
                            self.numFloors = numFloors

                    Lfrm_OutC1.grid_forget()
                    Lfrm_OutC4.grid_forget()
                    Lfrm_OutC.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)

                    lbl_OutC = Label(Lfrm_OutC, text="Create New Apartment", font=("times", 15, "bold"), bg="#ffcc5c",
                                     fg="#622569")
                    lbl_OutC.grid(row=0, column=0)
                    lbl_hsName = Label(Lfrm_InC, text="_House_Name_ : ", bg="#ffcc5c", fg="#622569",
                                       font=("times", 10, "bold"))
                    lbl_hsName.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                    lbl_loc = Label(Lfrm_InC, text="Location/City : ", bg="#ffcc5c", fg="#622569",
                                    font=("times", 10, "bold"))
                    lbl_loc.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                    lbl_units = Label(Lfrm_InC, text="Number_Of_Units: ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 10, "bold"))
                    lbl_units.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
                    lbl_flrs = Label(Lfrm_InC, text="No_of_Floo_rs : ", bg="#ffcc5c", fg="#622569",
                                     font=("times", 10, "bold"))
                    lbl_flrs.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

                    Hse_Name = StringVar()
                    etr_Hse = Entry(Lfrm_InC, textvariable=Hse_Name, bg="#c1946a", fg="#622569",
                                    font=("times", 20, "bold"))
                    etr_Hse.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                    City = StringVar()
                    etr_City = Entry(Lfrm_InC, textvariable=City, bg="#c1946a", fg="#622569",
                                     font=("times", 20, "bold"))
                    etr_City.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                    NumUnits = IntVar()
                    etr_Units = Entry(Lfrm_InC, textvariable=NumUnits, bg="#c1946a", fg="#622569",
                                      font=("times", 20, "bold"))
                    etr_Units.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
                    etr_Units.delete(0, END)
                    Floors = IntVar()
                    etr_Flrs = Entry(Lfrm_InC, textvariable=Floors, bg="#c1946a", fg="#622569",
                                     font=("times", 20, "bold"))
                    etr_Flrs.grid(row=3, column=2, columnspan=2, padx=10, pady=20)
                    etr_Flrs.delete(0, END)

                    def saveApt():
                        def saveLblout():
                            lbl_sux.grid_forget()
                            # btn_saveApt.grid_forget()
                            etr_Hse.focus()

                        try:
                            if Hse_Name.get() == '' or City.get() == '' or NumUnits.get() == 0 or Floors.get() == 0:
                                messagebox.showerror('Empty Field', 'Fill In All Fields To Continue')
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
                                conn = sqlite3.connect('Gracious_Data')
                                cur = conn.cursor()
                                cur.execute("""CREATE TABLE IF NOT EXISTS Apartment
                                            (House_Name VARCAHAR NOT NULL,
                                             Location VARCHAR NOT NULL,
                                             Num_Units INTEGER NOT NULL,
                                             Floors INTEGER NOT NULL)
                                            """)
                                cur.execute(
                                    "INSERT INTO Apartment(House_Name,Location,Num_Units,Floors) VALUES(?,?,?,?)",
                                    (Hse_Name.get(), City.get(), NumUnits.get(), Floors.get()))
                                conn.commit()
                                conn.close()
                                lbl_sux = Label(Lfrm_OutC, text=Hse_Name.get() + "Apartment Created Successfully",
                                                font=("times", 10), bg="#ffcc5c", fg="#622569")
                                lbl_sux.grid(row=2, column=0)
                                etr_Hse.delete(0, END)
                                etr_City.delete(0, END)
                                etr_Units.delete(0, END)
                                etr_Flrs.delete(0, END)
                                lbl_sux.after(3000, saveLblout)
                        except:
                            messagebox.showerror('Empty Field', 'Fill In Units and Floors And Must Be Numeric')

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

                    btn_saveApt = Button(frm_MidC, text="Create New Apartment", bg="#588c7e", fg="#ff6f69",
                                         activebackground="#ff6f69", activeforeground="#588c7e",
                                         font=("arial", 15, "bold"),
                                         relief="raised", borderwidth=1, command=saveApt)
                    btn_saveApt.grid(row=1, column=0, pady=5)
                    btn_exitApt = Button(frm_MidC, text="E_X_I_T", bg="#588c7e", fg="#ff6f69",
                                         activebackground="#ff6f69",
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

                    lbl_OutC1 = Label(Lfrm_OutC1, text="Add New User", font=("times", 15, "bold"), bg="#ffcc5c",
                                      fg="#622569")
                    lbl_OutC1.grid(row=0, column=0, pady=5)
                    lbl_userID = Label(Lfrm_InC1, text="_User_I_D : ", bg="#ffcc5c", fg="#622569",
                                       font=("times", 10, "bold"))
                    lbl_userID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                    lbl_fname = Label(Lfrm_InC1, text="First Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 10, "bold"))
                    lbl_fname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                    lbl_lname = Label(Lfrm_InC1, text="Last_Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 10, "bold"))
                    lbl_lname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
                    lbl_password = Label(Lfrm_InC1, text="Password : ", bg="#ffcc5c", fg="#622569",
                                         font=("times", 10, "bold"))
                    lbl_password.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

                    UserID = StringVar()
                    etr_usID = Entry(Lfrm_InC1, textvariable=UserID, bg="#c1946a", fg="#622569",
                                     font=("times", 20, "bold"))
                    etr_usID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                    firstName = StringVar()
                    etr_fname = Entry(Lfrm_InC1, textvariable=firstName, bg="#c1946a", fg="#622569",
                                      font=("times", 20, "bold"))
                    etr_fname.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                    lastName = StringVar()
                    etr_lname = Entry(Lfrm_InC1, textvariable=lastName, bg="#c1946a", fg="#622569",
                                      font=("times", 20, "bold"))
                    etr_lname.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
                    passWord = StringVar()
                    etr_psWord = Entry(Lfrm_InC1, textvariable=passWord, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"), show="*")
                    etr_psWord.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

                    def addUser():
                        if etr_usID == '' or etr_fname == '' or etr_lname.get() == '' or etr_psWord.get() == '':
                            messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                        else:
                            conn = sqlite3.connect('Gracious_Data')
                            cur = conn.cursor()
                            cur.execute("INSERT INTO User VALUES(?,?,?,?)",(UserID.get(), firstName.get(), lastName.get(), passWord.get()))
                            conn.commit()
                            conn.close()

                            def suxMesOut():
                                lbl_suxMes.grid_forget()

                            etr_fname.delete(0, END)
                            etr_lname.delete(0, END)
                            etr_usID.delete(0, END)
                            etr_psWord.delete(0, END)
                            lbl_suxMes = Label(Lfrm_OutC1, text='Successfully Added To Database ' + etr_usID.get(),
                                               font=("times", 10), bg="#ffcc5c", fg="#cfe0e8")
                            lbl_suxMes.grid(row=2, column=0)
                            lbl_suxMes.after(3000, suxMesOut)

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

                    btn_addUser = Button(frm_MidC1, text="Add New User", bg="#588c7e", fg="#ff6f69",
                                         activebackground="#ff6f69",
                                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                                         relief="raised", borderwidth=1, command=addUser)
                    btn_addUser.grid(row=1, column=0, pady=5)
                    btn_exitUse = Button(frm_MidC1, text="E_X_I_T", bg="#588c7e", fg="#ff6f69",
                                         activebackground="#ff6f69",
                                         activeforeground="#588c7e", font=("arial", 15, "bold"),
                                         relief="raised", borderwidth=1, command=exitUse)
                    btn_exitUse.grid(row=1, column=1, pady=5)

                def Office():
                    Lfrm_OutC.grid_forget()
                    Lfrm_OutC1.grid_forget()
                    Lfrm_OutC4.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)

                    lbl_OutC4 = Label(Lfrm_OutC4, text="Update System Profile", font=("times", 20, "bold"),
                                      bg="#ffcc5c", fg="#622569")
                    lbl_OutC4.grid(row=0, column=0)

                    def UpAdmin():
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
                        Lfrm_InC4i = LabelFrame(frm_MidC4, bg="#cfe0e8", padx=15, pady=20)
                        Lfrm_InC4i.grid(row=1, column=0, columnspan=2)
                        # ====================================================================================
                        Lfrm_UpAdminT = LabelFrame(Lfrm_InC4i, bg="#622569", padx=5, pady=5)
                        Lfrm_UpAdminT.grid(row=0, column=0, padx=20, pady=10)
                        conn = sqlite3.connect('Gracious_Data')
                        cur = conn.cursor()
                        cur.execute("SELECT Admin_Id,First_Name,Last_Name FROM Administrator")
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
                                tree_admin.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),
                                                  tags=('evenrow',))
                            else:
                                tree_admin.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),
                                                  tags=('oddrow',))
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
                                    conn = sqlite3.connect('Gracious_Data')
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
                                    etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569",
                                                   show="*",
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
                                                "SELECT Admin_Id,Password FROM Administrator WHERE Admin_Name=? AND Password=?",(AdmnID.get(), AdmnPass.get()))
                                            c = cur.fetchall()

                                            if c:
                                                cur.execute(
                                                    "UPDATE Administrator SET Admin_Id=?, First_Name=?, Last_Name=?, Password=? WHERE Admin_Id=?",((AdminID.get(), AfirstName.get(), AlastName.get(), ApassWord.get(),
                                                      AdminID.get())))
                                                conn.commit()
                                                conn.close()

                                                def suxMesOut():
                                                    lbl_suxMes.grid_forget()
                                                    vTop.destroy()
                                                    etr_adID.focus()

                                                etr_afname.delete(0, END)
                                                etr_alname.delete(0, END)
                                                etr_adID.delete(0, END)
                                                etr_apsWord.delete(0, END)
                                                etr_adID.focus()
                                                selected = tree_admin.focus()
                                                tree_admin.item(selected, text='', values=(
                                                etr_adID.get(), etr_afname.get(), etr_alname.get()))
                                                lbl_suxMes = Label(vTop,
                                                                   text=etr_adID.get() + ' Successfully Added To Database',
                                                                   font=("times", 10), bg="#ffcc5c", fg="#622569")
                                                lbl_suxMes.grid(row=3, column=0)
                                                lbl_suxMes.after(3000, suxMesOut)
                                            else:
                                                vTop.destroy()
                                                messagebox.showerror('Wrong Entry',
                                                                     'Wrong Name or Password.\n Cannot Proceed With Admin Update')

                                    btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69",
                                                      activebackground="#ff6f69",
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

                        # ======================================================================================

                        Lfrm_UpAdmin_1 = LabelFrame(Lfrm_InC4i, bg="#622569", padx=5, pady=5)
                        Lfrm_UpAdmin_1.grid(row=2, column=0, padx=20, pady=10)
                        lbl_MidC4 = Label(frm_MidC4, text=" Update Admin Details", fg="#cfe0e8", bg="#622569",
                                          font=("times", 10, "bold"))
                        lbl_MidC4.grid(row=0, column=0)

                        lbl_AdminID = Label(Lfrm_UpAdmin_1, text="_Admin_I_D : ", bg="#ffcc5c", fg="#622569",
                                            font=("times", 10, "bold"))
                        lbl_AdminID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Afname = Label(Lfrm_UpAdmin_1, text="First Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_Afname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Alname = Label(Lfrm_UpAdmin_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_Alname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Apassword = Label(Lfrm_UpAdmin_1, text="Password : ", bg="#ffcc5c", fg="#622569",
                                              font=("times", 10, "bold"))
                        lbl_Apassword.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

                        AdminID = StringVar()
                        etr_adID = Entry(Lfrm_UpAdmin_1, textvariable=AdminID, bg="#c1946a", fg="#622569",
                                         font=("times", 20, "bold"))
                        etr_adID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                        AfirstName = StringVar()
                        etr_afname = Entry(Lfrm_UpAdmin_1, textvariable=AfirstName, bg="#c1946a", fg="#622569",
                                           font=("times", 20, "bold"))
                        etr_afname.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                        AlastName = StringVar()
                        etr_alname = Entry(Lfrm_UpAdmin_1, textvariable=AlastName, bg="#c1946a", fg="#622569",
                                           font=("times", 20, "bold"))
                        etr_alname.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
                        ApassWord = StringVar()
                        etr_apsWord = Entry(Lfrm_UpAdmin_1, textvariable=ApassWord, bg="#c1946a", fg="#622569",
                                            font=("times", 20, "bold"),
                                            show="*")
                        etr_apsWord.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

                        def UpdateAdmin():
                            if etr_adID == '' or etr_afname == '' or etr_alname.get() == '' or etr_apsWord.get() == '':
                                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                            else:
                                conn = sqlite3.connect('Gracious_Data')
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

                                def UPDATE():
                                    if AdmnID.get() == '' or AdmnPass.get() == '':
                                        messagebox.showerror('Empty Field', 'You Must Enter Name and Password')
                                    else:
                                        cur.execute("SELECT * FROM Administrator")
                                        e = cur.fetchall()
                                        print(e)
                                        cur.execute(
                                            "SELECT Admin_Id,Password FROM Administrator WHERE Admin_Id=? AND Password=?",
                                            (AdmnID.get(), AdmnPass.get()))
                                        c = cur.fetchall()

                                        if c:
                                            cur.execute(
                                                "UPDATE Administrator SET Admin_Id=?, First_Name=?, Last_Name=?, Password=? WHERE Admin_Id=?",
                                                ((AdminID.get(), AfirstName.get(), AlastName.get(), ApassWord.get(),
                                                  AdmnID.get())))
                                            conn.commit()
                                            conn.close()

                                            def suxMesOut():
                                                lbl_suxMes.grid_forget()
                                                vTop.destroy()
                                                etr_adID.focus()

                                            etr_afname.delete(0, END)
                                            etr_alname.delete(0, END)
                                            etr_adID.delete(0, END)
                                            etr_apsWord.delete(0, END)
                                            lbl_suxMes = Label(vTop,
                                                               text=etr_adID.get() + ' Successfully Added To Database',
                                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                                            lbl_suxMes.grid(row=3, column=0)
                                            lbl_suxMes.after(3000, suxMesOut)
                                        else:
                                            vTop.destroy()
                                            messagebox.showerror('Wrong Entry',
                                                                 'Wrong Name or Password.\n Cannot Proceed With Admin Update')
                                            etr_adID.focus()

                                btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69",
                                                  activebackground="#ff6f69", activeforeground="#588c7e",
                                                  font=("arial", 15, "bold"),
                                                  relief="raised", borderwidth=1, command=UPDATE)
                                btn_vTop.grid(row=2, column=0)

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

                        btn_saveAdmin = Button(frm_MidC4, text="Update Admin", bg="#588c7e", fg="#ff6f69",
                                               activebackground="#ff6f69", activeforeground="#588c7e",
                                               font=("arial", 10, "bold",),
                                               relief="raised", borderwidth=1, command=UpdateAdmin)
                        btn_saveAdmin.grid(row=2, column=0)
                        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69",
                                               activebackground="#ff6f69",
                                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                                               relief="raised", borderwidth=1, command=BackAdmin)
                        btn_backAdmin.grid(row=2, column=1)

                    Lfrm_UpAdmin = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
                    Lfrm_UpAdmin.grid(row=0, column=0, padx=20, pady=10)
                    btn_UpAdmin = Button(Lfrm_UpAdmin, text="     _Update_ Admin_ Profile_        ", bg="#cfe0e8",
                                         fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",
                                         font=("times", 20, "bold"),
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
                        Lfrm_UpUserT.grid(row=0, column=0, padx=20, pady=(0, 10))
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
                        for id, fname, lname in c:
                            tree_user.tag_configure('evenrow', background="white")
                            tree_user.tag_configure('oddrow', background="lightblue")
                            if 1 % 2 == 0:
                                tree_user.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),
                                                 tags=('evenrow',))
                            else:
                                tree_user.insert(parent='', index='end', iid=str(i), values=(id, fname, lname),
                                                 tags=('oddrow',))
                            i += 1
                        conn.commit()
                        conn.close()
                        ys = ttk.Scrollbar(Lfrm_UpUserT, orient=VERTICAL, command=tree_user.yview)
                        tree_user["yscrollcommand"] = ys.set
                        ys.grid(row=0, column=1, sticky="E")

                        def EditUser():
                            selUser = tree_user.focus()
                            userDetails = tree_user.item(selUser, 'values')
                            userId = userDetails[0]
                            userf = userDetails[1]
                            userl = userDetails[2]

                            etr_userID.insert(0, userId)
                            etr_ufname.insert(0, userf)
                            etr_ulname.insert(0, userl)
                            btn_editUser.grid_forget()

                            def Edit():
                                if etr_userID == '' or etr_ufname == '' or etr_ulname.get() == '' or etr_upsWord.get() == '':
                                    messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                                else:
                                    conn = sqlite3.connect('Gracious_Data')
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
                                    etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569",
                                                   show="*",
                                                   font=("times", 20, "bold"))
                                    etr_pw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

                                    def UPDATEUSER():
                                        if AdmnID.get() == '' or AdmnPass.get() == '':
                                            messagebox.showerror('Empty Field', 'You Must Enter Name and Password')
                                        else:
                                            conn = sqlite3.connect('Gracious_Data')
                                            cur.execute("SELECT * FROM Administrator")
                                            e = cur.fetchall()
                                            print(e)
                                            cur.execute(
                                                "SELECT Admin_Id,Password FROM Administrator WHERE Admin_Id=? AND Password=?",
                                                (AdmnID.get(), AdmnPass.get()))
                                            c = cur.fetchall()

                                            if c:
                                                cur.execute(
                                                    "UPDATE User SET User_Id=?, First_Name=?, Last_Name=?, Password=? WHERE User_Id=?",
                                                    ((UserID.get(), UfirstName.get(), UlastName.get(), UpassWord.get(),
                                                      UserID.get())))
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
                                                etr_userID.focus()
                                                selected = tree_user.focus()
                                                tree_user.item(selected, text='', values=(
                                                etr_userID.get(), etr_ufname.get(), etr_ulname.get()))
                                                lbl_suxMes = Label(vTop,
                                                                   text=etr_userID.get() + ' Successfully Added To Database',
                                                                   font=("times", 10), bg="#ffcc5c", fg="#622569")
                                                lbl_suxMes.grid(row=3, column=0)
                                                lbl_suxMes.after(3000, suxMesOut)
                                            else:
                                                vTop.destroy()
                                                messagebox.showerror('Wrong Entry',
                                                                     'Wrong Name or Password.\n Cannot Proceed With Admin Update')

                                    btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69",
                                                      activebackground="#ff6f69",
                                                      activeforeground="#588c7e", font=("arial", 15, "bold"),
                                                      relief="raised", borderwidth=1, command=UPDATEUSER)
                                    btn_vTop.grid(row=2, column=0)

                            btn_EDITUSER = Button(Lfrm_UpUserT, text="Edit User Details", bg="#588c7e", fg="#ff6f69",
                                                  activebackground="#ff6f69",
                                                  activeforeground="#588c7e", font=("arial", 10, "bold"),
                                                  relief="raised", borderwidth=1, command=Edit)
                            btn_EDITUSER.grid(row=1, column=0)

                        btn_editUser = Button(Lfrm_UpUserT, text="Edit User Details", bg="#588c7e", fg="#ff6f69",
                                              activebackground="#ff6f69",
                                              activeforeground="#588c7e", font=("arial", 10, "bold"),
                                              relief="raised", borderwidth=1, command=EditUser)
                        btn_editUser.grid(row=1, column=0)

                        Lfrm_UpUser_1 = LabelFrame(Lfrm_InC4ii, bg="#622569", padx=5, pady=5)
                        Lfrm_UpUser_1.grid(row=2, column=0, padx=20, pady=(0, 0))
                        lbl_MidC4 = Label(frm_MidC4, text=" Update User Details", fg="#cfe0e8", bg="#622569",
                                          font=("times", 10, "bold"))
                        lbl_MidC4.grid(row=0, column=0)

                        lbl_UserID = Label(Lfrm_UpUser_1, text="_User__I_D : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_UserID.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Ufname = Label(Lfrm_UpUser_1, text="First Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_Ufname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Ulname = Label(Lfrm_UpUser_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_Ulname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
                        lbl_Upassword = Label(Lfrm_UpUser_1, text="Password : ", bg="#ffcc5c", fg="#622569",
                                              font=("times", 10, "bold"))
                        lbl_Upassword.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

                        UserID = StringVar()
                        etr_userID = Entry(Lfrm_UpUser_1, textvariable=UserID, bg="#c1946a", fg="#622569",
                                           font=("times", 20, "bold"))
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
                            if etr_userID == '' or etr_ufname == '' or etr_ulname.get() == '' or etr_upsWord.get() == '':
                                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                            else:
                                conn = sqlite3.connect('Gracious_Data')
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
                                        # cur.execute("SELECT * FROM System_AdminTest1")
                                        # e = cur.fetchall()
                                        # print(e)
                                        cur.execute(
                                            "SELECT Admin_Id,Password FROM Administrator WHERE Admin_Id=? AND Password=?",
                                            (AdmnID.get(), AdmnPass.get()))
                                        c = cur.fetchall()

                                        if c:
                                            conn1 = sqlite3.connect('Gracious_Data')
                                            cur1 = conn1.cursor()
                                            cur1.execute(
                                                "UPDATE User SET User_Id=?, First_Name=?, Last_Name=?, Password=? WHERE User_Id=?",
                                                ((UserID.get(), UfirstName.get(), UlastName.get(), UpassWord.get(),
                                                  UserID.get())))
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
                                            lbl_suxMes = Label(vTop,
                                                               text=etr_userID.get() + ' Successfully Added To Database',
                                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                                            lbl_suxMes.grid(row=3, column=0)
                                            lbl_suxMes.after(3000, suxMesOut)
                                        else:
                                            vTop.destroy()
                                            messagebox.showerror('Wrong Entry',
                                                                 'Wrong Name or Password.\n Cannot Proceed With User Update')
                                            etr_userID.focus()

                                btn_vTop = Button(vTop, text="Confirm", bg="#588c7e", fg="#ff6f69",
                                                  activebackground="#ff6f69", activeforeground="#588c7e",
                                                  font=("arial", 15, "bold"),
                                                  relief="raised", borderwidth=1, command=UPDATEUSER)
                                btn_vTop.grid(row=2, column=0)

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

                        btn_saveUser = Button(frm_MidC4, text="Update User", bg="#588c7e", fg="#ff6f69",
                                              activebackground="#ff6f69", activeforeground="#588c7e",
                                              font=("arial", 10, "bold",),
                                              relief="raised", borderwidth=1, command=UpdateUser)
                        btn_saveUser.grid(row=2, column=0)
                        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69",
                                               activebackground="#ff6f69",
                                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                                               relief="raised", borderwidth=1, command=BackAdmin)
                        btn_backAdmin.grid(row=2, column=1)

                    Lfrm_UpUser = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
                    Lfrm_UpUser.grid(row=1, column=0, padx=20, pady=10)
                    btn_UpUser = Button(Lfrm_UpUser, text="     _Update_ User_ Profile_           ", bg="#cfe0e8",
                                        fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",
                                        font=("times", 20, "bold"),
                                        command=UpUser)
                    btn_UpUser.grid()

                    # ================================def============Remove===============User==============================================
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
                        lbl_UnameF = Label(Lfrm_RemUser_1, text="First Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_UnameF.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                        lbl_UnameL = Label(Lfrm_RemUser_1, text="Last_Name : ", bg="#ffcc5c", fg="#622569",
                                           font=("times", 10, "bold"))
                        lbl_UnameL.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

                        IDuser = StringVar()
                        etr_IDuser = Entry(Lfrm_RemUser_1, textvariable=IDuser, bg="#c1946a", fg="#622569",
                                           font=("times", 20, "bold"))
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
                            if etr_IDuser == '' or etr_unamef == '' or etr_unamel.get() == '':
                                messagebox.showerror('Empty Field', 'All Entries Must Be Filled')
                            else:
                                conn = sqlite3.connect('Gracious_Data')
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

                                def REMOVEUSER():
                                    if AdmnID.get() == '' or AdmnPass.get() == '':
                                        messagebox.showerror('Empty Field', 'You Must Enter Name and Password')
                                    else:
                                        # cur.execute("SELECT * FROM System_AdminTest1")
                                        # e = cur.fetchall()
                                        # print(e)
                                        cur.execute(
                                            "SELECT Admin_Id,Password FROM Administrator WHERE Admin_Id=? AND Password=?",
                                            (AdmnID.get(), AdmnPass.get()))
                                        c = cur.fetchall()

                                        if c:
                                            conn1 = sqlite3.connect('Gracious_Data')
                                            cur1 = conn1.cursor()
                                            cur1.execute(
                                                "DELETE FROM User WHERE User_Id=? AND First_Name=? AND Last_Name=?",
                                                ((IDuser.get(), UnameF.get(), UnameL.get())))
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
                                            lbl_suxMes = Label(vTop,
                                                               text=etr_IDuser.get() + ' Has Been Removed And Will No Longer Have Access To System',
                                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                                            lbl_suxMes.grid(row=3, column=0)
                                            lbl_suxMes.after(3000, suxMesOut)
                                        else:
                                            vTop.destroy()
                                            messagebox.showerror('Wrong Entry',
                                                                 'Wrong Name or Password.\n Cannot Proceed With Removal')
                                            etr_IDuser.focus()

                                btn_vTop = Button(vTop, text="Remove", bg="#588c7e", fg="#ff6f69",
                                                  activebackground="#ff6f69", activeforeground="#588c7e",
                                                  font=("arial", 15, "bold"),
                                                  relief="raised", borderwidth=1, command=REMOVEUSER)
                                btn_vTop.grid(row=2, column=0)

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

                        btn_remUser = Button(frm_MidC4, text="Remove User", bg="#588c7e", fg="#ff6f69",
                                             activebackground="#ff6f69",
                                             activeforeground="#588c7e", font=("arial", 10, "bold",),
                                             relief="raised", borderwidth=1, command=RemoveUser)
                        btn_remUser.grid(row=2, column=0)
                        btn_backAdmin = Button(frm_MidC4, text="Back", bg="#588c7e", fg="#ff6f69",
                                               activebackground="#ff6f69",
                                               activeforeground="#588c7e", font=("arial", 10, "bold",),
                                               relief="raised", borderwidth=1, command=BackAdmin)
                        btn_backAdmin.grid(row=2, column=1)

                    Lfrm_RemUser = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
                    Lfrm_RemUser.grid(row=2, column=0, padx=20, pady=10)
                    btn_RemUser = Button(Lfrm_RemUser, text="_Remove_ User_ From_ System_  ", bg="#cfe0e8",
                                         fg="#622569", activebackground="#ff6f69", activeforeground="#cfe0e8",
                                         font=("times", 20, "bold"),
                                         command=RemUser)
                    btn_RemUser.grid()

                    Lfrm_RemApt = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
                    Lfrm_RemApt.grid(row=3, column=0, padx=20, pady=10)
                    btn_RemApt = Button(Lfrm_RemApt, text="Remove Apartment From System_", bg="#cfe0e8", fg="#622569",
                                        activebackground="#ff6f69", activeforeground="#cfe0e8",
                                        font=("times", 20, "bold"))
                    btn_RemApt.grid()

                    Lfrm_bg = LabelFrame(Lfrm_InC4, bg="#622569", padx=5, pady=5)
                    Lfrm_bg.grid(row=4, column=0, padx=20, pady=10)
                    btn_bg = Button(Lfrm_bg, text="  _Change_System_Background_   ", bg="#cfe0e8", fg="#622569",
                                    activebackground="#ff6f69", activeforeground="#cfe0e8", font=("times", 20, "bold"))
                    btn_bg.grid()

                Lfrm_OutL1 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
                Lfrm_OutL1.grid(row=1, column=0, padx=(15, 50), pady=10)
                frm_MidL1 = Frame(Lfrm_OutL1, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidL1.grid(row=1, column=0, padx=60, pady=15)
                lbl_pageAd = Label(Lfrm_OutL1, text="Administrator_", bg="#ffcc5c", fg="#622569", font=("times", 18))
                lbl_pageAd.grid(row=0, column=0)

                Lfrm_OutL2 = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutL2.grid(row=2, column=0, padx=(5, 50), pady=50)
                frm_MidL2 = Frame(Lfrm_OutL2, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidL2.grid(padx=15, pady=15)
                Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InL2.grid()
                def backAdministrator():
                    Lfrm_OutC.grid_forget()
                    Lfrm_OutC1.grid_forget()
                    Lfrm_OutC4.grid_forget()
                    Lfrm_OutL1.grid_forget()
                    Lfrm_OutL2.grid_forget()
                    Lfrm_OutR1.grid_forget()
                    Lfrm_OutR2.grid_forget()
                    Lfrm_OutR3.grid_forget()
                    Lfrm_OutR4.grid_forget()
                    Lfrm_Outhpage.grid(row=2,column=2)


                btn_InL2c = Button(Lfrm_InL2, text=" B_A_C_K_HOME", font=("times", 15), bg="#cfe0e8",
                                   fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1, command=backAdministrator)
                btn_InL2c.grid(padx=10, pady=10)
                btn_InL2a = Button(Lfrm_InL2, text="Create New Apartment", font=("times", 15), bg="#cfe0e8",
                                   fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1,
                                   command=createNewApartment)
                btn_InL2a.grid(padx=10, pady=10)
                btn_InL2b = Button(Lfrm_InL2, text="  Add___New__User  ", font=("times", 15), bg="#cfe0e8",
                                   fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1,
                                   command=addNewUser)
                btn_InL2b.grid(padx=10, pady=10)
                btn_InL2d = Button(Lfrm_InL2, text="  B_i_l_l_Man_age_r_", font=("times", 15), bg="#cfe0e8",
                                   fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1)
                btn_InL2d.grid(padx=10, pady=10)
                btn_InL2e = Button(Lfrm_InL2, text=" A_d_m_i_n_Office    ", font=("times", 15), bg="#cfe0e8",
                                   fg="#622569", activebackground="#ff6f69", activeforeground="#588c7e",
                                   relief="raised", borderwidth=1,
                                   command=Office)
                btn_InL2e.grid(padx=10, pady=10)

                frm_Right = Frame(master, bg="#cfe0e8", padx=0, pady=0)
                frm_Right.grid(row=1, column=4, rowspan=2, pady=(20, 10), padx=(20, 20))
                Lfrm_OutR1 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR1.grid(row=1, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR1 = Frame(Lfrm_OutR1, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR1.grid(padx=8, pady=8)
                Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR1.grid()
                btn_InR1 = Button(Lfrm_InR1, text="To Do List", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised",
                                  borderwidth=1)
                btn_InR1.grid(padx=10, pady=10)

                Lfrm_OutR2 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR2.grid(row=2, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR2 = Frame(Lfrm_OutR2, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR2.grid(padx=8, pady=8)
                Lfrm_InR2 = LabelFrame(frm_MidR2, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR2.grid()
                btn_InR2 = Button(Lfrm_InR2, text="Set Reminder", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised",
                                  borderwidth=1)
                btn_InR2.grid(padx=10, pady=10)

                Lfrm_OutR3 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR3.grid(row=3, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR3 = Frame(Lfrm_OutR3, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR3.grid(padx=8, pady=8)
                Lfrm_InR3 = LabelFrame(frm_MidR3, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR3.grid()
                btn_InR3 = Button(Lfrm_InR3, text="Sticky Note", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised",
                                  borderwidth=1)
                btn_InR3.grid(padx=10, pady=10)

                Lfrm_OutR4 = LabelFrame(frm_Right, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
                Lfrm_OutR4.grid(row=4, column=0, padx=(50, 0), pady=(20, 10))
                frm_MidR4 = Frame(Lfrm_OutR4, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
                frm_MidR4.grid(padx=8, pady=8)
                Lfrm_InR4 = LabelFrame(frm_MidR4, bg="#cfe0e8", padx=15, pady=20)
                Lfrm_InR4.grid()
                btn_InR4 = Button(Lfrm_InR4, text="Tenant Box", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                  activebackground="#ff6f69", activeforeground="#588c7e", relief="raised",
                                  borderwidth=1)
                btn_InR4.grid(padx=10, pady=10)

                mainloop()


            def shrink():
                frm_Admin.configure(bg="#622569", padx=10, pady=10)

            def normal():
                btn_Admin.configure(font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569")
                btn_Admin.grid_configure(padx=5, pady=5)
                administration()

            frm_Admin.after(1000, shrink)
            btn_Admin.after(1000, normal)

        frm_Admin = Frame(Lfrm_In, bg="#622569", padx=10, pady=10)
        frm_Admin.grid(row=5, rowspan=2, columnspan=3, column=0, padx=10, pady=10)
        btn_Admin = Button(frm_Admin, text="Ad_min_is_tra_to_r", font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569",
                           relief="raised", borderwidth=3, command=adminCommand)
        btn_Admin.grid(padx=5, pady=5)

        def maintainC():
            frm_maintenance.configure(bg="#ffcc5c", padx=0, pady=0)
            btn_maintenance.configure(font=("times", 40), bg="#ffcc5c", fg="#622569")
            btn_maintenance.grid_configure(padx=0, pady=0)

            def shrink():
                frm_maintenance.configure(bg="#622569", padx=10, pady=10)
                '''Lfrm_In.grid_forget()
                Lfrm_InAd = LabelFrame(frm_Mid, bg="#ffcc5c")
                Lfrm_InAd.grid()

                lbl_Ad = Label(Lfrm_InAd, text="Administrator_", bg="#ffcc5c", fg="#622569", font=("times", 30, "bold"))
                lbl_Ad.grid(row=0, column=1, columnspan=4, padx=10, pady=20)
                lbl_User = Label(Lfrm_InAd, text="AdminName: ", bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
                lbl_User.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                lbl_Pass = Label(Lfrm_InAd, text="Pass_Word: ", bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
                lbl_Pass.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

                User_Name = StringVar()
                etr_User = Entry(Lfrm_InAd, textvariable=User_Name, bg="#cfe0e8", fg="#622569", font=("times", 20, "bold"))
                etr_User.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                Pass_Word = StringVar()
                etr_Pass = Entry(Lfrm_InAd, textvariable=Pass_Word, bg="#cfe0e8", fg="#622569", font=("times", 20, "bold"),
                                 show='*')
                etr_Pass.grid(row=2, column=2, columnspan=2, padx=10, pady=20)

                def Validate():
                    if User_Name.get() == '' or Pass_Word.get() == '':
                        messagebox.showerror('Empty Fields', 'User Name and Password Must Be Filled')
                    else:
                        conn = sqlite3.connect('User_Data')
                        cur = conn.cursor()
                        cur.execute("SELECT * FROM user")
                        a = cur.fetchall()
                        # print(a)
                        cur.execute("SELECT * FROM user WHERE user_id=? AND password=?", (User_Name.get(), Pass_Word.get()))
                        c = cur.fetchall()
                        if c:
                            print('Log In Successful')
                        else:
                            print('Log In Failed!!')

                        conn.commit()
                        conn.close()

                btn_Login = Button(frm_Mid, text="Log In", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                                   activeforeground="#588c7e", font=("arial", 15, "bold"), command=Validate)
                btn_Login.grid(padx=2, pady=4)'''

            def normal():
                btn_maintenance.configure(font=("times", 30, "bold"), bg="#e4d1d1", fg="#622569")
                btn_maintenance.grid_configure(padx=5, pady=5)

            frm_maintenance.after(1000, shrink)
            btn_maintenance.after(1000, normal)

        frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=10, pady=10)
        frm_maintenance.grid(row=7, rowspan=2, columnspan=3, column=0, padx=10, pady=10)
        btn_maintenance = Button(frm_maintenance, text="Main_t_e_n_a_n_c_e", font=("times", 30, "bold"), bg="#e4d1d1",
                                 fg="#622569", relief="raised", borderwidth=3, command=maintainC)
        btn_maintenance.grid(padx=5, pady=5)



    def Validatelogin():
        if User_Name.get() == '' or Pass_Word.get() == '':
            messagebox.showerror('Empty Fields', 'User Name and Password Must Be Filled')
        else:
            conn = sqlite3.connect('Gracious_Data')
            Allowed = []
            if conn:
                cur = conn.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS Administrator
                               (Admin_Id text,
                                First_Name text,
                                Last_Name text,
                                Password text)
                            """)
                cur.execute("""CREATE TABLE IF NOT EXISTS User
                                               (User_Id text,
                                                First_Name text,
                                                Last_Name text,
                                                Password text)
                                            """)
                cur.execute("SELECT * FROM Administrator")
                a= cur.fetchall()
                if a:
                    cur.execute("SELECT * FROM Administrator WHERE Admin_Id=? AND Password=?",
                                (User_Name.get(), Pass_Word.get()))
                    c = cur.fetchall()
                    cur.execute("SELECT * FROM User WHERE User_Id=? AND Password=?", (User_Name.get(), Pass_Word.get()))
                    u = cur.fetchall()
                    if c:
                        etr_User.delete(0,END)
                        etr_Pass.delete(0,END)
                        homePage()
                    elif u:
                        etr_User.delete(0, END)
                        etr_Pass.delete(0, END)
                        homePage()
                    else:
                        def fOut():
                            lbl_f.grid_forget()

                        lbl_f = Label(frm_Mid, text='Log In Failed!!!', bg="#cfe0e8", fg="#622569",
                                      font=("times", 12, "bold"))
                        lbl_f.grid()
                        lbl_f.after(3000, fOut)
                else:
                    etr_User.configure(state=DISABLED)
                    etr_Pass.configure(state=DISABLED)
                    vTop = Toplevel()
                    vTop.title('Sign Up As Administrator')
                    vTop.geometry('500x550')
                    vTop.configure(bg="#ffcc5c")
                    Lfrm_top = LabelFrame(vTop, bg="#622569")
                    Lfrm_top.grid(row=1, column=0, padx=20, pady=20)
                    lbl_Aid = Label(Lfrm_top, text="Admin ID : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_Aid.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
                    lbl_Afname = Label(Lfrm_top, text="First Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_Afname.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
                    lbl_Alname = Label(Lfrm_top, text="Last Name : ", bg="#ffcc5c", fg="#622569",
                                      font=("times", 15, "bold"))
                    lbl_Alname.grid(row=2, column=0, columnspan=2, padx=10, pady=20)
                    lbl_Apassword = Label(Lfrm_top, text="Password : ", bg="#ffcc5c", fg="#622569",
                                          font=("times", 15, "bold"))
                    lbl_Apassword.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

                    AdminID = StringVar()
                    etr_AdminID = Entry(Lfrm_top, textvariable=AdminID, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"))
                    etr_AdminID.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
                    Adminf = StringVar()
                    etr_Admnf = Entry(Lfrm_top, textvariable=Adminf, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"))
                    etr_Admnf.grid(row=1, column=2, columnspan=2, padx=10, pady=20)
                    Adminl = StringVar()
                    etr_Admnl = Entry(Lfrm_top, textvariable=Adminl, bg="#c1946a", fg="#622569",
                                       font=("times", 20, "bold"))
                    etr_Admnl.grid(row=2, column=2, columnspan=2, padx=10, pady=20)
                    AdmnPass = StringVar()
                    etr_pw = Entry(Lfrm_top, textvariable=AdmnPass, bg="#c1946a", fg="#622569", show="*",
                                   font=("times", 20, "bold"))
                    etr_pw.grid(row=3, column=2, columnspan=2, padx=10, pady=20)
                    def signUp():
                        if AdminID.get() == '' or Adminf.get() =='' or Adminl.get() =='' or AdmnPass.get() == '':
                            messagebox.showerror('Empty Field', 'You Must Enter All Fields')
                        else:
                            con = sqlite3.connect('Gracious_Data')
                            cr = con.cursor()
                            cr.execute("INSERT INTO Administrator VALUES(?,?,?,?)",(AdminID.get(), Adminf.get(),Adminl.get(),AdmnPass.get()))
                            etr_AdminID.delete(0, END)
                            etr_Admnf.delete(0, END)
                            etr_Admnl.delete(0, END)
                            etr_pw.delete(0, END)
                            etr_AdminID.focus()
                            def suxMesOut():
                                vTop.destroy()
                                homePage()
                            lbl_suxMes = Label(vTop, text=etr_AdminID.get() + ' Successfully Signed Up As Administrator.',
                                               font=("times", 10), bg="#ffcc5c", fg="#622569")
                            lbl_suxMes.grid(row=4, column=0)
                            lbl_suxMes.after(3000, suxMesOut)
                            con.commit()
                            con.close()

                    btn_vTop = Button(vTop, text="Sign Up", bg="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                                      activeforeground="#588c7e", font=("arial", 15, "bold"),
                                      relief="raised", borderwidth=1, command=signUp)
                    btn_vTop.grid(row=2, column=0)
            else:
                def nOut():
                    lbl_nocon.grid_forget()

                lbl_nocon = Label(frm_Mid, text='Cannot Connect To Gracious Database, Sorry.', bg="#cfe0e8", fg="#622569",font=("times", 12, "bold"))
                lbl_nocon.grid()
                lbl_nocon.after(3000, nOut)
            conn.commit()
            conn.close()

    btn_Login = Button(frm_Mid, text="Log In", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                       activeforeground="#588c7e", font=("arial", 15, "bold"), command=Validatelogin)
    btn_Login.grid(padx=2, pady=4)

    master.mainloop()


mainframe.after(16000, logIn)

mainframe.mainloop()