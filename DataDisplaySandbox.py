import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show 
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import column, row, layout
from bokeh.models import Select, DatetimeTickFormatter, CustomJS
from bokeh.io import curdoc, show 
from datetime import datetime, timedelta
import json
import string


# initialize json file date range that will be indexed from
start_date = date(2022,11,28)
end_date = date.today()
delta = timedelta(days=1)

# initialize stat lists
tot_deaths = []
tot_deaths_1m = []
daily_deaths = []
daily_deaths_1m = []

#create a function that filters the dataframe by country and date range and returns a ColumnDataSource 
def make_dataset(country, start_date, end_date):
    all_dates = []
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
        #needs to return the tot_deaths
    
# ADD**: make sure works if skip a day of json file

#create a function that returns a figure object
def make_plot(src):
    p = figure(title="daily deaths in " + str(country) + " vs time", 
                 x_axis_label='date',
                 y_axis_label='daily deaths', 
                 x_axis_type="datetime",
                 sizing_mode="stretch_width",
                max_width=700,height=400,)
    # add line
    p.line(all_dates, daily_deaths, color="navy", line_width=1, source = src)
    # format x axis date ticks
    p.xaxis[0].formatter = DatetimeTickFormatter(days="%m / %d")
    # show the results
    return p

#create a function that returns a layout object
def make_layout(country, date_range):
    web_menu_array = [("Worldometers", "worldometers")]
    #access one json file to get countries list
    f = open('country_statistics1_2022-11-28.json')
    data = json.load(f)
    # pull countries out of the json file
    keys = data.keys()
    country_menu_array = []
    for i in keys:
        country_menu_array.append((i[0].upper() + i[1:-1] + i[-1], i))
    #create a select widget 
    select_country = Select(title="Select Country:",
                    value = country_menu_array,
                    options= country_menu_array)
    select_country.js_on_change("value", CustomJS(code="""
        console.log('select: value=' + this.value, this.toString())"""))
    select_website = Select(title="Select Website:",
                    value = country_menu_array,
                    options= web_menu_array)
    select_website.js_on_change("value", CustomJS(code="""
        console.log('select: value=' + this.value, this.toString())"""))
    #create a plot
    plot = make_plot(make_dataset(country, '2022-11-28', '2022-11-29'))
    #create a layout and add the plot and widget
    dropdown = row(select_website, select_country)
    layout = column(dropdown, plot)
    return layout
    
def update_plot(attr, old, new):
    #get the current value of the select widget
    country = select_country.value
    #update the plot
    layout.children[1] = make_plot(make_dataset(country, '2022-11-28', '2022-11-29' ))    

#set the country to usa
country= 'usa'

#create a layout
layout = make_layout(country, date_range)
curdoc().add_root(layout)

select_country = layout.children[0]
select_country.on_change("value", update_plot)
