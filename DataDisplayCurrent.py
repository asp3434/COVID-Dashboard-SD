# This script takes data from the json files for a certain country and then plots any of the four statistics

#import bokeh libraries
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter, widgets
from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import grid, gridplot, row, layout
from bokeh.events import MenuItemClick, Event
from ScrapeWebsite import scrape_country
from bokeh.models import CustomJS, MultiSelect
from bokeh.io import show
from bokeh.models import CustomJS, TextInput

# date modules
from datetime import datetime, timedelta
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter

from bokeh.io import output_file, show
from bokeh.models.widgets import Select

# other libraries
import datetime
from datetime import date
from datetime import timedelta, datetime
import json
import string

# **Need widget with callback here so the country = user text input
# **And then need to allow multiple plots and selection of each of the four stats
country = "japan"

# initialize stat lists
tot_deaths = []
tot_deaths_1m = []
daily_deaths = []
daily_deaths_1m = []

# initialize json file date range that will be indexed from
start_date = date(2022,11,28)
end_date = date.today()
delta = timedelta(days=1)

# initialize vector of dates for plotting
all_dates = []

# Loop through each date and make arrays for each of the four stats over time
while start_date <= end_date:
    # use this if want to print the dates --> print(start_date.strftime("%Y-%m-%d"))
    with open('country_statistics1_'+str(start_date)+'.json') as f:
        # get country data
        data = json.load(f)
        country_data = data[country]
        # make lists for each of the stats over all of the dates
        tot_deaths.append(country_data[0])
        tot_deaths_1m.append(country_data[1])
        daily_deaths.append(country_data[2])
        daily_deaths_1m.append(country_data[3])
    # convert dates to datetimes so bokeh dateticks on the x axis will work (this is for plotting only)
    dateString = str(start_date)
    dateList = dateString.split('-')
    start_timeDate = datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]))
    # record all of the dates the loop goes through (this is for plotting only) 
    all_dates.append(start_timeDate)
    # increment the day
    start_date += delta
# ADD**: make sure works if skip a day of json file

# create new plot
p = figure(title="daily deaths in " + str(country) + " vs time", 
    x_axis_label='date', y_axis_label='daily deaths', x_axis_type="datetime",
    sizing_mode="stretch_width",max_width=700,height=400,)

# add line
p.line(all_dates, daily_deaths, color="navy", line_width=1)

# format x axis date ticks
p.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")

# # show the results
show(p)

