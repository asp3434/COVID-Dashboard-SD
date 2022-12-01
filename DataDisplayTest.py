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
from datetime import timedelta
import json

# initialize stat lists
country = 'usa' #temp --> change to user input
tot_deaths = []
tot_deaths_1m = []
daily_deaths = []
daily_deaths_1m = []

# initialize json file date range that will be indexed from
start_date = date(2022,11,28)
end_date = date.today()
delta = timedelta(days=1)

# start vector of dates for plotting
all_dates = []

# Loop through each date and make arrays that are each of the four stats over time
while start_date <= end_date:
    # use this if want to print the dates --> print(start_date.strftime("%Y-%m-%d"))
    with open('country_statistics1_'+str(start_date)+'.json') as f:
        data = json.load(f)
        country_data = data[country]
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
p = figure(title="Covid Stats Test Plot", x_axis_label="x", y_axis_label="y")

# Plot all stats
#p.line(x, tot_deaths, legend_label="Temp.", color="blue", line_width=2)
#p.line(x, tot_deaths_1m, legend_label="Rate", color="red", line_width=2)
p.line(x, daily_deaths, legend_label="Objects", color="green", line_width=2)
#p.line(x, daily_deaths_1m, legend_label="Objects", color="green", line_width=2)

# show the results
show(p)

# This is date ticker code that has not been implemented yet:
# # plot a stat vs date on the x axis using the date tickers using bokeh
# # create new plot
# p = figure(title="datetime axis example",x_axis_type="datetime")
# # add renderers
# p.line(all_dates, tot_deaths, color="navy", line_width=1)
# # format axes ticks
# p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")
# # show the results
# show(p)
