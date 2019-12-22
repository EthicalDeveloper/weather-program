"""
Ask user what city to get 3 day forecast for then get it 

https://home.openweathermap.org

original url: api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml

Miles_key = 11e2a40b075d1f4c0e3d89980b4a61a3

"""
from datetime import datetime
import requests #library to get data from web
from pprint import pprint as pp


#https://home.openweathermap.org/api_keys
appid = '11e2a40b075d1f4c0e3d89980b4a61a3' #it is a key provided in the url website


def open_lat_lon(city_lat, city_lon):
    import webbrowser
    url = f'http://google.com/maps/@{city_lat},{city_lon},15z'
    webbrowser.open_new_tab(url)




city = input('Please enter a city name followed by country (Dallas, US): ')
city = city.replace(' ','') # this will remove the space between words in input 
request_text = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&mode=json&APPID={appid}' #url where we get that data from. We formatted the url so the user defines what he is gonna look for in the web
forecast_request = requests.get(request_text) # get the data from that URL above
req_json = forecast_request.json()


# working through dictionaries
city_name = req_json['city']['name']
city_id = req_json['city']['id']
city_country = req_json['city']['country']
city_lat = req_json['city']['coord']['lat']
city_lon = req_json['city']['coord']['lon']


print(f'{city_name}, {city_country} id: {city_id} lat: {city_lat} lon: {city_lon}')

open_lat_lon(city_lat,city_lon)

for day in req_json['list']:
    
    for condition in day['weather']:
       
        celcius_convert = (day['main']['temp'] - 32) / 1.8
        day_of_week = datetime.fromtimestamp(int(day['dt'])).strftime('%A') # printing the day
        #pp("Date: " + day['dt_txt'] + ' ' + day_of_week + " |Cloudiness: " + condition['description'] + " |Weather: " + str(celcius_convert))
        print ("Date: {} | Day: {}      | Clouds: {}      | Weather: {} Celsius".format(day['dt_txt'],day_of_week,condition['description'],str(round(celcius_convert,2))))




