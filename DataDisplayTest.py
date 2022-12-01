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
from datetime import timedelta, datetime
import json

# inialize country temp --> change to user input
country = 'france' 

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
    # record all of the dates the loop goes through for plotting
    all_dates.append(start_date)
    # increment the day
    start_date += delta
# ADD**: make sure works if skip a day of json file

# Temporary x axis  
x = [1, 2, 3, 4]

# create a new plot with a title and axis labels
p = figure(title= "daily deaths for " + str(country), x_axis_label="dates", y_axis_label="# of deaths")

# Plot all stats: Easier to plot one at a time because the numbers are so different
p.line(x, daily_deaths, legend_label="Objects", color="green", line_width=2)
#p.line(x, tot_deaths, legend_label="Temp.", color="blue", line_width=2)
#p.line(x, tot_deaths_1m, legend_label="Rate", color="red", line_width=2)
#p.line(x, daily_deaths_1m, legend_label="Objects", color="green", line_width=2)

# show the results
show(p)

