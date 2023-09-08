import requests
import tkinter as tk
from tkinter import ttk, messagebox


def fetch_prayer_times(city, country):
  url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=5"

  try:
    response = requests.get(url)
    info = response.json()
    if "data" in info:
      timings = info["data"]["timings"]
      return timings
    else:
      return None
  except Exception as e:
    return f"unexpected error occurred {e}"

def gui_fetch_prayer_times():
  city = city_entry.get()
  country = country_entry.get()
  
  if city and country:
    prayer_timings = fetch_prayer_times(city, country)
    for name, time in prayer_timings.items():
       result.insert(tk.END, f"{name}:{time}")
  else:
    messagebox.showerror("Error!","unable to fetch prayer time, please enter correct city and country names")
  


app = tk.Tk()
app.title("Prayer Times")
frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0)

city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column=0, pady=10)
city_entry = ttk.Entry(frame, width=20)
city_entry.grid(row=0, column=1, pady=10)

country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column=0, pady=10)
country_entry = ttk.Entry(frame, width=20)
country_entry.grid(row=1, column=1, pady=10)

fetch_button = ttk.Button(frame, text="Get Time", command=gui_fetch_prayer_times)
fetch_button.grid(row=2, column=0, columnspan=3, pady=15)

result = tk.Listbox(frame, height=15, width=30)
result.grid(row=3, column=0, columnspan=2, pady=5)

app.mainloop()
