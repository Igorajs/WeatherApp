import tkinter as tk
import datetime as dt
import requests


bgc = '#35383d'
win = tk.Tk()
win.title('Weather checker')
win.geometry('740x600')
win.resizable(False, False)
win.configure(bg=bgc)

# Zmienne
cityvar = tk.StringVar()
typeIMG = tk.PhotoImage('')
tvar = tk.StringVar()
wvar = tk.StringVar()
hvar = tk.StringVar()
pvar = tk.StringVar()
mmvar = tk.StringVar()
cvar = tk.StringVar()

cityvar.set("*City name*")
tvar.set('...')
wvar.set('...')
hvar.set('...')
pvar.set('...')
mmvar.set('...')
cvar.set('...')

# Tytuł
title = tk.Label(win, text="Weather Checker", bg=bgc, fg='white', font=('Arial', 40, 'bold'))
title.pack(ipadx=20, ipady=20, pady=(0,120))

# Centralny Frame
frameCenter = tk.Frame(win, bg=bgc)
inputLabel = tk.Label(frameCenter, text="Search for City:", bg=bgc, fg='white', font=('Arial',13))
inputLabel.pack()
entry = tk.Entry(frameCenter, width=30, font=('Arial 15'))
sbtn = tk.Button(frameCenter, text="Search", bg='#05a11f', fg='#daebdd',font=('Arial 10 bold'))
entry.pack(fill="x", side='left', padx=10)
sbtn.pack(fill="x", side='left', ipadx=10)
frameCenter.pack()

# Informacje o pogodzie
frameInfo = tk.Frame(win, bg=bgc)
cityName = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 17 bold'), textvariable=cityvar)
cityName.grid(column=0, row=0, columnspan=7, padx=10, pady=10)
typ1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Type")
typ1.grid(column=0, row=1, padx=10, pady=10)
t1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Temperature")
t1.grid(column=1, row=1, padx=10, pady=10)
w1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Wind")
w1.grid(column=2, row=1, padx=10, pady=10)
h1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Humidity")
h1.grid(column=3, row=1, padx=10, pady=10)
p1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Pressure")
p1.grid(column=4, row=1, padx=10, pady=10)
mm1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Min/Max Temp.")
mm1.grid(column=5, row=1, padx=10, pady=10)
c1 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), text="Cloudiness")
c1.grid(column=6, row=1, padx=10, pady=10)


typ2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), image=typeIMG)
typ2.grid(column=0, row=2, padx=10, pady=10)
t2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=tvar)
t2.grid(column=1, row=2, padx=10, pady=10)
w2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=wvar)
w2.grid(column=2, row=2, padx=10, pady=10)
h2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=hvar)
h2.grid(column=3, row=2, padx=10, pady=10)
p2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=pvar)
p2.grid(column=4, row=2, padx=10, pady=10)
mm2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=mmvar)
mm2.grid(column=5, row=2, padx=10, pady=10)
c2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=cvar)
c2.grid(column=6, row=2, padx=10, pady=10)
frameInfo.pack(pady=(80, 0))

win.mainloop()