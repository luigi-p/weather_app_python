# importing libraries

from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
# app title
root.title("Weather App")

# display dimension
root.geometry("900x500+300+200")

# disable resizable 
root.resizable(False, False)


def getWeather():

    try:

        # get the city name in input
        city = text_field.get()

        # find and display the time zone of the given location
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        # get the current time of the given location
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # get weather condition with API + json
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=07cbc381c4f34acb2298aeb95c1244fa"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] -273.15)
        pressure = json_data["main"]['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # temperature
        t.config(text=(temp, "°"))

        # condition
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid entry, please retry.")


# search box - upload and place the image
Search_image = PhotoImage(file = "icons/search.png")
my_image = Label(image = Search_image)
my_image.place(x = 20, y = 20)

# text field characteristics
text_field = tk.Entry(root, justify= "center", width= 17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
text_field.place(x = 70, y = 40)
text_field.focus()

# search icon - upload and place the image
Search_icon = PhotoImage(file = "icons/search_icon.png")
my_image_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
my_image_icon.place(x = 400, y = 34)

# logo - upload and place the image
Logo_image = PhotoImage(file="icons/logo.png")
logo = Label(image=Logo_image)
logo.place(x = 150, y = 100)

# bottom box - upload and place image
Frame_image=PhotoImage(file="icons/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx = 5, pady = 5, side = BOTTOM)

# display current time
name = Label(root, font=("Arial", 15, "bold"))
name .place(x = 30, y = 100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x = 30, y = 130)

# label WIND - declaration and position
label_1 = Label(root, text = "WIND", font = ("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_1.place(x = 120, y = 400)

# label HUMIDITY - declaration and position
label_2 = Label(root, text = "HUMIDITY", font = ("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_2.place(x = 250, y = 400)

# label DESCRIPTION - declaration and position
label_3 = Label(root, text = "DESCRIPTION", font = ("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_3.place(x = 430, y = 400)

# label PRESSURE - declaration and position
label_4 = Label(root, text = "PRESSURE", font = ("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_4.place(x = 650, y = 400)

t = Label(font=("Arial", 70, "bold"), fg="#ee666d")
t.place(x = 400, y = 150)
c = Label(font=("Arial", 15, "bold"))
c.place(x = 400, y = 250)

# 3 dots displayed under each label
# wind
w = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
w.place(x = 120, y = 430)

# humidity
h = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
h.place(x = 280, y = 430)

#description
d = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
d.place(x = 450, y = 430)

# pressure
p = Label(text="...", font=("Arial", 20, "bold"), bg="#1ab5ef")
p.place(x = 670, y = 430)


# run app
root.mainloop()