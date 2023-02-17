from django.shortcuts import render
import json
import urllib.request
import re

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'] # This line gets the value of the city parameter from the POST data.
        city = city.capitalize() # Convert the first letter of the city to uppercase
        if re.search('[^a-zA-Z]', city):
            return render(request, 'index.html', {'message': 'Please use English letters only'}) # Gives message if non-english letter was given as input for a city
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a650b0b2d0b34f9f427c884856e0603c').read() 
        #This line uses the urlopen function from the urllib module to make a GET request to the OpenWeatherMap API. 
        # The URL is constructed by concatenating the city parameter, the API endpoint, and the API key.
        json_data = json.loads(res) # Current weather data stored for specific city in variable
        data = {
            "country_code": str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ', ' + str(json_data['coord']['lat']),
            'temp': round(json_data['main']['temp'] -273.15),
            'pressure': str(json_data['main']['pressure'])+"hPa",
            'humidity': str(json_data['main']['humidity']) +"%",
    }
    else:  #This line starts the else block that will be executed if the request is not a POST request.
        city =''
        data = {}   
    return render (request, 'index.html',{'city':city, 'data' : data}) # This line uses the render function to render the index.html template and return an HTTP response. 
