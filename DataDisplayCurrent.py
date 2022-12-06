
# This script takes data from the json files for a certain country and then plots any of the four statistics

# NEED:
# 1. Allow user to pick country and pick a stat for the country --> then plot stat over time (working in script, need UI for bokeh)
# 2. Allow user to compare multiple plots for country stats over time on the same graph  (need in script and bokeh)

# Pseudocode for adding multiple plots (just in script, no widgets):
# Initialize the figure
# for country in countries:
#       execute the main part of the script
#       and add the stat to the plot

#import modules
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter, widgets, Select
from bokeh.plotting import figure, show, curdoc
from bokeh.layouts import grid, gridplot, row, layout
from bokeh.events import MenuItemClick, Event
from ScrapeWebsite import scrape_country
from bokeh.models import CustomJS, MultiSelect
from bokeh.io import show
from bokeh.models import CustomJS, TextInput
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.io import output_file, show
from bokeh.models.widgets import Select
from bokeh.colors import RGB
import json
import numpy 
import random
import string

# Date modules
import datetime
from datetime import date
from datetime import timedelta, datetime
from datetime import datetime, timedelta

colors = ['blue', 'green', 'red']
# create new plot
p = figure(title="daily deaths in vs time", 
    x_axis_label='date', y_axis_label='daily deaths', x_axis_type="datetime",
    sizing_mode="stretch_width",max_width=700,height=400,)

countries = ["usa", "brazil", "japan", "china", "spain", "germany"]

# for color indexing
i = 0

for country in countries:
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
    country_data = []
    # number of json files that are not available (were skipped)
    times_skipped = 1
    # Loop through each date and make arrays for each of the four stats over time
    while start_date <= end_date:
        # use this if want to print the dates --> print(start_date.strftime("%Y-%m-%d"))
        try:
            with open('country_statistics1_'+str(start_date)+'.json') as f:
                # get country data
                data = json.load(f)
                country_data = data[country]
        # If there is no json file (because script wasn't ran on that date) then do not update country date
        # The last recorded values will be used instead
        except FileNotFoundError:
                times_skipped += 1
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

        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        red = 255*x1
        green = 255*x2
        blue = 255*x3
        color_rand = RGB(r = red,
            g = green,
            b = blue)
        # add line
        p.line(all_dates, daily_deaths, legend_label=country,color=color_rand, line_width=1)

        # format x axis date ticks
        p.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    i += 1
        


# outside loop
# # show the results
show(p)
