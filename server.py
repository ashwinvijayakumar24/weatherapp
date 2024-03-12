import random
import re
import weather
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_or_zip = request.form['city_or_zip']
        weather_response = input_validation(city_or_zip)
        return render_template('index.html', city_or_zip=city_or_zip, weather_response=weather_response)
    
    return render_template('index.html')

def input_validation(city_or_zip):
    input_field = city_or_zip
    if(re.match(("^[a-zA-Z]+$"),input_field)):
        coordinates = weather.city_to_coordinates(city_or_zip)
        return (weather.get_weather_data(coordinates))
    if(re.match(("^\\d{5}+$"),input_field)):
        coordinates = weather.zipcode_to_coordinates(city_or_zip)
        return (weather.get_weather_data(coordinates))
    else:
        return ["Please type in a valid location or zipcode"]

if __name__ == '__main__':
    app.run(debug=True)