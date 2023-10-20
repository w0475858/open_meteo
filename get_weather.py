
import requests

city = "Halifax, Nova Scotia"

searched_results = f"https://geocode.maps.co/search?q={city}"

geocode_info = requests.get(searched_results)

json_resonse = geocode_info.json()


lat = json_resonse["lat"]
lon = json_resonse["lon"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

weather_data = requests.get(weather_url)

print(weather_data)