import tkinter
from tkinter import *
from tkinter import ttk
import tkcalendar
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image
import random


win = Tk()
win.title('GRACIOUS APARTMENTS HOME PAGE')
sW = win.winfo_screenwidth()
sH = win.winfo_screenheight()
print("my screen size is: "+ str(sW) +" x "+ str(sH))
aW = sW - 200
aH = sH - 100
posx = (sW/2) - (aW/2)
posy = (sH/2) - (aH/2)
win.geometry(f'{aW}x{aH}+{int(posx)}+{int(posy)}')
win.configure(background="#cfe0e8")
#win.geometry(f'{aW}x{aH}')
#win.geometry('1920x1080')
wW = win.winfo_width()
wH = win.winfo_height()

#Create canvas to win
can_vas = Canvas(win)
can_vas.pack(side=TOP, fill=BOTH, expand=1)

#Create scrollbar widget to bind to canvas
scr_bar = ttk.Scrollbar(win, orient= VERTICAL, command=can_vas.yview)
scr_bar.pack(side=RIGHT, fill=Y)

scr_barx = ttk.Scrollbar(win, orient= HORIZONTAL, command=can_vas.xview)
scr_barx.pack(side=BOTTOM, fill=X)

def on_mousewheel(event):
    can_vas.yview_scroll(int(-1*(event.delta/120)), "units")

can_vas.bind_all("<MouseWheel>", on_mousewheel)

can_vas.configure(yscrollcommand=scr_bar.set)
can_vas.bind('<Configure>', lambda e:can_vas.configure(scrollregion = can_vas.bbox("all")))

can_vas.configure(xscrollcommand=scr_barx.set)
can_vas.bind('<Configure>', lambda e:can_vas.configure(scrollregion = can_vas.bbox("all")))

#Create window in canvas
frm_win = Frame(can_vas)

can_vas.create_window((0,0), window=frm_win, anchor=CENTER)

   
#===============screensize=====1920 x 1080=====================================================================================
wWid = win.winfo_width()
wHeit = win.winfo_height()
x4 = int(wWid/4)
x50 = int(wWid/50)
x100 = int(wWid/100)
x90 = int(wWid/90)
x222 = int(wWid/222)
x20 = int(wWid/20)
x30 = int(wWid/30)
x133 = int(wWid/133)
x200 = int(wWid/200)
x40 = int(wWid/40)
x400 = int(wWid/400)
x250 = int(wWid/250)
Lfrm_Graciousmaster = LabelFrame(frm_win, relief="groove", bg="#ffcc5c")
Lfrm_Graciousmaster.grid(padx=22,pady=9) #x90_22 x222_9
lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura",100,), bg="#ffcc5c", fg="#cfe0e8") #x20_100
lbl_Introg.grid(row=1, column=3)

Lfrm_Outhpage = LabelFrame(frm_win, relief="raised", borderwidth=9, bg="#ffcc5c",padx=65,pady=65) #x222_9 x30_65 x30_65
Lfrm_Outhpage.grid(padx=x4, pady=x50) #x4_480 x50_40
frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=9, bg="#622569",padx=15,pady=15) #x222_9 x133_15 x133_15
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=10, pady=10) #x200_10 x200_10
Lfrm_In.grid()

win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_columnconfigure(0, weight=1)


def houseCommand():
    frm_house.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_house.configure(font=("times",65),bg="#ffcc5c", fg="#622569") #x30_65
    btn_house.grid_configure(padx=0,pady=0)
    def shrink():
        frm_house.configure( bg="#622569", padx=15, pady=15) #x133_15 x133_15
    def normal():
        btn_house.configure(font=("times",50,"bold"), bg="#e4d1d1", fg="#622569") #x40_50
        btn_house.grid_configure(padx=10, pady=10) #x200_10 x200_10

    frm_house.after(1000, shrink)
    btn_house.after(1000, normal)

