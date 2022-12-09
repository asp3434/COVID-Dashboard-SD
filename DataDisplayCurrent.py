# This script displays country COVID statistics and allows the user to deselect specific country statistics

# import bokeh modules
from bokeh.models import DatetimeTickFormatter
from bokeh.plotting import figure, show
from bokeh.io import show
from bokeh.models import (ColumnDataSource, DataTable, IntEditor, SelectEditor,
                          StringFormatter, TableColumn)
from bokeh.colors import RGB
from bokeh.layouts import column, gridplot

# import other modules
import json
import random
import datetime
from datetime import timedelta, datetime, date

# code to let the user know that the script is running. It takes a while to generate the plots
print("Code is running...")

# loads one .json file to grab all countries
f = open('country_statistics1_2022-11-28.json')
data1 = json.load(f)

# creates a list of countries
countries = list(data1.keys())

# create new plots
p1 = figure(title= "Total Deaths" + " vs Time", 
    x_axis_label='Date mm/yy', y_axis_label="Total Deaths", x_axis_type="datetime"
    ,width=1400,height=5500,)
p2 = figure(title="Total Deaths per Million" + " vs Time", 
    x_axis_label='Date mm/yy', y_axis_label="Total Deaths per Million", x_axis_type="datetime"
    ,width=1400,height=5500,)
p3 = figure(title="Daily Deaths" + " vs Time", 
    x_axis_label='Date mm/yy', y_axis_label="Daily Deaths", x_axis_type="datetime"
    ,width=1400,height=5500,)
p4 = figure(title="Daily Deaths per Million" + " vs Time", 
    x_axis_label='Date mm/yy', y_axis_label="Daily Deaths per Million", x_axis_type="datetime"
    ,width=1400,height=5500,)

# data frame arrays for the dictionary/table later on
df_total_deaths = []
df_total_deaths_1m = []
df_daily_deaths = []
df_daily_deaths_1m = []

# loop through the countries
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

    # Loop through each date (.json file) and make arrays for each of the four stats over time
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
        tot_deaths_1m.append(country_data[2])
        daily_deaths.append(country_data[1])
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
    red = 255.0 *x1
    green = 255.0*x2
    blue = 255.0*x3
    color_rand = RGB(r = red,
        g = green,
        b = blue)
    
    # updating arrays for table outside the for loop
    df_total_deaths.append(tot_deaths)
    df_total_deaths_1m.append(tot_deaths_1m)
    df_daily_deaths.append(daily_deaths)
    df_daily_deaths_1m.append(daily_deaths_1m)
    
    # add lines of each country
    p1.line(all_dates, tot_deaths, line_color=color_rand, legend_label = country, visible= False)
    p2.line(all_dates, tot_deaths_1m, line_color=color_rand, legend_label = country, visible=False)
    p3.line(all_dates, daily_deaths, line_color=color_rand, legend_label = country, visible=False)
    p4.line(all_dates, daily_deaths_1m, line_color=color_rand, legend_label = country, visible=False)
    
    # format x axis date ticks
    p1.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    p2.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    p3.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    p4.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    
    
# create dictionary for the table
df_dict = {"country": countries,
           "total_deaths": df_total_deaths,
           "new_deaths_daily": df_daily_deaths,
           "deaths_per_mil" : df_total_deaths_1m,
           "deaths_per_mil_daily" : df_daily_deaths_1m
    }

# Create table
source = ColumnDataSource(df_dict)
columns = [
    TableColumn(field="country", title="Country",
                editor=SelectEditor(options=countries),
                formatter=StringFormatter(font_style="bold")),
    TableColumn(field="total_deaths", title="Total Deaths", editor=IntEditor()),
    TableColumn(field="new_deaths_daily", title="Daily New Deaths", editor=IntEditor()),
    TableColumn(field="deaths_per_mil", title="Total Deaths per Million", editor=IntEditor()),
    TableColumn(field="deaths_per_mil_daily", title="Daily Deaths per Million", editor=IntEditor()),
]
data_table = DataTable(source=source, columns=columns, editable=False, width=2800,
                       index_position=-1, index_header="row index", index_width=60)

# allow for interactive legend
p1.legend.click_policy="hide"
p2.legend.click_policy="hide"
p3.legend.click_policy="hide"
p4.legend.click_policy="hide"

# set legend font size
p1.legend.label_text_font_size="8pt"
p2.legend.label_text_font_size="8pt"
p3.legend.label_text_font_size="8pt"
p4.legend.label_text_font_size="8pt"

# show the results in a web browser
show(column(gridplot([[p1, p2], [p3, p4]]), data_table))