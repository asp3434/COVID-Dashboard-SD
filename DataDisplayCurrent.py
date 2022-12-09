# This script lets user choose the contries and statistic desired and then plots the data

# NEED:
# 1. In UI - Allow user to pick country and pick a stat for the country --> then plot stat over time 
# 2. In UI - Allow user to compare multiple plots for country stats over time on the same graph  

# import bokeh modules
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.models import DatetimeTickFormatter
from bokeh.colors import RGB

# import other modules
import json
import random
import datetime
from datetime import timedelta, datetime, date

# user input: countries and stat
countries = ['usa', 'brazil', 'japan', 'russia', 'australia', 'france']
stats_choices = ['total deaths', '(total deaths)/1m', 'daily deaths', '(daily deaths)/1m']
stat_choice = stats_choices[1]

# create new plot
p = figure(title=stat_choice + " vs time", 
    x_axis_label='date mm/yy', y_axis_label=stat_choice, x_axis_type="datetime",
    sizing_mode="stretch_width",max_width=700,height=400,)

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

        # generate a random color for each country being plotted
        x1 = random.random()
        x2 = random.random()
        x3 = random.random()
        red = 255*x1
        green = 255*x2
        blue = 255*x3
        color_rand = RGB(r = red,
            g = green,
            b = blue)
        
        # dictionary to convert user input into the array containing the data for the user selected statistic
        stats_dict = {'total deaths' : tot_deaths, '(total deaths)/1m' : tot_deaths_1m, 
        'daily deaths' : daily_deaths, '(daily deaths)/1m' : daily_deaths_1m}

        # add line
        p.line(all_dates, stats_dict[stat_choice], legend_label=country,color=color_rand, line_width=1)

        # format x axis date ticks
        p.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")

p.legend.click_policy="hide"

#p.add_layout(mytext)

# show the results in a new tab
show(p)
