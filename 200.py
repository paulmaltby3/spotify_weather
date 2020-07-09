from flask import Flask, escape, request, render_template
import pandas
import numpy as np

#added static file to enable images
#worked it out by putting /static/ as a seperate folder under 200_Songs rather than under templates, via https://code-maven.com/flask-serve-static-files

app = Flask(__name__, static_url_path='/static')

#Get the weather API stuff
from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'

darksky = DarkSky(API_KEY)

latitude = 52.475769
longitude = -0.921517
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    # timezone='UTC' # default None - will be set by DarkSky API automatically
)
# This prints it out on the command line, it makes it easier to see whether it doesnt work
print(forecast.currently.summary)

forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be found at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be found at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be found at darksky/forecast.py
forecast.daily # DailyForecast. Can be found at darksky/forecast.py
forecast.alerts # [Alert]. Can be found at darksky/forecast.py

#This is the python logic to get the right info to show depending on the weather
if weather == 'Clear':
    filename = 'static/top10.csv' 

elif weather == 'Rain':
    filename = 'static/bottom10.csv'

else:
    filename = 'static/middle10.csv'

#Below is defining the web pages we're creating
#Changed this below to do get/post 
#added in new content to do tables https://stackoverflow.com/questions/54854498/reading-a-csv-file-in-flask-and-iterating-through-jinga2
@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Homepage"
    weather = forecast.currently.summary
    #filename = 'static/top10.csv'
    data = pandas.read_csv(filename, header=0)
    table = list(data.values)
    #changed index to indextest while I was playing around to get things to work. Remember to change back
    return render_template("indextest.html", table=table, title=title, weather=weather)

@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)