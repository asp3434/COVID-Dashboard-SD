# Testing bokeh features. We can combine a script like this with ScrapeWebsite to visualize the data

#import bokeh libraries
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter, widgets
from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import grid, gridplot, row, layout
from bokeh.events import MenuItemClick, Event
from ScrapeWebsite import scrape_country

# date modules
from datetime import datetime, timedelta
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show

# other libraries
import datetime
from datetime import date
import json

# initialize stat lists
country = 'usa' #temp
tot_deaths = []
tot_deaths_1m = []
daily_deaths = []
daily_deaths_1m = []
x_axis_dates = [datetime.date(2022,11,30)]
country_data = []
data = []
# ** need to index all of the json files up to today --> change this
past_date = datetime.date(2022,11,28)
current_date = date.today()
print(current_date)

# loop through all of the json files for dates up to current date using time delta
# add timedelta day up to current date starting at 11-28

with open('country_statistics1_'+str(past_date)+'.json') as f:
    data = json.load(f)
    country_data= data[country]
    tot_deaths = country_data[0]
    tot_deaths_1m = country_data[1]
    daily_deaths = country_data[2]
    daily_deaths_1m = country_data[3]

print(country_data)

# then plot a stat vs date on the x axis using the date tickers using bokeh