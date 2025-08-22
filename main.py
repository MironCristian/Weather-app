import tkinter as tk
import requests
from PIL import Image, ImageTk
import io


def translate_weather_code(code):
    if code in [0, 1]: return "Cer senin"
    elif code == 2: return "Parțial înnorat"
    elif code == 3: return "Complet înnorat"
    elif code in [45, 48]: return "Ceață"
    elif code in [61, 63, 65]: return "Ploaie"
    elif code in [71, 73, 75]: return "Ninsoare"
    elif code in [80, 81, 82]: return "Aversă de ploaie"
    elif code in [95, 96, 99]: return "Furtună"
    else: return "Condiții necunoscute"

def weather_code_to_icon_code(code):
    if code in [0,1]: return "01d"
    elif code == 2: return "02d"
    elif code == 3: return "03d"
    elif code in [45, 48]: return "50d"
    elif code in [51, 53, 55, 61, 63, 65, 80, 81, 82]: return "10d"
    elif code in [71, 73, 75]: return "13d"
    elif code in [95, 96, 99]: return "11d"
    else: return "01d"

def get_weather():
    city_name = entry_oras.get()
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    response = requests.get(geocoding_url)

    if response.status_code == 200:
        data = response.json()
        
        if 'results' in data:
            location = data['results'][0]
            latitude = location['latitude']
            longitude = location['longitude']
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code"
            weather_response = requests.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            current_data = weather_data['current']
            temperatura = current_data['temperature_2m']
            weather_code = current_data['weather_code']
            descriere_vreme = translate_weather_code(weather_code)
            info_vreme = f"Temperatura in {city_name}: {temperatura}°C \n{descriere_vreme}"
            
            icon_code = weather_code_to_icon_code(weather_code)
            icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
            image_response = requests.get(icon_url)
            image_response.raise_for_status()
            
            image_data = io.BytesIO(image_response.content)
            img = Image.open(image_data)
            photo = ImageTk.PhotoImage(img)
            
            label_icon.config(image=photo)
            label_icon.image = photo
            label_rezultat.config(text=info_vreme)
            


        else:
            label_rezultat.config(text=f"Nu am putut gasi orasul '{city_name}'.")
    else: 
        
        label_rezultat.config(text="Eroare la retea.")

window = tk.Tk()
window.title("Weather-app")
window.geometry("400x400")
label_oras = tk.Label(
    master=window, 
    text = "introdu numele orasului:",
    font=("Helvetica", 14)
)
label_oras.pack(pady=10)

entry_oras = tk.Entry(
    master=window, 
    width=30,
    font=("Helvetica", 12)
)
entry_oras.pack(pady=5)
button_cauta = tk.Button(
    master=window, 
    text="Cauta Vremea",
    font=("Helvetica", 12, "bold"),
    command= get_weather
)
button_cauta.pack(pady=10)

label_icon = tk.Label(
master=window
)
label_icon.pack()  
label_icon.config(bg="gray")

label_rezultat = tk.Label(
    master=window, 
    text="",
    font=("Helvetica", 14)
)
label_rezultat.pack(pady=5)

  






window.mainloop()
