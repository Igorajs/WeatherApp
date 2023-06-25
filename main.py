import tkinter as tk
import datetime as dt


bgc = '#35383d'
win = tk.Tk()
win.title('Weather checker')
win.geometry('740x600')
win.resizable(False, False)
win.configure(bg=bgc)

title = tk.Label(win, text="Weather Checker", bg=bgc, fg='white', font=('Arial', 40, 'bold'))
title.pack(ipadx=20, ipady=20, pady=(0,120))

frameCenter = tk.Frame(win, bg=bgc)
inputLabel = tk.Label(frameCenter, text="Search for City:", bg=bgc, fg='white', font=('Arial',13))
inputLabel.pack()
entry = tk.Entry(frameCenter, width=30, font=('Arial 15'))
sbtn = tk.Button(frameCenter, text="Search", bg='#05a11f', fg='#daebdd',font=('Arial 10 bold'))
entry.pack(fill="x", side='left', padx=10)
sbtn.pack(fill="x", side='left', ipadx=10)
frameCenter.pack()

frameInfo = tk.Frame(win, bg=bgc)
cityName = tk.Label(frameInfo, bg=bgc, font=('Arial 15'), text="*City name*")
cityName.grid(column=0,row=0,columnspan=6)
t1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Temperatura")
t1.grid(column=0,row=1)
w1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Wiatr")
w1.grid(column=1,row=1)
a1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Wiatr")
a1.grid(column=2,row=1)
e1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Wiatr")
e1.grid(column=3,row=1)
y1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Wiatr")
y1.grid(column=4,row=1)
u1 = tk.Label(frameInfo, bg=bgc, font=('Arial 13'), text="Wiatr")
u1.grid(column=5,row=1)
frameInfo.pack()







win.mainloop()