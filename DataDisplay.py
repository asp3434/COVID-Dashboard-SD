# Testing bokeh features. We can combine a script like this with ScrapeWebsite to visualize the data

from datetime import datetime, timedelta
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show, curdoc
import json


# generate list of dates (today's date in subsequent weeks)
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 3)]

# arrays to take the place of deaths for a certain country  --> the user can input a country and then the    
USA_deaths = [20000, 21000, 21500]
Brazil_deaths = [10000, 19000, 20000]
Italy_deaths = [21000, 21100, 21500]

f = open('country_statistics1_2022-11-28.json')
data = json.load(f)
print(data)

# create a new plot with a title and axis labels
p = figure(title="# Deaths vs Days",
x_axis_type="datetime",
x_axis_label="Days", 
y_axis_label="Deaths")

# add multiple renderers
p.line(dates, USA_deaths, legend_label="USA", color="blue", line_width=2)
p.line(dates, Brazil_deaths, legend_label="Brazil", color="red", line_width=2)
p.line(dates, Italy_deaths, legend_label="Italy", color="green", line_width=2)

# add date ticks to x axis
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# show the results
show(p)

f.close