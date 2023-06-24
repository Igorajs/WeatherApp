import tkinter as tk

bgc = '#35383d'
win = tk.Tk()
win.title('Weather checker')
win.geometry('740x600')
win.resizable(False, False)
win.configure(bg=bgc)

title = tk.Label(win, text="Weather Checker", bg=bgc, fg='white', font=('Arial', 40, 'bold'))
title.pack(ipadx=20, ipady=20, pady=(0,120))

frameCenter = tk.Frame(win, bg=bgc)
inputLabel = tk.Label(frameCenter, text="Search for City", bg=bgc, fg='white', font=('Arial',13))
inputLabel.pack()
entry = tk.Entry(frameCenter, width=30, font=('Arial 15'))
sbtn = tk.Button(frameCenter, text="Search", bg='#05a11f', fg='#daebdd',font=('Arial 10 bold'))
entry.pack(fill="x", side='left', padx=10)
sbtn.pack(fill="x", side='left', ipadx=10)
frameCenter.pack()







win.mainloop()