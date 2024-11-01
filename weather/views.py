import requests
from django.shortcuts import render
from .forms import WeatherForm

def get_weather(request):
    weather_data = None
    form = WeatherForm()
    
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'your_api_key_here'  # Replace with your actual API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'City not found'}

    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})