frm_house = Frame(Lfrm_In, bg="#622569", padx=15, pady=15) #x133_15 x133_15
frm_house.grid(row=1,rowspan=2, columnspan=3, column=0, padx=15, pady=15) #x133_15 x133_15
btn_house = Button(frm_house,text="H_o_u_s_e Accounts", font=("times",50,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=5, command=houseCommand) #x40_50 x 400_5
btn_house.grid(padx=8, pady=8) #x250_8 x250_8

def billCommand():
    frm_bill.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_bill.configure(font=("times",65),bg="#ffcc5c", fg="#622569") #x30_65
    btn_bill.grid_configure(padx=0,pady=0)
    def shrink():
        frm_bill.configure( bg="#622569", padx=15,pady=15)#x133_15 x133_15
    def normal():
        btn_bill.configure(font=("times",50,"bold"), bg="#e4d1d1", fg="#622569") #x40_50
        btn_bill.grid_configure(padx=10, pady=10) #x200_10 x200_10

    frm_bill.after(1000, shrink)
    btn_bill.after(1000, normal)

frm_bill = Frame(Lfrm_In, bg="#622569", padx=15,pady=15) #x133_15 x133_15
frm_bill.grid(row=3,rowspan=2, columnspan=3, column=0, padx=15, pady=15) #x133_15 x133_15
btn_bill = Button(frm_bill,text="B_i_l_l Man_age_r_", font=("times",50,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=5, command=billCommand) #x40_50 x400_5
btn_bill.grid(padx=10, pady=10) #x200_10 x200_10

def adminCommand():
    frm_Admin.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_Admin.configure(font=("times",65),bg="#ffcc5c", fg="#622569") #x30_65
    btn_Admin.grid_configure(padx=0,pady=0)
    def shrink():
        frm_Admin.configure( bg="#622569", padx=15,pady=15) #x133_15 x133_15
    def normal():
        btn_Admin.configure(font=("times",50,"bold"), bg="#e4d1d1", fg="#622569") #x40_59
        btn_Admin.grid_configure(padx=8, pady=8) #x250_8 x250_8

    frm_Admin.after(1000, shrink)
    btn_Admin.after(1000, normal)

frm_Admin = Frame(Lfrm_In, bg="#622569", padx=15,pady=15) #x133_15 x133_15
frm_Admin.grid(row=5,rowspan=2, columnspan=3, column=0, padx=15, pady=15) #x133_15 x133_15
btn_Admin = Button(frm_Admin,text="Ad_min_is_tra_to_r", font=("times",50,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=5, command=adminCommand) #x40_50 x400_5
btn_Admin.grid(padx=10, pady=10) #x200_10 x200_10

def maintainC():
    frm_maintenance.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_maintenance.configure(font=("times",65),bg="#ffcc5c", fg="#622569") #x30_65
    btn_maintenance.grid_configure(padx=0,pady=0)
    def shrink():
        frm_maintenance.configure( bg="#622569", padx=15,pady=15) #x133_15 x133_15

    def normal():
        btn_maintenance.configure(font=("times",50,"bold"), bg="#e4d1d1", fg="#622569") #x40_5 
        btn_maintenance.grid_configure(padx=10, pady=10) #x200_10 x200_10

    frm_maintenance.after(1000, shrink)
    btn_maintenance.after(1000, normal)

frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=15,pady=15) #x133_15 x133_15
frm_maintenance.grid(row=7,rowspan=2, columnspan=3, column=0, padx=15, pady=15) #x133_15 x133_15
btn_maintenance = Button(frm_maintenance,text="Main_t_e_n_a_n_c_e", font=("times",50,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=5,command=maintainC) #x40_50 x400_5
btn_maintenance.grid(padx=10, pady=10) #x200_10 x200_10

#Function to print size of tk window
def print_width():
   wW = win.winfo_width()
   print("The width of Tkinter window:", wW)
   print("The height of Tkinter window:", win.winfo_height())
# Create a Label
lbl_winfo = Label(Lfrm_In, text="Click the below Button to Print the Height and width of the Screen", font=('Helvetica 10 bold'))
lbl_winfo.grid(row=8,rowspan=2, columnspan=3, column=0, padx=x133, pady=x133) #x133_15 x133_15
# Create a Button for print function
btn_winfo = Button(Lfrm_In, text="Click", command=print_width)
btn_winfo.grid(row=9,rowspan=2, columnspan=3, column=1, padx=x133, pady=x133) #x133_15 x133_15

#=========================================================================================================================================================================

'''#===============screensize=====1536 x 864=====================================================================================
Lfrm_Graciousmaster = LabelFrame(frm_win, relief="groove", bg="#ffcc5c")
Lfrm_Graciousmaster.grid(padx=17,pady=7)
lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura",80,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)

Lfrm_Outhpage = LabelFrame(frm_win, relief="raised", borderwidth=7, bg="#ffcc5c",padx=52,pady=52)
Lfrm_Outhpage.grid(padx=360, pady=32)
frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=7, bg="#622569",padx=12,pady=12)
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=7, pady=8)
Lfrm_In.grid()

def houseCommand():
    frm_house.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_house.configure(font=("times",52),bg="#ffcc5c", fg="#622569")
    btn_house.grid_configure(padx=0,pady=0)
    def shrink():
        frm_house.configure( bg="#622569", padx=12,pady=12)
    def normal():
        btn_house.configure(font=("times",40,"bold"), bg="#e4d1d1", fg="#622569")
        btn_house.grid_configure(padx=8, pady=8)

    frm_house.after(1000, shrink)
    btn_house.after(1000, normal)

frm_house = Frame(Lfrm_In, bg="#622569", padx=12, pady=12)
frm_house.grid(row=1,rowspan=2, columnspan=3, column=0, padx=12, pady=12)
btn_house = Button(frm_house,text="H_o_u_s_e Accounts", font=("times",40,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=4, command=houseCommand)
btn_house.grid(padx=6, pady=6)

def billCommand():
    frm_bill.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_bill.configure(font=("times",52),bg="#ffcc5c", fg="#622569")
    btn_bill.grid_configure(padx=0,pady=0)
    def shrink():
        frm_bill.configure( bg="#622569", padx=12,pady=12)
    def normal():
        btn_bill.configure(font=("times",40,"bold"), bg="#e4d1d1", fg="#622569")
        btn_bill.grid_configure(padx=8, pady=8)

    frm_bill.after(1000, shrink)
    btn_bill.after(1000, normal)

frm_bill = Frame(Lfrm_In, bg="#622569", padx=12,pady=12)
frm_bill.grid(row=3,rowspan=2, columnspan=3, column=0, padx=12, pady=12)
btn_bill = Button(frm_bill,text="B_i_l_l Man_age_r_", font=("times",40,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=4, command=billCommand)
btn_bill.grid(padx=8, pady=8)

def adminCommand():
    frm_Admin.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_Admin.configure(font=("times",52),bg="#ffcc5c", fg="#622569")
    btn_Admin.grid_configure(padx=0,pady=0)
    def shrink():
        frm_Admin.configure( bg="#622569", padx=12,pady=12)
    def normal():
        btn_Admin.configure(font=("times",40,"bold"), bg="#e4d1d1", fg="#622569")
        btn_Admin.grid_configure(padx=8, pady=8)

    frm_Admin.after(1000, shrink)
    btn_Admin.after(1000, normal)

frm_Admin = Frame(Lfrm_In, bg="#622569", padx=12,pady=12)
frm_Admin.grid(row=5,rowspan=2, columnspan=3, column=0, padx=12, pady=12)
btn_Admin = Button(frm_Admin,text="Ad_min_is_tra_to_r", font=("times",40,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=4, command=adminCommand)
btn_Admin.grid(padx=8, pady=8)

def maintainC():
    frm_maintenance.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_maintenance.configure(font=("times",52),bg="#ffcc5c", fg="#622569")
    btn_maintenance.grid_configure(padx=0,pady=0)
    def shrink():
        frm_maintenance.configure( bg="#622569", padx=12,pady=12)

    def normal():
        btn_maintenance.configure(font=("times",40,"bold"), bg="#e4d1d1", fg="#622569")
        btn_maintenance.grid_configure(padx=8, pady=8)

    frm_maintenance.after(1000, shrink)
    btn_maintenance.after(1000, normal)

frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=12,pady=12)
frm_maintenance.grid(row=7,rowspan=2, columnspan=3, column=0, padx=12, pady=12)
btn_maintenance = Button(frm_maintenance,text="Main_t_e_n_a_n_c_e", font=("times",40,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=4,command=maintainC)
btn_maintenance.grid(padx=8, pady=8)

#========================================================================================================================================================================='''

'''#===============screensize=====1280 x 720=====================================================================================
Lfrm_Graciousmaster = LabelFrame(frm_win, relief="groove", bg="#ffcc5c")
Lfrm_Graciousmaster.grid(padx=13,pady=5)
lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura",60,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)

Lfrm_Outhpage = LabelFrame(frm_win, relief="raised", borderwidth=5, bg="#ffcc5c",padx=39,pady=39)
Lfrm_Outhpage.grid(padx=270, pady=24)
frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=5, bg="#622569",padx=9,pady=9)
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=5, pady=6)
Lfrm_In.grid()

def houseCommand():
    frm_house.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_house.configure(font=("times",39),bg="#ffcc5c", fg="#622569")
    btn_house.grid_configure(padx=0,pady=0)
    def shrink():
        frm_house.configure( bg="#622569", padx=9,pady=9)
    def normal():
        btn_house.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_house.grid_configure(padx=6, pady=6)

    frm_house.after(1000, shrink)
    btn_house.after(1000, normal)

frm_house = Frame(Lfrm_In, bg="#622569", padx=9, pady=9)
frm_house.grid(row=1,rowspan=2, columnspan=3, column=0, padx=9, pady=9)
btn_house = Button(frm_house,text="H_o_u_s_e Accounts", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=houseCommand)
btn_house.grid(padx=6, pady=6)

def billCommand():
    frm_bill.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_bill.configure(font=("times",39),bg="#ffcc5c", fg="#622569")
    btn_bill.grid_configure(padx=0,pady=0)
    def shrink():
        frm_bill.configure( bg="#622569", padx=9,pady=9)
    def normal():
        btn_bill.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_bill.grid_configure(padx=6, pady=6)

    frm_bill.after(1000, shrink)
    btn_bill.after(1000, normal)

frm_bill = Frame(Lfrm_In, bg="#622569", padx=9,pady=9)
frm_bill.grid(row=3,rowspan=2, columnspan=3, column=0, padx=9, pady=9)
btn_bill = Button(frm_bill,text="B_i_l_l Man_age_r_", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=billCommand)
btn_bill.grid(padx=6, pady=6)

def adminCommand():
    frm_Admin.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_Admin.configure(font=("times",39),bg="#ffcc5c", fg="#622569")
    btn_Admin.grid_configure(padx=0,pady=0)
    def shrink():
        frm_Admin.configure( bg="#622569", padx=9,pady=9)
    def normal():
        btn_Admin.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_Admin.grid_configure(padx=6, pady=6)

    frm_Admin.after(1000, shrink)
    btn_Admin.after(1000, normal)

frm_Admin = Frame(Lfrm_In, bg="#622569", padx=9,pady=9)
frm_Admin.grid(row=5,rowspan=2, columnspan=3, column=0, padx=9, pady=9)
btn_Admin = Button(frm_Admin,text="Ad_min_is_tra_to_r", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=adminCommand)
btn_Admin.grid(padx=6, pady=6)

def maintainC():
    frm_maintenance.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_maintenance.configure(font=("times",39),bg="#ffcc5c", fg="#622569")
    btn_maintenance.grid_configure(padx=0,pady=0)
    def shrink():
        frm_maintenance.configure( bg="#622569", padx=9,pady=9)

    def normal():
        btn_maintenance.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_maintenance.grid_configure(padx=6, pady=6)

    frm_maintenance.after(1000, shrink)
    btn_maintenance.after(1000, normal)

frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=9,pady=9)
frm_maintenance.grid(row=7,rowspan=2, columnspan=3, column=0, padx=9, pady=9)
btn_maintenance = Button(frm_maintenance,text="Main_t_e_n_a_n_c_e", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3,command=maintainC)
btn_maintenance.grid(padx=6, pady=6)

#========================================================================================================================================================================='''

'''#===============screensize 360 x 640====x 780============x 800=====390 x 844=====412 x 915=============================
Lfrm_Graciousmaster = LabelFrame(frm_win, relief="groove", bg="#ffcc5c")
Lfrm_Graciousmaster.grid(padx=13,pady=5)
lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura",20,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)

Lfrm_Outhpage = LabelFrame(frm_win, relief="raised", borderwidth=5, bg="#ffcc5c",padx=13,pady=13)
Lfrm_Outhpage.grid(padx=90, pady=8)
frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=5, bg="#622569",padx=3,pady=3)
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=5, pady=6)
Lfrm_In.grid()

def houseCommand():
    frm_house.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_house.configure(font=("times",13),bg="#ffcc5c", fg="#622569")
    btn_house.grid_configure(padx=0,pady=0)
    def shrink():
        frm_house.configure( bg="#622569", padx=3,pady=3)
    def normal():
        btn_house.configure(font=("times",10,"bold"), bg="#e4d1d1", fg="#622569")
        btn_house.grid_configure(padx=2, pady=2)

    frm_house.after(1000, shrink)
    btn_house.after(1000, normal)

frm_house = Frame(Lfrm_In, bg="#622569", padx=3, pady=3)
frm_house.grid(row=1,rowspan=2, columnspan=3, column=0, padx=3, pady=3)
btn_house = Button(frm_house,text="H_o_u_s_e Accounts", font=("times",10,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=1, command=houseCommand)
btn_house.grid(padx=2, pady=2)

def billCommand():
    frm_bill.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_bill.configure(font=("times",13),bg="#ffcc5c", fg="#622569")
    btn_bill.grid_configure(padx=0,pady=0)
    def shrink():
        frm_bill.configure( bg="#622569", padx=3,pady=3)
    def normal():
        btn_bill.configure(font=("times",10,"bold"), bg="#e4d1d1", fg="#622569")
        btn_bill.grid_configure(padx=2, pady=2)

    frm_bill.after(1000, shrink)
    btn_bill.after(1000, normal)

frm_bill = Frame(Lfrm_In, bg="#622569", padx=3,pady=3)
frm_bill.grid(row=3,rowspan=2, columnspan=3, column=0, padx=3, pady=3)
btn_bill = Button(frm_bill,text="B_i_l_l Man_age_r_", font=("times",10,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=billCommand)
btn_bill.grid(padx=2, pady=2)

def adminCommand():
    frm_Admin.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_Admin.configure(font=("times",13),bg="#ffcc5c", fg="#622569")
    btn_Admin.grid_configure(padx=0,pady=0)
    def shrink():
        frm_Admin.configure( bg="#622569", padx=3,pady=3)
    def normal():
        btn_Admin.configure(font=("times",10,"bold"), bg="#e4d1d1", fg="#622569")
        btn_Admin.grid_configure(padx=2, pady=2)

    frm_Admin.after(1000, shrink)
    btn_Admin.after(1000, normal)

frm_Admin = Frame(Lfrm_In, bg="#622569", padx=3,pady=3)
frm_Admin.grid(row=5,rowspan=2, columnspan=3, column=0, padx=3, pady=3)
btn_Admin = Button(frm_Admin,text="Ad_min_is_tra_to_r", font=("times",10,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=1, command=adminCommand)
btn_Admin.grid(padx=2, pady=2)

def maintainC():
    frm_maintenance.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_maintenance.configure(font=("times",13),bg="#ffcc5c", fg="#622569")
    btn_maintenance.grid_configure(padx=0,pady=0)
    def shrink():
        frm_maintenance.configure( bg="#622569", padx=3,pady=3)

    def normal():
        btn_maintenance.configure(font=("times",10,"bold"), bg="#e4d1d1", fg="#622569")
        btn_maintenance.grid_configure(padx=2, pady=2)

    frm_maintenance.after(1000, shrink)
    btn_maintenance.after(1000, normal)

frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=3,pady=3)
frm_maintenance.grid(row=7,rowspan=2, columnspan=3, column=0, padx=10, pady=10)
btn_maintenance = Button(frm_maintenance,text="Main_t_e_n_a_n_c_e", font=("times",10,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=1,command=maintainC)
btn_maintenance.grid(padx=2, pady=2)

#=========================================================================================='''
'''Lfrm_Graciousmaster = LabelFrame(frm_win, relief="groove", bg="#ffcc5c")
Lfrm_Graciousmaster.grid(padx=100,pady=50)
lbl_Introg = Label(Lfrm_Graciousmaster, text="GRACIOUS APARTMENTS", font=("futura",85,), bg="#ffcc5c", fg="#cfe0e8")
lbl_Introg.grid(row=1, column=3)'''

'''Lfrm_Outhpage = LabelFrame(frm_win, text="Welcome Grace",font=("arial",5), relief="raised", borderwidth=5, bg="#ffcc5c",padx=40,pady=40)
Lfrm_Outhpage.grid(padx=500, pady=50)
frm_Mid = Frame(Lfrm_Outhpage, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_Mid.grid()
Lfrm_In = LabelFrame(frm_Mid, bg="#cfe0e8", padx=15, pady=20)
Lfrm_In.grid()'''

'''def houseCommand():
    frm_house.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_house.configure(font=("times",40),bg="#ffcc5c", fg="#622569")
    btn_house.grid_configure(padx=0,pady=0)
    def shrink():
        frm_house.configure( bg="#622569", padx=10,pady=10)
    def normal():
        btn_house.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_house.grid_configure(padx=5, pady=5)

    frm_house.after(1000, shrink)
    btn_house.after(1000, normal)'''


'''frm_house = Frame(Lfrm_In, bg="#622569", padx=10,pady=10)
frm_house.grid(row=1,rowspan=2, columnspan=3, column=0, padx=10, pady=10)
btn_house = Button(frm_house,text="H_o_u_s_e Accounts", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=houseCommand)
btn_house.grid(padx=5, pady=5)'''

'''def billCommand():
    frm_bill.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_bill.configure(font=("times",40),bg="#ffcc5c", fg="#622569")
    btn_bill.grid_configure(padx=0,pady=0)
    def shrink():
        frm_bill.configure( bg="#622569", padx=10,pady=10)
    def normal():
        btn_bill.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_bill.grid_configure(padx=5, pady=5)

    frm_bill.after(1000, shrink)
    btn_bill.after(1000, normal)

frm_bill = Frame(Lfrm_In, bg="#622569", padx=10,pady=10)
frm_bill.grid(row=3,rowspan=2, columnspan=3, column=0, padx=10, pady=10)
btn_bill = Button(frm_bill,text="B_i_l_l Man_age_r_", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=billCommand)
btn_bill.grid(padx=5, pady=5)'''

'''def adminCommand():
    frm_Admin.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_Admin.configure(font=("times",40),bg="#ffcc5c", fg="#622569")
    btn_Admin.grid_configure(padx=0,pady=0)
    def shrink():
        frm_Admin.configure( bg="#622569", padx=10,pady=10)
    def normal():
        btn_Admin.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_Admin.grid_configure(padx=5, pady=5)

    frm_Admin.after(1000, shrink)
    btn_Admin.after(1000, normal)

frm_Admin = Frame(Lfrm_In, bg="#622569", padx=10,pady=10)
frm_Admin.grid(row=5,rowspan=2, columnspan=3, column=0, padx=10, pady=10)
btn_Admin = Button(frm_Admin,text="Ad_min_is_tra_to_r", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3, command=adminCommand)
btn_Admin.grid(padx=5, pady=5)'''

'''def maintainC():
    frm_maintenance.configure(bg="#ffcc5c",padx=0,pady=0)
    btn_maintenance.configure(font=("times",40),bg="#ffcc5c", fg="#622569")
    btn_maintenance.grid_configure(padx=0,pady=0)
    def shrink():
        frm_maintenance.configure( bg="#622569", padx=10,pady=10)

        Lfrm_In.grid_forget()
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

'''def normal():
        btn_maintenance.configure(font=("times",30,"bold"), bg="#e4d1d1", fg="#622569")
        btn_maintenance.grid_configure(padx=5, pady=5)

    frm_maintenance.after(1000, shrink)
    btn_maintenance.after(1000, normal)

frm_maintenance = Frame(Lfrm_In, bg="#622569", padx=10,pady=10)
frm_maintenance.grid(row=7,rowspan=2, columnspan=3, column=0, padx=10, pady=10)
btn_maintenance = Button(frm_maintenance,text="Main_t_e_n_a_n_c_e", font=("times",30,"bold"), bg="#e4d1d1", fg="#622569", relief="raised", borderwidth=3,command=maintainC)
btn_maintenance.grid(padx=5, pady=5)'''

mainloop()