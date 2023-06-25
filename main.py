import tkinter as tk
import datetime as dt
import requests
from PIL import Image, ImageTk

def checkWeather():
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = '14aa10bc5f9015cce02d398d9195a099'
    CITY = entry.get()
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    if response['cod'] == '404' or entry.get() == "":
        errorvar.set('Such a city does not exist')
        entry.delete(0, tk.END)
        return
    errorvar.set('')
    entry.delete(0, tk.END)
    #Deklaracja zmiennych i przypisywanie nowych wartości

    r = response
    print(r)
    icon = r['weather'][0]['icon']
    temp = int(r['main']['temp']-273.15)
    tempMin = int(r['main']['temp_min']-273.15)
    tempMax = int(r['main']['temp_max']-273.15)
    pressure = r['main']['pressure']
    humidity = r['main']['humidity']
    wind = r['wind']['speed']
    clouds = r['clouds']['all']
    image_path = f'icons/{icon}@2x.png'
    img_resize = Image.open(image_path).resize((70, 70))
    img = ImageTk.PhotoImage(img_resize)
    typ2 = tk.Label(frameInfo, bg=bgc, fg='white', image=img)
    typ2.image = img
    typ2.grid(column=0, row=2, padx=10)
    tvar.set(f'{temp}°C')
    hvar.set(f'{humidity}%')
    pvar.set(f'{pressure} hPa')
    wvar.set(f'{wind} m/s')
    cvar.set(f'{clouds} %')
    mmvar.set(f'{tempMin}°C / {tempMax}°C')
    cityvar.set(f'{r["name"]}')


#bgc = '#35383d'
bgc = '#6140ad'
win = tk.Tk()
win.title('Weather checker')
win.geometry('800x600')
win.resizable(False, False)
win.configure(bg=bgc)

# Zmienne
cityvar = tk.StringVar()
tvar = tk.StringVar()
wvar = tk.StringVar()
hvar = tk.StringVar()
pvar = tk.StringVar()
mmvar = tk.StringVar()
cvar = tk.StringVar()
errorvar = tk.StringVar()
countryVal = tk.StringVar()
timeVal = tk.StringVar()
sunriseVal = tk.StringVar()
sunsetVal = tk.StringVar()

cityvar.set("*City name*")
tvar.set('...')
wvar.set('...')
hvar.set('...')
pvar.set('...')
mmvar.set('...')
cvar.set('...')
countryVal.set('...')
timeVal.set('...')
sunriseVal.set('...')
sunsetVal.set('...')

# Tytuł
title = tk.Label(win, text="Weather Checker", bg=bgc, fg='white', font=('Arial', 40, 'bold'))
title.pack(ipadx=20, ipady=20, pady=(0,120))

# Centralny Frame
frameCenter = tk.Frame(win, bg=bgc)
inputLabel = tk.Label(frameCenter, text="Search for City:", bg=bgc, fg='white', font=('Arial',13))
inputLabel.pack()
entry = tk.Entry(frameCenter, width=30, font=('Arial 15'))
sbtn = tk.Button(frameCenter, text="Search", bg='#05a11f', fg='#daebdd', font=('Arial 10 bold'), command=checkWeather)
entry.pack(fill="x", side='left', padx=10)
sbtn.pack(fill="x", side='left', ipadx=10)
frameCenter.pack()
errorLabel = tk.Label(win, bg=bgc, fg='red', font=('Arial', 13), textvariable=errorvar)
errorLabel.pack(ipadx=10)

# Informacje o pogodzie
ifg = '#f73434'

cityName = tk.Label(win, bg=bgc, fg='#e3b719', font=('Arial 22 bold'), textvariable=cityvar)
cityName.pack()

frameDesc = tk.Frame(win, bg=bgc)
country = tk.Label(frameDesc, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Country󠁥󠁳󠁰󠁶󠁿:")
time = tk.Label(frameDesc, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Time:")
sunrise = tk.Label(frameDesc, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Sunrise:")
sunset = tk.Label(frameDesc, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Sunset:")
country.grid(column=0, row=0, sticky="W")
time.grid(column=0, row=1, sticky="W")
sunrise.grid(column=0, row=2, sticky="W")
sunset.grid(column=0, row=3, sticky="W")

countryV = tk.Label(frameDesc, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=countryVal)
timeV = tk.Label(frameDesc, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=timeVal)
sunriseV = tk.Label(frameDesc, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=sunriseVal)
sunsetV = tk.Label(frameDesc, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=sunsetVal)
countryV.grid(column=1, row=0)
timeV.grid(column=1, row=1)
sunriseV.grid(column=1, row=2)
sunsetV.grid(column=1, row=3)

frameDesc.pack()

frameInfo = tk.Frame(win, bg=bgc)
typ1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Type")
typ1.grid(column=0, row=0, padx=10)
t1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Temperature")
t1.grid(column=1, row=0, padx=10)
w1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Wind")
w1.grid(column=2, row=0, padx=10)
h1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Humidity")
h1.grid(column=3, row=0, padx=10)
p1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Pressure")
p1.grid(column=4, row=0, padx=10)
mm1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Min/Max Temp.")
mm1.grid(column=5, row=0, padx=10)
c1 = tk.Label(frameInfo, bg=bgc, fg=ifg, font=('Arial 13 bold'), text="Cloudiness")
c1.grid(column=6, row=0, padx=10)


t2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=tvar)
t2.grid(column=1, row=1, padx=10)
w2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=wvar)
w2.grid(column=2, row=1, padx=10)
h2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=hvar)
h2.grid(column=3, row=1, padx=10)
p2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=pvar)
p2.grid(column=4, row=1, padx=10)
mm2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=mmvar)
mm2.grid(column=5, row=1, padx=10)
c2 = tk.Label(frameInfo, bg=bgc, fg='white', font=('Arial 13 bold'), textvariable=cvar)
c2.grid(column=6, row=1, padx=10)
frameInfo.pack(pady=(40, 0))

win.mainloop()