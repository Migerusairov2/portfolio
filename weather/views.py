from django.shortcuts import render
from .models import SearchHistory
import requests

API_KEY = '9ae0beea2a0a67c0e79cda498614a858'

def weather(request):
    weather = None
    error = None

    if request.method == "POST":
        city = request.POST.get('city', '').strip()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                resp = requests.get(url, timeout=5)
                data = resp.json()

                if resp.status_code == 200:
                    weather = {
                        'city': f"{data['name']}, {data['sys']['country']}",
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'description': data['weather'][0]['description'].title(),  # <-- fixed here
                        'icon': data['weather'][0]['icon'],
                    }            
                else:
                    error = data.get("message", "Could not fetch weather data.")
            except requests.RequestException:
                error = "Network error. Please try again."
        else:
            error = "Please enter a city name."

    return render(request, "index.html", {
        'weather': weather,
        'error': error,
    })
