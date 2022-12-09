import json

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models.widgets import Select

# load the data from the JSON file
with open('country_statistics1_2022-11-28.json') as f:
    data = json.load(f)

# create a ColumnDataSource with the data
source = ColumnDataSource(data=data)

# create a figure and add a line renderer
p = figure(title='COVID-19 Death Rates')
p.line('x', 'y1', source=source, legend_label='y = x^2')

# create a select widget to choose the data to display
select = Select(options=['y1', 'y2'], value='y1')

# create a callback function to update the line renderer when the selection is changed
def update_data(attr, old, new):
    p.line('x', select.value, source=source, legend_label='y = x^' + select.value[1])

# attach the callback function to the select widget
select.on_change('value', update_data)

# create a layout and add the figure and select widget
layout = row(p, select)

# output the plot to a file
output_file('covid_deaths.html')

# show the plot
show(layout)
