from tkinter import *
from tkinter import ttk
import tkcalendar
import sqlite3
from tkinter import messagebox
import tempfile
import os
from PIL import ImageTk, Image
import random
from tkcalendar import *
import datetime
from datetime import date,timedelta


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

Lfrm_OutCwat = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c",padx=10,pady=30)
Lfrm_OutCwat.grid(row=1, column=1, rowspan=2, columnspan=3, padx=20)
frm_MidC = Frame(Lfrm_OutCwat, relief="raised", borderwidth=5, bg="#622569",padx=10,pady=10)
frm_MidC.grid(row=1, column=0)
Lfrm_InC = LabelFrame(frm_MidC, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC.grid(row=0, column=0,columnspan=2)

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

Lfrm_OutL1wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=40,pady=40)
Lfrm_OutL1wat.grid(row=1, column=0,padx=(15,50), pady=10)
frm_MidL1 = Frame(Lfrm_OutL1wat, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL1.grid(row=1, column=0, padx=60,pady=15)
lbl_pageAd = Label(Lfrm_OutL1wat, text="View_ And_ Process_ Bills", bg="#ffcc5c", fg="#622569", font=("times",18))
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
    if housebill.get()=='':
        messagebox.showerror('Apartment Not Selected','You Must Select Apartment')
    else:
        lbl_OutC = Label(Lfrm_OutCwat, text="Admin/User Log In", font=("times", 15, "bold"), bg="#ffcc5c", fg="#622569")
        lbl_OutC.grid(row=0, column=0)
        lbl_usid = Label(Lfrm_InC, text="_User_Id_ : ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_usid.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
        lbl_passw= Label(Lfrm_InC,    text="_Password_: ", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
        lbl_passw.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        UserName = StringVar()
        etr_usid = Entry(Lfrm_InC, textvariable=UserName, bg="#c1946a", fg="#622569", font=("times", 20, "bold"))
        etr_usid.grid(row=0, column=2, columnspan=2, padx=10, pady=20)
        passw = StringVar()
        etr_passw = Entry(Lfrm_InC, textvariable=passw, bg="#c1946a", fg="#622569", font=("times", 20, "bold"),show='*')
        etr_passw.grid(row=1, column=2, columnspan=2, padx=10, pady=20)

        def BillDetails():
            Lfrm_OutL1wat.grid_forget()
            Lfrm_OutL2wat.grid_forget()
            Lfrm_OutCwat.grid_forget()
            Lfrm_OutR1wat.grid_forget()

            conn = sqlite3.connect('Gracious_Data')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS Apartment_MeterNo
                        (Apart_Name text,
                         House_No text,
                         Meter_No text)
                        """)
            cur.execute("SELECT Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?",(housebill.get(),))
            c = cur.fetchall()
            num = len(c)

            Lfrm_OutL1Bd = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=40, pady=40)
            Lfrm_OutL1Bd.grid(row=1, column=0, padx=(15, 50), pady=10)
            frm_MidL1Bd = Frame(Lfrm_OutL1Bd, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
            frm_MidL1Bd.grid(row=1, column=0, padx=60, pady=15)
            lbl_pageAdBd = Label(Lfrm_OutL1Bd, text=housebill.get(), bg="#ffcc5c", fg="#622569", font=("times", 18))
            lbl_pageAdBd.grid(row=0, column=0)
            lbl_pageAdBdnum = Label(Lfrm_OutL1Bd, text="Number of Meters: "+str(num), bg="#ffcc5c", fg="#622569", font=("times", 10))
            lbl_pageAdBdnum.grid(row=1, column=0)
            conn.commit()
            conn.close()

            Lfrm_OutL2Bd = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c", padx=10, pady=10)
            Lfrm_OutL2Bd.grid(row=2, column=0, padx=(5, 50), pady=50, rowspan=2)
            frm_MidL2Bd = Frame(Lfrm_OutL2Bd, relief="raised", borderwidth=3, bg="#622569", padx=3, pady=3)
            frm_MidL2Bd.grid(padx=15, pady=15)
            Lfrm_InL2Bd = LabelFrame(frm_MidL2Bd, bg="#cfe0e8", padx=15, pady=20)
            Lfrm_InL2Bd.grid()

            Lfrm_OutCBd = LabelFrame(master, relief="raised", borderwidth=5, bg="#ffcc5c", padx=10, pady=30)
            Lfrm_OutCBd.grid(row=1, column=1, rowspan=3, columnspan=5, padx=20)
            frm_MidCBd = Frame(Lfrm_OutCBd, relief="raised", borderwidth=5, bg="#622569", padx=10, pady=10)
            frm_MidCBd.grid(row=1, column=0)
            Lfrm_InCBd = LabelFrame(frm_MidCBd, bg="#cfe0e8", padx=15, pady=20)
            Lfrm_InCBd.grid(row=0, column=0, columnspan=2)

            def ProcessBills():
                btn_InL2Bdview.configure(state=DISABLED)
                btn_InL2BdPro.configure(state=DISABLED)
                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                cur = conn.cursor()
                cur.execute("SELECT Hse_No,Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?", (housebill.get(),))
                c = cur.fetchall()
                frm_readings = Frame(Lfrm_InCBd, bg="#622569", padx=5, pady=5)
                frm_readings.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
                lbl_hsnum = Label(frm_readings, text="House No", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
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
                        btn_bilday.configure(fg="green",bg="yellow")
                        bil = str(cal1.get_date())
                        lbl_bil.configure(text=bil)
                        cal1.grid_forget()
                        btn_cal1.grid_forget()
                        btn_res1.grid_forget()
                    def Resbil():
                        lbl_bil.configure(text='')

                    btn_bilday.configure(bg="green",fg="yellow")
                    cal1.grid(row=1, column=1, columnspan=3)
                    btn_cal1 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10), command=Savebil)
                    btn_cal1.grid(row=2,column=1)
                    btn_res1 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue", font=("arial", 10), command=Resbil)
                    btn_res1.grid(row=2, column=2)


                def Issday():
                    cal1.grid_forget()
                    cal3.grid_forget()
                    def Saveiss():
                        btn_issday.configure(fg="green",bg="yellow")
                        iss = str(cal2.get_date())
                        lbl_iss.configure(text=iss)
                        cal2.grid_forget()
                        btn_cal2.grid_forget()
                        btn_res2.grid_forget()
                    def Resiss():
                        lbl_iss.configure(text='')

                    btn_issday.configure(bg="green", fg="yellow")
                    cal2.grid(row=1, column=1, columnspan=3)
                    btn_cal2 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10), command=Saveiss)
                    btn_cal2.grid(row=2, column=1)
                    btn_res2 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue", font=("arial", 10), command=Resiss)
                    btn_res2.grid(row=2, column=2)

                def Dueday():
                    cal1.grid_forget()
                    cal2.grid_forget()
                    def Savedue():
                        btn_dueday.configure(fg="green",bg="yellow")
                        due = str(cal3.get_date())
                        lbl_due.configure(text=due)
                        cal3.grid_forget()
                        btn_cal3.grid_forget()
                        btn_res3.grid_forget()
                    def Resdue():
                        lbl_due.configure(text='')

                    btn_dueday.configure(bg="green", fg="yellow")
                    cal3.grid(row=1, column=1, columnspan=3)
                    btn_cal3 = Button(Lfrm_cal, text="Save", bg="yellow", fg="blue", font=("arial", 10), command=Savedue)
                    btn_cal3.grid(row=2, column=1)
                    btn_res3 = Button(Lfrm_cal, text="Reset", bg="yellow", fg="blue", font=("arial", 10),command=Resdue)
                    btn_res3.grid(row=2, column=2)

                Lfrm_cal = LabelFrame(frm_readings,bg="#ffcc5c",padx=10,pady=10,borderwidth=5)
                Lfrm_cal.grid(row=1, column=0)
                Lfrm_UnitEtr = LabelFrame(frm_readings,fg="#622569",bg="#ffcc5c",padx=10,pady=10)
                Lfrm_UnitEtr.grid(row=2,column=0)
                lbl_UnitEtr = Label(Lfrm_UnitEtr,text="Price Per Unit: ",bg="#ffcc5c", fg="#622569", font=("times",15))
                lbl_UnitEtr.grid(row=0,column=0,padx=5,pady=10)
                UnitEtr = IntVar()
                etr_UnitEtr = Entry(Lfrm_UnitEtr, textvariable=UnitEtr, bg="#cfe0e8",fg="#622569",font=("times",10,"bold"), justify=RIGHT)
                etr_UnitEtr.grid(row=0, column=1,padx=5,pady=10,columnspan=2)
                etr_UnitEtr.delete(0,END)

                Lfrm_opt = LabelFrame(Lfrm_cal, bg="#622569", padx=5, pady=5)
                Lfrm_opt.grid(row=0, column=0, padx=5)
                months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
                lbl_mon = Label(Lfrm_opt,text="Month",bg="yellow", fg="green",font=("times",10))
                lbl_mon.grid(row=0,column=0,pady=1)
                bilmon = StringVar()
                opt_bilmon = OptionMenu(Lfrm_opt, bilmon, *months)
                opt_bilmon.grid(row=1, column=0)

                Lfrm_btn1 = LabelFrame(Lfrm_cal,bg="#622569", padx=3,pady=3)
                Lfrm_btn1.grid(row=0,column=1,padx=5)
                btn_bilday = Button(Lfrm_btn1,text="Bill Day",bg="yellow",fg="green",activeforeground="yellow",
                                    command=Bilday, font=("helvetica",10,"bold"),activebackground="green",relief="raised")
                btn_bilday.grid(row=0,column=0)
                lbl_bil  = Label(Lfrm_btn1,text="",bg="#ffcc5c", fg="#622569", font=("times",10))
                lbl_bil.grid(row=1,column=0)
                tex1 = datetime.datetime.today()
                cal1 = Calendar(Lfrm_cal, selectmode="day", year=tex1.year, month=tex1.month, day=tex1.day)
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
                btn_issday = Button(Lfrm_btn2, text="Issue Day", bg="yellow", fg="green", activeforeground="yellow",
                                    command=Issday,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_issday.grid(row=0, column=0)
                lbl_iss = Label(Lfrm_btn2, text="", bg="#ffcc5c", fg="#622569", font=("times", 10))
                lbl_iss.grid(row=1, column=0)
                tex2 = datetime.datetime.today()
                #datetime
                cal2 = Calendar(Lfrm_cal, selectmode="day", year=tex2.year, month=tex2.month, day=tex2.day)
                cal2.grid_forget()

                Lfrm_btn3 = LabelFrame(Lfrm_cal, bg="#622569", padx=3, pady=3)
                Lfrm_btn3.grid(row=0, column=3, padx=5)
                btn_dueday = Button(Lfrm_btn3, text="Due Day", bg="yellow", fg="green", activeforeground="yellow",
                                    command=Dueday,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_dueday.grid(row=0, column=0)
                lbl_due = Label(Lfrm_btn3, text="", bg="#ffcc5c", fg="#622569", font=("times", 10))
                lbl_due.grid(row=1, column=0)
                tex3 = datetime.datetime.today()
                cal3 = Calendar(Lfrm_cal, selectmode="day", year=tex3.year, month=tex3.month, day=tex3.day)
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
                br.execute("SELECT Previous FROM Prev_Readings WHERE Apart_Name=?",(housebill.get(),))
                bills = br.fetchall()
                print(bills)
                count = 0
                Previous = []
                Current = []
                try:
                    if bills:
                        for hs, mtr in c:
                            lbl_hs = Label(LFrm_readings, text=hs, bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                            lbl_hs.grid(row=count, column=0)
                            lbl_mtr = Label(LFrm_readings, text=mtr, bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                            lbl_mtr.grid(row=count, column=1)
                            Prev = IntVar()
                            etr_prev = Entry(LFrm_readings, textvariable=Prev, bg="#c1946a", fg="#622569", font=("times", 15, "bold"), justify=RIGHT)
                            etr_prev.grid(row=count, column=2)
                            try:
                                etr_prev.insert(END,bills[count])
                                etr_prev.configure(state=DISABLED)
                            except:
                                etr_prev.insert(END,'')
                            Previous.append(etr_prev)
                            Curr = IntVar()
                            etr_curr = Entry(LFrm_readings, textvariable=Curr, bg="#c1946a", fg="#622569",
                                             font=("times", 15, "bold"), justify=RIGHT)
                            etr_curr.grid(row=count, column=3)
                            etr_curr.delete(0,END)
                            Current.append(etr_curr)
                            count += 1
                    else:
                        for hs, mtr in c:
                            lbl_hs = Label(LFrm_readings, text=hs, bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                            lbl_hs.grid(row=count, column=0)
                            lbl_mtr = Label(LFrm_readings, text=mtr, bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                            lbl_mtr.grid(row=count, column=1)
                            Prev = IntVar()
                            etr_prev = Entry(LFrm_readings, textvariable=Prev, bg="#c1946a", fg="#622569", font=("times", 15, "bold"), justify=RIGHT)
                            etr_prev.grid(row=count, column=2)
                            etr_prev.delete(0,END)
                            Previous.append(etr_prev)
                            Curr = IntVar()
                            etr_curr = Entry(LFrm_readings, textvariable=Curr, bg="#c1946a", fg="#622569",
                                             font=("times", 15, "bold"), justify=RIGHT)
                            etr_curr.grid(row=count, column=3)
                            etr_curr.delete(0,END)
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
                    '''if UnitEtr.get() == 0:
                        messagebox.showerror('Missing Entry','Fill in Unit Price')'''

                    if bilmon.get()=='':
                        messagebox.showerror('Month Not Selected','Select The Month Of The Bill.')
                    if cal1floaty== cal2floaty == cal3floaty:
                        if cal1floatj== cal2floatj == cal3floatj:
                            messagebox.showerror('No Entry', 'Fill All Entries Required To Process Bill.')
                        elif cal1floatj > cal2floatj:
                            messagebox.showerror('Invalid Date','Bill Date Cannot Be Later Than Issue Date.')
                        elif cal2floatj > cal3floatj:
                            messagebox.showerror('Invalid Date', 'Issue Date Cannot Be Later Than Due Date.')
                        elif cal1floatj > cal3floatj:
                            messagebox.showerror('Invalid Date', 'Bill Date Cannot Be Later Than Due Date.')
                    if cal1floaty < cal2floaty or cal1floaty < cal3floaty:
                        if cal1floatm != str(12) or j >1 or f >1:
                            messagebox.showerror('Invalid Date', 'Cannot Allow To Process This Bill.')
                    else:
                        conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                        cur = conn.cursor()
                        cur.execute("SELECT Meter_No FROM Apartment_MeterNo WHERE Apart_Name=?",(housebill.get(),))
                        c = cur.fetchall()
                        cur.execute("SELECT Hse_No FROM Apartment_MeterNo WHERE Apart_Name=?", (housebill.get(),))
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
                        LFrm_readingsE = LabelFrame(frm_readings, bg="#cfe0e8", padx=5, pady=5, borderwidth=5)
                        LFrm_readingsE.grid(row=1, column=0, columnspan=11, padx=10)
                        p = len(Previous)
                        cr = len(Current)
                        '''dayone = date.today().replace(day=1)
                        daylastmon = dayone - timedelta(days=1)
                        lastmon = daylastmon.strftime('%b')'''
                        def printProcess():
                            con = sqlite3.connect('ProjoZ_SysAdminTest1')
                            cr = con.cursor()
                            cr.execute("DELETE FROM Prev_Readings WHERE Apart_Name=?", (housebill.get(),))

                            LFrm_readingsE.grid_forget()
                            #btn_readEdit.grid_forget()
                            #btn_printProcess.grid_forget()
                            btn_readExit.grid_forget()
                            LFrm_readingsP = LabelFrame(frm_readings, bg="#cfe0e8", padx=5, pady=5, borderwidth=5)
                            LFrm_readingsP.grid(row=1, column=0, columnspan=12, padx=10)



                            #===============================Text Area=================================================
                            text_receipt = Text(LFrm_readingsP, width=56, bg="#daebe8", fg="blue",
                                                font=("times", 15, "bold"))
                            text_receipt.grid(row=0, column=0, columnspan=11)

                            x = 0
                            f = open(housebill.get() + bilmon.get() + str(tex1.year) + ".txt", 'w')
                            fA = open(housebill.get()+bilmon.get()+str(tex1.year)+"agent.txt", 'w')
                            fA.write("   "+housebill.get().upper()+" "+bilmon.get()+" "+str(tex1.year)+"\n")
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
                                    text_receipt.insert(END, " House No.- "+str(h[x])+"| Meter No.- "+str(c[x])+"\n")
                                    text_receipt.insert(END,"_____________________________________________\n")
                                    text_receipt.insert(END,"| Month | Bill Date | Issue Date | Due Date |\n")
                                    text_receipt.insert(END, "------------------------------------------------\n")
                                    text_receipt.insert(END,"|  "+bilmon.get()+"  | "+cal1.get_date()+" |  "+cal2.get_date()+"  | "+cal3.get_date()+"  |\n")
                                    text_receipt.insert(END, "_______________________________________________\n")
                                    text_receipt.insert(END,"| Previous | Current | Units | Price | Amount |\n")
                                    text_receipt.insert(END, "------------------------------------------------\n")
                                    text_receipt.insert(END,"|     "+pvxE+"   |     "+cvxE+"  |    "+str(usedE)+"  |    "+str(etr_UnitEtr.get())+" |   "+str(amtE)+"  |\n")
                                    text_receipt.insert(END, "________________________________________________________\n\n\n\n\n")
                                    cr.execute("SELECT Year,Month FROM Water_Bills WHERE Apart_Name=?",(housebill.get(),))
                                    ym = cr.fetchall()
                                    existing = []
                                    mas = datetime.datetime.now()
                                    masaa = mas.strftime("%c")
                                    mwaka = mas.strftime("%Y")
                                    siku = mas.strftime("%j")
                                    for yr,mt in ym:
                                        if yr == cal3floaty and mt ==cal3floatb:
                                            existing.append(yr)
                                    if existing:
                                        messagebox.showerror('Existing Record','The Bill for This Month And Year Already Exists\nWater Bill Once Processed Cannot Be Changed.')
                                        print(existing)
                                    if cal1floaty == mwaka:
                                        if cal1floatj > siku:
                                            messagebox.showerror('Invalid Date','Cannot Allow Processing Of Bill Due To Wrong Bill Date.')
                                    else:
                                        cr.execute("INSERT INTO Water_Bills VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                (housebill.get(),str(h[x]),str(c[x]),bilmon.get(),cal1.get_date(),cal2.get_date(),cal3.get_date(),pvxE,cvxE,str(usedE),str(amtE),cal3floaty,cal3floatb,tz))
                                        cr.execute("INSERT INTO Prev_Readings VALUES(?,?)",(housebill.get(),cvxE))
                                        f.write(str(h[x])+'-'+str(c[x])+'-'+bilmon.get()+'-'+cal1.get_date()+'-'+cal2.get_date()+'-'+cal3.get_date()+'-'+pvxE+'-'+cvxE+'-'+str(usedE)+'-'+str(amtE)+'-'+cal3floaty+'-'+cal3floatb+'-'+tz+'\n')
                                        fA.write(str(h[x]) + ' | ' + str(c[x]) + ' | ' + pvxE + ' | ' + cvxE + ' | ' + str(usedE) + ' | ' + str(amtE) + '\n')
                                        #print("Done 'n Dusted")
                                else:
                                    text_receipt.insert(END, " House No.- " + str(h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                    text_receipt.insert(END, "_____________________________________________\n")
                                    text_receipt.insert(END, "| Month | Bill Date | Issue Date | Due Date |\n")
                                    text_receipt.insert(END, "------------------------------------------------\n")
                                    text_receipt.insert(END, "|  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                    text_receipt.insert(END, "_______________________________________________\n")
                                    text_receipt.insert(END, "| Previous | Current | Units | Price | Amount |\n")
                                    text_receipt.insert(END, "------------------------------------------------\n")
                                    text_receipt.insert(END, "|     " + pvx + "   |     " + cvx + "  |    " + str(used) + "  |    " + str(etr_UnitEtr.get()) + " |   " + str(amt) + "  |\n")
                                    text_receipt.insert(END, "________________________________________________________\n\n\n\n\n")
                                    cr.execute("INSERT INTO Water_Bills VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                (housebill.get(), str(h[x]), str(c[x]), bilmon.get(), cal1.get_date(), cal2.get_date(), cal3.get_date(), pvx, cvx, str(used), str(amt), cal3floaty, cal3floatb, tz))
                                    cr.execute("INSERT INTO Prev_Readings VALUES(?,?)", (housebill.get(), cvx))
                                    f.write(str(h[x]) + '-' + str(c[x]) + '-' + bilmon.get() + '-' + cal1.get_date() + '-' + cal2.get_date() + '-' + cal3.get_date() + '-' + pvx + '-' + cvx + '-' + str(used) + '-' + str() + '-' + cal3floaty + '-' + cal3floatb + '-' + tz + '\n')
                                    fA.write(str(h[x]) + ' | ' + str(c[x]) + ' | ' + pvx + ' | ' + cvx + ' | ' + str(used) + ' | ' + str(amtE) + '\n')
                                    #print("Done 'n Done")
                                x += 1
                            f.close()
                            fA.close()
                            con.commit()
                            con.close()
                            text_receipt.configure(state=DISABLED)

                            scr_bar = ttk.Scrollbar(LFrm_readingsP, orient=VERTICAL, command=text_receipt.yview)
                            text_receipt['yscrollcommand'] = scr_bar.set
                            scr_bar.grid(row=0, column=11, sticky="E")
                            def SaveForFiling():
                                btn_printFile.grid_forget()
                                btn_printProcessE.grid_forget()
                                def sffOut():
                                    lbl_sff.grid_forget()
                                lbl_sff = Label(Lfrm_InCBd,text="Saved Successfully! You Can Go To 'View Bills' To View.",
                                                font=("times",10,"bold"),bg="#ffcc5c", fg="#622569")
                                lbl_sff.grid(row=1,column=1)
                                lbl_sff.after(5000,sffOut)
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
                                            text_bills.insert(END, "      "+housebill.get().upper()+"   APARTMENTS   \n")
                                            text_bills.insert(END,"   ______________________________________________\n")
                                            text_bills.insert(END, "    House No.- " + str(h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                            text_bills.insert(END, "   _____________________________________________\n")
                                            text_bills.insert(END, "   | Month | Bill Date | Issue Date | Due Date |\n")
                                            text_bills.insert(END, "   ------------------------------------------------\n")
                                            text_bills.insert(END, "   |  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                            text_bills.insert(END, "   _______________________________________________\n")
                                            text_bills.insert(END, "   | Previous | Current | Units | Price | Amount |\n")
                                            text_bills.insert(END, "   ------------------------------------------------\n")
                                            text_bills.insert(END, "   |     " + pvxE+ "   |     " + cvxE + "  |    " +str(usedE) + "  |    " + str(etr_UnitEtr.get()) + " |   " + str(amtE) + "  |\n")
                                            text_bills.insert(END,"   _____________________________________________________\n")
                                            text_bills.insert(END,"    NB/Your supply shall be liable for disconnection \n    if not settled within 5 days from the date of issue \n    without any further notice. \n   In addition you will pay a reconnection fee of Kshs 1000\n")
                                            text_bills.insert(END,"   _____________________________________________________\n\n")
                                        else:
                                            text_bills.insert(END, "      "+housebill.get().upper()+"   APARTMENTS   \n")
                                            text_bills.insert(END, "   ______________________________________________\n")
                                            text_bills.insert(END, "    House No.- " + str(h[x]) + "| Meter No.- " + str(c[x]) + "\n")
                                            text_bills.insert(END, "   _____________________________________________\n")
                                            text_bills.insert(END, "   | Month | Bill Date | Issue Date | Due Date |\n")
                                            text_bills.insert(END, "   ------------------------------------------------\n")
                                            text_bills.insert(END, "   |  " + bilmon.get() + "  | " + cal1.get_date() + " |  " + cal2.get_date() + "  | " + cal3.get_date() + "  |\n")
                                            text_bills.insert(END, "   _______________________________________________\n")
                                            text_bills.insert(END, "   | Previous | Current | Units | Price | Amount |\n")
                                            text_bills.insert(END, "   ------------------------------------------------\n")
                                            text_bills.insert(END, "   |  " + pvx + "   |     " + cvx + "  |    " + str(used) + "  |    " + str(etr_UnitEtr.get()) + " |   " + str(amt) + "  |\n")
                                            text_bills.insert(END, "   _____________________________________________________\n")
                                            text_bills.insert(END, "    NB/Your supply shall be liable for disconnection \n    if not settled within 5 days from the date of issue \n    without any further notice. \n   In addition you will pay a reconnection fee of Kshs 1000\n")
                                            text_bills.insert(END, "   _____________________________________________________\n\n")
                                        x += 1
                                    text_bills.configure(state=DISABLED)

                                    scr_barB = ttk.Scrollbar(LFrm_readingsP, orient=VERTICAL, command=text_bills.yview)
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

                                btn_printBill = Button(frm_readings, text="Print Bills", background="#588c7e",
                                                       fg="#ff6f69",
                                                       command=PrintForBilling, activebackground="#ff6f69",
                                                       activeforeground="#588c7e", font=("arial", 15, "bold"))
                                btn_printBill.grid(row=2, column=3)
                                btn_billExit = Button(frm_readings, text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                                       command=billExit, activebackground="#ff6f69",
                                                       activeforeground="#588c7e", font=("arial", 15, "bold"))
                                btn_billExit.grid(row=2, column=4)
                            def printExit():
                                frm_readings.grid_forget()
                                btn_InL2Bdview.configure(state=NORMAL)
                                btn_InL2BdPro.configure(state=NORMAL)




                            #=========================================================================================

                            btn_printFile = Button(frm_readings, text="Save For Filing", background="#588c7e", fg="#ff6f69",
                                                      command=SaveForFiling,activebackground="#ff6f69", activeforeground="#588c7e", font=("arial", 15, "bold"))
                            btn_printFile.grid(row=2, column=3)
                            btn_printExit = Button(frm_readings, text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                                  command=printExit, activebackground="#ff6f69", activeforeground="#588c7e",font=("arial", 15, "bold"))
                            btn_printExit.grid(row=2, column=4)



                        if p == cr:
                            x = 0
                            msg = ''
                            lbl_bilmon = Label(frm_readings, text="Month", bg="#ffcc5c", fg="#622569", font=("times", 10, "bold"))
                            lbl_bilmon.grid(row=0, column=0)

                            lbl_bilday = Label(frm_readings, text="Bill_Day", bg="#ffcc5c", fg="#622569",
                                               font=("times", 10, "bold"))
                            lbl_bilday.grid(row=0, column=1)

                            lbl_issday = Label(frm_readings, text="Issue_Day", bg="#ffcc5c", fg="#622569",
                                               font=("times", 10, "bold"))
                            lbl_issday.grid(row=0, column=2)

                            lbl_dueday = Label(frm_readings, text="Due_ Day", bg="#ffcc5c", fg="#622569",
                                               font=("times", 10, "bold"))
                            lbl_dueday.grid(row=0, column=3)

                            lbl_hsnumP = Label(frm_readings, text="House_No", bg="#ffcc5c", fg="#622569",
                                               font=("times", 10, "bold"))
                            lbl_hsnumP.grid(row=0, column=4)

                            lbl_mtrnumP = Label(frm_readings, text="Meter_No", bg="#ffcc5c", fg="#622569",
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
                                        msg += str(Current[x].get())+' is less than '+ str(Previous[x].get())+'\n'
                                        used = int(Current[x].get()) - int(Previous[x].get())
                                        px = str(Previous[x].get())
                                        cx = str(Current[x].get())
                                        # print(used)
                                        mon = tex1.month
                                        amt = used * UnitEtr.get()
                                        etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                          font=("times", 10, "bold"), justify=RIGHT, width=10)
                                        etr_Month.grid(row=x, column=0)
                                        etr_Month.insert(END, bilmon.get())
                                        etr_Month.configure(state=DISABLED)

                                        etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                         font=("times", 10, "bold"), justify=RIGHT, width=10)
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
                                        #print(used)
                                        mon = tex1.month
                                        amtE = usedE * UnitEtr.get()
                                        etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"), justify=RIGHT, width=10)
                                        etr_Month.grid(row=x,column=0)
                                        etr_Month.insert(END, bilmon.get())
                                        etr_Month.configure(state=DISABLED)

                                        etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),justify=RIGHT, width=10)
                                        etr_BilE.grid(row=x, column=1)
                                        etr_BilE.insert(END, str(cal1.get_date()))
                                        etr_BilE.configure(state=DISABLED)

                                        etr_IssE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_IssE.grid(row=x, column=2)
                                        etr_IssE.insert(END, str(cal2.get_date()))
                                        etr_IssE.configure(state=DISABLED)

                                        etr_DueE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_DueE.grid(row=x, column=3)
                                        etr_DueE.insert(END, str(cal3.get_date()))
                                        etr_DueE.configure(state=DISABLED)

                                        etr_Hno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Hno.grid(row=x, column=4)
                                        etr_Hno.insert(END, h[x])
                                        etr_Hno.configure(state=DISABLED)

                                        etr_Mno = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Mno.grid(row=x, column=5)
                                        etr_Mno.insert(END, c[x])
                                        etr_Mno.configure(state=DISABLED)

                                        etr_Pread = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Pread.grid(row=x, column=6)
                                        etr_Pread.insert(END, px)
                                        etr_Pread.configure(state=DISABLED)
                                        prevEdit.append(etr_Pread)

                                        etr_Cread = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Cread.grid(row=x, column=7)
                                        etr_Cread.insert(END, cx)
                                        etr_Cread.configure(state=DISABLED)
                                        currEdit.append(etr_Cread)

                                        etr_Qtt = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times",10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Qtt.grid(row=x, column=8)
                                        etr_Qtt.insert(END, str(usedE))
                                        etr_Qtt.configure(state=DISABLED)

                                        etr_Price = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Price.grid(row=x, column=9)
                                        etr_Price.insert(END, str(etr_UnitEtr.get()))
                                        etr_Price.configure(state=DISABLED)

                                        etr_Amount = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569", font=("times", 10, "bold"),
                                                          justify=RIGHT, width=10)
                                        etr_Amount.grid(row=x, column=10)
                                        etr_Amount.insert(END, str(amtE))
                                        etr_Amount.configure(state=DISABLED)
                                    x += 1
                                except:
                                    messagebox.showerror('Invalid Entry','Insert "0" If Their Is No Reading On Current Meter No Or No Unit Price.')

                            if inRed:
                                inRed2 = []
                                def readEdit():
                                    x = 0
                                    msgE =''
                                    for mtr in prevEdit:
                                        try:
                                            if currEdit[x].get() < prevEdit[x].get():
                                                msgE += str(currEdit[x].get()) + ' is less than ' + str(prevEdit[x].get()) + '\n'
                                                usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                pvx = str(prevEdit[x].get())
                                                cvx = str(currEdit[x].get())
                                                # print(usedE)
                                                mon = tex1.month
                                                amtE = usedE * UnitEtr.get()
                                                etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                  font=("times", 10, "bold"), justify=RIGHT, width=10)
                                                etr_Month.grid(row=x, column=0)
                                                etr_Month.insert(END, bilmon.get())
                                                etr_Month.configure(state=DISABLED)

                                                etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                 font=("times", 10, "bold"), justify=RIGHT, width=10)
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
                                                etr_Pread.insert(END, pvx)
                                                etr_Pread.configure(state=NORMAL)
                                                prevEdit.clear()
                                                prevEdit.append(etr_Pread)

                                                etr_Cread = Entry(LFrm_readingsE, bg="#c1946a", fg="red",
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
                                                etr_Amount.insert(END, str(amtE))
                                                etr_Amount.configure(state=NORMAL)
                                                print('Current Reading Cannot Be Less Than Previous: ' + msgE)
                                                inRed2.append(currEdit[x])
                                                btn_readEdit.grid_forget()
                                            else:
                                                usedE = int(currEdit[x].get()) - int(prevEdit[x].get())
                                                pvx = str(prevEdit[x].get())
                                                cvx = str(currEdit[x].get())
                                                # print(used)
                                                mon = tex1.month
                                                amtE = usedE * UnitEtr.get()
                                                etr_Month = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                  font=("times", 10, "bold"), justify=RIGHT, width=10)
                                                etr_Month.grid(row=x, column=0)
                                                etr_Month.insert(END, bilmon.get())
                                                etr_Month.configure(state=DISABLED)

                                                etr_BilE = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                 font=("times", 10, "bold"), justify=RIGHT, width=10)
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
                                                etr_Pread.insert(END, pvx)
                                                etr_Pread.configure(state=DISABLED)

                                                etr_Cread = Entry(LFrm_readingsE, bg="#c1946a", fg="#622569",
                                                                  font=("times", 10, "bold"),
                                                                  justify=RIGHT, width=10)
                                                etr_Cread.grid(row=x, column=7)
                                                etr_Cread.insert(END, cvx)
                                                etr_Cread.configure(state=DISABLED)

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
                                            messagebox.showerror('Invalid Entry','Insert "0" If Their Is No Reading On Current Meter No Or No Unit Price.')
                                    if inRed2:
                                        pass
                                    else:
                                        btn_readEdit.grid_forget()
                                        btn_printProcessE = Button(frm_readings, text="Process_ Bill",
                                                                  background="#588c7e",
                                                                  fg="#ff6f69",
                                                                  command=printProcess, activebackground="#ff6f69",
                                                                  activeforeground="#588c7e",
                                                                  font=("arial", 15, "bold"))
                                        btn_printProcessE.grid(row=2, column=3)


                                btn_readEdit = Button(frm_readings, text="E_D_I_T", background="#588c7e", fg="#ff6f69",
                                                      command=readEdit, activebackground="#ff6f69",
                                                      activeforeground="#588c7e", font=("arial", 15, "bold"))
                                btn_readEdit.grid(row=2, column=2)
                            else:
                                btn_printProcessE = Button(frm_readings, text="Process_ Bill", background="#588c7e",
                                                      fg="#ff6f69",
                                                      command=printProcess, activebackground="#ff6f69",
                                                      activeforeground="#588c7e",
                                                      font=("arial", 15, "bold"))
                                btn_printProcessE.grid(row=2, column=3)

                                #print(Previous[0].get())
                                #print(Current[0].get()
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


                btn_readProcess = Button(frm_readings, text="Process_ Bill", background="#588c7e", fg="#ff6f69",
                                         command=readProcess,activebackground="#ff6f69", activeforeground="#588c7e",
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
                Lfrm_Vbills = LabelFrame(Lfrm_InCBd, relief="raised", borderwidth=3, bg="#622569", padx=5, pady=5)
                Lfrm_Vbills.grid(row=1, column=0, columnspan=3)
                lbl_nodata = Label(Lfrm_Vbills, text="No Data Available For Selected Year And Month",
                                   bg="#ffcc5c", fg="#622569", font=("times", 20, "bold"))
                lbl_nodata.grid_forget()

                
                janlist = []
                btnList = []
                '''feblist = []
                marlist = []
                aprlist = []
                maylist = []
                junlist = []
                jullist = []
                auglist = []
                seplist = []
                octlist = []
                novlist = []
                declist = []'''
#===============================Jan===============Button====================================================================================================================================
                def mon(month,row):
                    janlist.clear()
                    #lbl_nodata.grid_forget()
                                                                                                    
                    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                    cur = conn.cursor()
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(), month))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vjan = ttk.Treeview(Lfrm_Vbills)
                    tree_vjan.grid(row=1, column=2, columnspan=10)
                    tree_vjan['columns'] = ('n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vjan.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vjan.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vjan.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()

                    lbl_hno = Label(Lfrm_Vbills, text= 'House No')
                    lbl_hno.grid(row=3, column=2)
                    lbl_mtr = Label(Lfrm_Vbills, text= 'Meter No')
                    lbl_mtr.grid(row=3, column=3)
                    '''lbl_mon = Label(Lfrm_Vbills, text= 'Month')
                    lbl_mon.grid(row=3, column=4)
                    lbl_bil = Label(Lfrm_Vbills, text= 'Bill Date')
                    lbl_bil.grid(row=3, column=5)
                    lbl_iss = Label(Lfrm_Vbills, text= 'Issue Date')
                    lbl_iss.grid(row=3, column=6)
                    lbl_due = Label(Lfrm_Vbills, text= 'Due Date')
                    lbl_due.grid(row=3, column=7)'''
                    lbl_prev = Label(Lfrm_Vbills, text= 'Previous')
                    lbl_prev.grid(row=3, column=8)
                    lbl_curr = Label(Lfrm_Vbills, text= 'Current')
                    lbl_curr.grid(row=3, column=9)
                    lbl_units = Label(Lfrm_Vbills, text= 'Units')
                    lbl_units.grid(row=3, column=10)
                    lbl_amt = Label(Lfrm_Vbills, text= 'Amount')
                    lbl_amt.grid(row=3, column=11)

                    etrHsno = StringVar()
                    etr_hno = Entry(Lfrm_Vbills, textvariable= etrHsno)
                    etr_hno.grid(row=4, column=2)
                    etrMtno = StringVar()
                    etr_mtr = Entry(Lfrm_Vbills, textvariable= etrMtno)
                    etr_mtr.grid(row=4, column=3)
                    etrMon = StringVar()
                    etr_mon = Entry(Lfrm_Vbills, textvariable= etrMon, state=DISABLED)
                    
                    etrBil = StringVar()
                    etr_bil = Entry(Lfrm_Vbills, textvariable= etrBil, state=DISABLED)
                    
                    etrIss = StringVar()
                    etr_iss = Entry(Lfrm_Vbills, textvariable= etrIss, state=DISABLED)
                    
                    etrDue = StringVar()
                    etr_due = Entry(Lfrm_Vbills, textvariable= etrDue, state=DISABLED)
                    
                    etrPrev = StringVar()
                    etr_prev = Entry(Lfrm_Vbills, textvariable= etrPrev)
                    etr_prev.grid(row=4, column=8)
                    etrCurr = StringVar()
                    etr_curr = Entry(Lfrm_Vbills, textvariable= etrCurr)
                    etr_curr.grid(row=4, column=9)
                    etrUnits = StringVar()
                    etr_units = Entry(Lfrm_Vbills, textvariable= etrUnits)
                    etr_units.grid(row=4, column=10)
                    etrAmt = StringVar()
                    etr_amt = Entry(Lfrm_Vbills, textvariable= etrAmt)
                    etr_amt.grid(row=4, column=11)

                    '''#Edit selected record on treeview
                    def EditSelected():
                        etr_hsno.delete(0, END)
                        etr_mtr.delete(0, END)
                        etr_prev.delete(0, END)
                        etr_curr.delete(0, END)
                        etr_units.delete(0, END)
                        etr_amt.delete(0, END)
                        selected = tree_vdec.focus()
                        value = tree_vdec.item(selected, 'values')
                        # val1 = value[0]
                        # entry_hse entry_f entry_l entry_id entry_cont
                        etr_hsno.insert(0, value[0])
                        etr_mtr.insert(0, value[1])
                        etr_prev.insert(0, value[2])
                        etr_curr.insert(0, value[3])
                        etr_units.insert(0, value[4])
                        etr_amt.insert(0, value[5])
                        
                        selected = tree_vdec.focus()
                        tree_ten.item(selected, text='', values=(etr_hsno.get(), etr_mtr.get(), etr_prev.get(), etr_curr.get(), etr_units.get(), etr_amt.get()))

                        x = tree_vdec.selection()
                        for rec in x:
                            tree_vdec.set(rec)'''
                    def insert_values(event):
                        etr_hno.configure(state=NORMAL)
                        etr_mtr.configure(state=NORMAL)
                        etr_mon.configure(state=NORMAL)
                        etr_bil.configure(state=NORMAL)
                        etr_iss.configure(state=NORMAL)
                        etr_due.configure(state=NORMAL)
                        etr_units.configure(state=NORMAL)
                        etr_amt.configure(state=NORMAL)
                        etr_hno.delete(0, END)
                        etr_mtr.delete(0, END)
                        etr_mon.delete(0, END)
                        etr_bil.delete(0, END)
                        etr_iss.delete(0, END)
                        etr_due.delete(0, END)
                        etr_prev.delete(0, END)
                        etr_curr.delete(0, END)
                        etr_units.delete(0, END)
                        etr_amt.delete(0, END)
                        selected = tree_vjan.focus()
                        value = tree_vjan.item(selected, 'values')
                        print(value)
                        # val1 = value[0]
                        # entry_hse entry_f entry_l entry_id entry_cont
                        etr_hno.insert(0, str(value[1]))
                        etr_hno.configure(state=DISABLED)
                        etr_mtr.insert(0, str(value[2]))
                        etr_mtr.configure(state=DISABLED)
                        etr_mon.insert(0, str(value[3]))
                        etr_bil.insert(0, str(value[4]))
                        etr_iss.insert(0, str(value[5]))
                        etr_due.insert(0, str(value[6]))
                        etr_prev.insert(0, str(value[7]))
                        etr_curr.insert(0, str(value[8]))
                        etr_units.insert(0, str(value[9]))
                        etr_units.configure(state=DISABLED)
                        etr_amt.insert(0, str(value[10]))
                        etr_amt.configure(state=DISABLED)

                        def editVbills():
                            etr_hno.configure(state=NORMAL)
                            etr_mtr.configure(state=NORMAL)
                            etr_units.configure(state=NORMAL)
                            etr_amt.configure(state=NORMAL)
                            if etr_prev.get() == '' or etr_curr.get() == '':
                                messagebox.showerror('No entry','Previous Reading and Current Reading Cannot Be Empty!')
                            elif etr_curr.get() < etr_prev.get():
                                messagebox.showerror('Wrong Entry','Current Reading Cannot Be Less Than Previous Reading!')
                            else:
                                new_units = int(etr_curr.get()) - int(etr_prev.get())
                                unit_price = int(etr_amt.get())/int(etr_units.get())
                                new_amount = new_units * unit_price
                                conn = sqlite3.connect('ProjoZ_SysAdminTest1')
                                cur = conn.cursor()
                                '''EXISTS Water_Bills
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
                                      Date_Time text)'''
                                cur.execute("UPDATE Water_Bills SET Previous=?,Current=?,Units=?,Amount=? WHERE Apart_Name=? AND House_No=? AND Bil_Month=?",
                                            ((etr_prev.get(),etr_curr.get(),new_units, new_amount, housebill.get(), etr_hno.get(),month)))
                                conn.commit()
                                conn.close()
                                etr_hno.configure(state=NORMAL)
                                etr_mtr.configure(state=NORMAL)
                                etr_units.configure(state=NORMAL)
                                etr_amt.configure(state=NORMAL)

                                selected = tree_vjan.focus()
                                tree_vjan.item(selected, text='', values=('e',etr_hno.get(), etr_mtr.get(), etr_mon.get(),etr_bil.get(),etr_iss.get(),etr_due.get(),etr_prev.get(), etr_curr.get(), new_units, int(new_amount)))

                                x = tree_vjan.selection()
                                for rec in x:
                                    tree_vjan.set(rec)

                                etr_hno.delete(0, END)
                                etr_mtr.delete(0, END)
                                etr_mon.delete(0, END)
                                etr_bil.delete(0, END)
                                etr_iss.delete(0, END)
                                etr_due.delete(0, END)
                                etr_prev.delete(0, END)
                                etr_curr.delete(0, END)
                                etr_units.delete(0, END)
                                etr_amt.delete(0, END)
                                etr_hno.configure(state=DISABLED)
                                etr_mtr.configure(state=DISABLED)
                                etr_units.configure(state=DISABLED)
                                etr_amt.configure(state=DISABLED)
                                btn_editVbills.grid_forget()
                                
                                
                        btn_editVbills = Button(Lfrm_InCBd, relief="raised",text="E_D_I_T", background="#588c7e", fg="#ff6f69",
                                                            command=editVbills,activebackground="#ff6f69", activeforeground="#588c7e", font=("arial", 15, "bold"))
                        btn_editVbills.grid(row=2, column=1)
                        
                    tree_vjan.bind('<ButtonRelease-1>', insert_values)

                def exitVbills():
                    Lfrm_Vbills.grid_forget()
                    btn_exitVbills.grid_forget()
                    btn_InL2Bdview.configure(state=NORMAL)
                    btn_InL2BdPro.configure(state=NORMAL)

                btn_exitVbills = Button(Lfrm_InCBd, relief="raised",text="E_X_I_T", background="#588c7e", fg="#ff6f69",
                                                    command=exitVbills,activebackground="#ff6f69", activeforeground="#588c7e", font=("arial", 15, "bold"))
                btn_exitVbills.grid(row=2, column=2)

                
                frm_months = Frame(Lfrm_Vbills,bg="#ffcc5c",pady=5,padx=5)
                frm_months.grid(row=1,column=0)
                monList = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',]
                                
                row = 0 
                for month in monList:
                    btn_mon = Button(frm_months, text=month, bg="yellow", fg="green", activeforeground="yellow", command=lambda k=month, r=row: mon(k,r), font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                    btn_mon.grid(row=row, column=0)
                    btnList.append(btn_mon)
                    row += 1                   
                    
#=================================Feb===============Button==============================================================================================================================
                '''def feb():
                    feblist.clear()
                    #lbl_nodata.grid_forget()
                    btn_feb.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),''))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vfeb = ttk.Treeview(Lfrm_Vbills)
                    tree_vfeb.grid(row=1, column=2, columnspan=10)
                    tree_vfeb['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vfeb.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vfeb.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vfeb.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#==================================March====================Button==========================================================================================================
                def mar():
                    marlist.clear()
                    #lbl_nodata.grid_forget()
                    btn_mar.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Mar'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vmar = ttk.Treeview(Lfrm_Vbills)
                    tree_vmar.grid(row=1, column=2, columnspan=10)
                    tree_vmar['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vmar.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vmar.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vmar.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#==============================April===============But=======================================================================================================================
                def apr():
                    aprlist.clear()
                    #lbl_nodata.grid_forget()
                    btn_apr.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Apr'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vapr = ttk.Treeview(Lfrm_Vbills)
                    tree_vapr.grid(row=1, column=2, columnspan=10)
                    tree_vapr['columns'] = ('n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vapr.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vapr.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vapr.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#==================================May==================But=====================================================================================================================
                def may():
                    maylist.clear()
                    #lbl_nodata.grid_forget()
                    btn_may.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'May'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vmay = ttk.Treeview(Lfrm_Vbills)
                    tree_vmay.grid(row=1, column=2, columnspan=10)
                    tree_vmay['columns'] = ('n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vmay.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vmay.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vmay.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#=============================================June=================But===================================================================================================================
                def jun():
                    junlist.clear()
                    #lbl_nodata.grid_forget()
                    btn_jun.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Jun'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vjun = ttk.Treeview(Lfrm_Vbills)
                    tree_vjun.grid(row=1, column=2, columnspan=10)
                    tree_vjun['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vjun.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vjun.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vjun.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#=================================July==================But=================================================================================================================
                def jul():
                    jullist.clear()
                    #lbl_nodata.grid_forget()
                    btn_jul.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Jul'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vjul = ttk.Treeview(Lfrm_Vbills)
                    tree_vjul.grid(row=1, column=2, columnspan=10)
                    tree_vjul['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vjul.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vjul.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vjul.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#================================Aug===================But====================================================================================================================
                def aug():
                    auglist.clear()
                    #lbl_nodata.grid_forget()
                    btn_aug.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Aug'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vaug = ttk.Treeview(Lfrm_Vbills)
                    tree_vaug.grid(row=1, column=2, columnspan=10)
                    tree_vaug['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vaug.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vaug.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vaug.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#============================================September=======But============================================================================================================
                def sep():
                    seplist.clear()
                    #lbl_nodata.grid_forget()
                    btn_sep.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Sep'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vsep = ttk.Treeview(Lfrm_Vbills)
                    tree_vsep.grid(row=1, column=2, columnspan=10)
                    tree_vsep['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vsep.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vsep.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vsep.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#==================================October==================But==================================================================================================================
                def oct():
                    octlist.clear()
                    #lbl_nodata.grid_forget()
                    btn_oct.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Oct'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_voct = ttk.Treeview(Lfrm_Vbills)
                    tree_voct.grid(row=1, column=2, columnspan=10)
                    tree_voct['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_voct.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_voct.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_voct.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#=================================November====================But==============================================================================================================
                def nov():
                    novlist.clear()
                    #lbl_nodata.grid_forget()
                    btn_nov.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Nov'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vnov = ttk.Treeview(Lfrm_Vbills)
                    tree_vnov.grid(row=1, column=2, columnspan=10)
                    tree_vnov['columns'] = ('n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vnov.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vnov.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vnov.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
#================================December======================But================================================================================================================
                def dec():
                    declist.clear()
                    #lbl_nodata.grid_forget()
                    btn_dec.configure( bg="green", fg="yellow")
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
                    cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Bil_Month=?",
                                (housebill.get(), Year.get(),'Dec'))
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
                    style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'blue')])
                    tree_vdec = ttk.Treeview(Lfrm_Vbills)
                    tree_vdec.grid(row=1, column=2, columnspan=10)
                    tree_vdec['columns'] = (
                    'n', 'hsno', 'mtrno', 'bilm', 'billd', 'issd', 'dued', 'prev', 'curr', 'units', 'amount')
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
                                tree_vdec.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('evenrow',))
                            else:
                                tree_vdec.insert(parent='', index=END, iid=str(num),values=(n, hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                            num += 1
                            n += 1
                    else:
                        tree_vbills.grid_forget()
                        tree_vdec.grid_forget()
                        lbl_nodata.grid(row=2,column=2, columnspan=10)
                    conn.commit()
                    conn.close()
                    tree_vnov.grid_forget()
                    tree_voct.grid_forget()
                    tree_vsep.grid_forget()
                    tree_vaug.grid_forget()
                    tree_vjul.grid_forget()
                    tree_vjun.grid_forget()
                    tree_vmay.grid_forget()
                    tree_vapr.grid_forget()
                    tree_vmar.grid_forget()
                    tree_vfeb.grid_forget()
                    tree_vjan.grid_forget()'''
                    
#=====================================================================================================================================================================================
                
                '''btn_jan = Button(frm_months,text="Jan", bg="yellow", fg="green", activeforeground="yellow",command=jan,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_jan.grid(row=0,column=0)
                btn_feb = Button(frm_months, text="Feb", bg="yellow", fg="green", activeforeground="yellow",command=feb,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_feb.grid(row=1, column=0)
                btn_mar = Button(frm_months, text="Mar", bg="yellow", fg="green", activeforeground="yellow",command=mar,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_mar.grid(row=2, column=0)
                btn_apr = Button(frm_months, text="Apr", bg="yellow", fg="green", activeforeground="yellow",command=apr,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_apr.grid(row=3, column=0)
                btn_may = Button(frm_months, text="May", bg="yellow", fg="green", activeforeground="yellow",command=may,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_may.grid(row=4, column=0)
                btn_jun = Button(frm_months, text="Jun", bg="yellow", fg="green", activeforeground="yellow",command=jun,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_jun.grid(row=5, column=0)
                btn_jul = Button(frm_months, text="Jul", bg="yellow", fg="green", activeforeground="yellow",command=jul,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_jul.grid(row=6, column=0)
                btn_aug = Button(frm_months, text="Aug", bg="yellow", fg="green", activeforeground="yellow",command=aug,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_aug.grid(row=7, column=0)
                btn_sep = Button(frm_months, text="Sep", bg="yellow", fg="green", activeforeground="yellow",command=sep,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_sep.grid(row=8, column=0)
                btn_oct = Button(frm_months, text="Oct", bg="yellow", fg="green", activeforeground="yellow",command=oct,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_oct.grid(row=9, column=0)
                btn_nov = Button(frm_months, text="Nov", bg="yellow", fg="green", activeforeground="yellow",command=nov,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_nov.grid(row=10, column=0)
                btn_dec = Button(frm_months, text="Dec", bg="yellow", fg="green", activeforeground="yellow",command=dec,font=("helvetica", 10, "bold"), activebackground="green", relief="raised")
                btn_dec.grid(row=11, column=0)'''

                frm_year = Frame(Lfrm_Vbills, bg="#622569", pady=10, padx=10)
                frm_year.grid(row=1, column=1)
                yr = datetime.datetime.today()
                ry = str(yr.strftime("%Y"))
                md = str(yr.strftime("%b"))
                Year = IntVar()
                etr_year = Entry(frm_year, textvariable=Year, bg="#c1946a", fg="#622569",font=("times", 15, "bold"),justify=RIGHT, width=5)
                etr_year.grid(row=1)
                etr_year.delete(0,END)
                etr_year.insert(END,ry)

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
                tree_vbills.grid(row=1,column=2)
                tree_vbills['columns']= ('n','hsno','mtrno','bilm','billd','issd','dued','prev','curr','units','amount')
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
                tree_vbills.heading('hsno',text='House No')
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
                cur.execute("SELECT House_No,Meter_No,Bil_Month,Bill_Date,Iss_Date,Due_Date,Previous,Current,Units,Amount FROM Water_Bills WHERE Apart_Name=? AND Year=? AND Month=?",(housebill.get(),ry,md))
                vb = cur.fetchall()
                if vb:
                    num = 0
                    n = 1
                    for hs,mtr,bil,bill,iss,due,prev,curr,unit,amount in vb:
                        tree_vbills.tag_configure('evenrow', background="white")
                        tree_vbills.tag_configure('oddrow', background="lightblue")
                        if num % 2 ==0:
                            tree_vbills.insert(parent='',index=END,iid=str(num),values=(n,hs,mtr,bil,bill,iss,due,prev,curr,unit,amount), tags=('evenrow',))
                        else:
                            tree_vbills.insert(parent='', index=END, iid=str(num),values=(n,hs, mtr, bil, bill, iss, due, prev, curr, unit, amount),tags=('oddrow',))
                        num += 1
                        n += 1
                else:
                    tree_vbills.grid_forget()
                    lbl_nodata.grid(row=1,column=2)
                conn.commit()
                conn.close()

            btn_InL2Bd= Button(Lfrm_InL2Bd, text="B_A_C_K_ T_O_ S_E_L_E_C_T", font=("times", 10), bg="#cfe0e8", fg="#622569",
                               command=BackSelect,activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1, )
            btn_InL2Bd.grid(padx=10, pady=10)

            btn_InL2BdPro = Button(Lfrm_InL2Bd, text="P_R_O_C_E_S_S_ B_I_L_L_S_ ", font=("times", 10), bg="#cfe0e8", fg="#622569",
                                command=ProcessBills,activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1, )
            btn_InL2BdPro.grid(padx=10, pady=10)

            btn_InL2Bdview = Button(Lfrm_InL2Bd, text="V_I_E_W_ B_I_L_L_S_ ", font=("times", 10), bg="#cfe0e8",fg="#622569",
                                    command= ViewBills,activebackground="#ff6f69", activeforeground="#588c7e",
                                    relief="raised", borderwidth=1, )
            btn_InL2Bdview.grid(padx=10, pady=10)


        def Validate():
            if UserName.get() == '' or passw.get() == '':
                messagebox.showerror('Empty Fields', 'User Id and Password Must Be Filled')
            else:
                conn = sqlite3.connect('ProjoZ_SysTest1')
                conn1 = sqlite3.connect('ProjoZ_SysAdminTest1')
                cur1 = conn1.cursor()
                cur = conn.cursor()
                #cur.execute("SELECT * FROM System_UserTest1")
                cur1.execute("SELECT Admin_Name,Pass_Word FROM System_AdminTest1 WHERE Admin_Name=? AND Pass_word=?",(UserName.get(), passw.get()))
                c = cur1.fetchall()
                #a = cur.fetchall()
                #print(a)
                cur.execute("SELECT * FROM System_UserTest1 WHERE User_Id=? AND Pass_Word=?", (UserName.get(), passw.get()))
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
                    lbl_fail = Label(Lfrm_OutCwat,text='Log In Failed!!',bg="#ffcc5c", fg="#622569",font=("times", 10, "bold"))
                    lbl_fail.grid(row=2,column=0)
                    lbl_fail.after(3000,failOut)
                conn1.commit()
                conn.commit()
                conn1.close()
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

        btn_usLogin = Button(frm_MidC, text="Log In", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"), command=Validate)
        btn_usLogin.grid(row=1, column=0, pady=5)
        btn_exitusLog = Button(frm_MidC, text="E_X_I_T", background="#588c7e", fg="#ff6f69", activebackground="#ff6f69",
                           activeforeground="#588c7e", font=("arial", 15, "bold"), command=ExitLog)
        btn_exitusLog.grid(row=1, column=1, pady=5)
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

housebill = StringVar()
opt_select = OptionMenu(frm_MidL1, housebill, *AptName)
opt_select.grid(row=1, column=0, padx=20,pady=(5,10))
btn_select = Button(Lfrm_OutL1wat,text="Select Apartment", font=("times",10), bg="#cfe0e8", fg="#622569",activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,
                    command=HseLogin)
btn_select.grid(row=2,column=0)
conn.commit()
conn.close()

Lfrm_OutL2wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutL2wat.grid(row=2, column=0,padx=(5,50),pady=50)
frm_MidL2 = Frame(Lfrm_OutL2wat, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidL2.grid(padx=15,pady=15)
Lfrm_InL2 = LabelFrame(frm_MidL2, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InL2.grid()
def backBill():
    Lfrm_OutL1wat.grid_forget()
    Lfrm_OutL2wat.grid_forget()
    Lfrm_OutR1wat.grid_forget()
    Lfrm_OutCwat.grid_forget()


btn_InL2a = Button(Lfrm_InL2,text="_B_A_C_K_HOME_", font=("times",15), bg="#cfe0e8", fg="#622569",
                   command=backBill,activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1,)
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



Lfrm_OutR1wat = LabelFrame(master, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutR1wat.grid(row=1, column=4,padx=(10,20),pady=(20,10))
frm_MidR1 = Frame(Lfrm_OutR1wat, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidR1.grid(padx=8,pady=8)
Lfrm_InR1 = LabelFrame(frm_MidR1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InR1.grid()
tex = datetime.datetime.today()
cal = Calendar(Lfrm_InR1, selectmode="day", year=tex.year, month=tex.month, day=tex.day)
cal.grid(padx=20,pady=20)
y = cal.get_date()
c,v,b = y.split('/')
x = datetime.datetime(int(b),int(c),int(v))
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

mainloop()