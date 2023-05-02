from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import re

Wapp = Tk()
Wapp.title('Water Usage App')
Wapp.geometry('800x640')

Lfrm_OutC1 = LabelFrame(Wapp, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutC1.grid(row=1, column=0,padx=(10,20),pady=(20,10))
frm_MidC1 = Frame(Lfrm_OutC1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidC1.grid(padx=8,pady=8)
Lfrm_InC1 = LabelFrame(frm_MidC1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC1.grid()

Lfrm_OutC1R = LabelFrame(Wapp, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutC1R.grid(row=2, column=0,padx=(10,20),pady=(20,10))
frm_MidC1R = Frame(Lfrm_OutC1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidC1R.grid(padx=8,pady=8)
Lfrm_InC1R = LabelFrame(frm_MidC1, bg="#cfe0e8", padx=15, pady=15)
Lfrm_InC1R.grid()

Lfrm_OutC2R = LabelFrame(Wapp, relief="raised", borderwidth=3, bg="#ffcc5c",padx=10,pady=10)
Lfrm_OutC2R.grid(row=1, column=1, rowspan=2,padx=(10,20),pady=(20,10))
frm_MidC2R = Frame(Lfrm_OutC1, relief="raised", borderwidth=3, bg="#622569",padx=3,pady=3)
frm_MidC2R.grid(padx=8,pady=8)
Lfrm_InC2R = LabelFrame(frm_MidC1, bg="#cfe0e8", padx=15, pady=20)
Lfrm_InC2R.grid()

def waterUse():
    conn = sqlite3.connect('ProjoZ_SysAdminTest1')
    cur = conn.cursor()
    cur.execute("SELECT House_No FROM Water_Bills WHERE Apart_Name=?",('Kings Palace',))
    j = cur.fetchall()
    #print(j)
    cur.execute("SELECT Units FROM Water_Bills WHERE Apart_Name=?",('Kings Palace',))
    k = cur.fetchall()
    #print(k)
    hseNum = []
    unitNum = []
    for num in k:
        print(num)
        uNum = num[0]
        unitNum.append(uNum)
    for rec in j:
        '''print(rec[0][4])
        print(rec[0][5])
        print(rec[0][6])
        print(rec[0][7])
        print(rec[0][8])'''
        jfinds = re.findall("[a-zA-Z0-9]", rec[0])
        print(jfinds)
        word = ''
        for c in jfinds:
             word += str(c)
        print(word)
        hseNum.append(word)
    
    xpoints = np.array(hseNum)
    ypoints = np.array(unitNum)

    plt.bar(xpoints,ypoints)
    plt.show()
    conn.commit
    conn.close()

btn_use = Button(Lfrm_InC1R,text="  B_i_l_l_Man_age_r_", font=("times",15), bg="#cfe0e8", fg="#622569",
                 command=waterUse,activebackground="#ff6f69", activeforeground="#588c7e", relief="raised", borderwidth=1)
btn_use.grid(padx=10, pady=10)

Wapp.mainloop()