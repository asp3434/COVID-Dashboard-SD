import random
from datetime import datetime, timedelta, date

from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show

# generate list of dates (today's date in subsequent weeks)
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]

# generate 25 random data points
y = random.sample(range(0, 100), 26)

# create new plot
p = figure(
    title="datetime axis example",
    x_axis_type="datetime",
    sizing_mode="stretch_width",
    max_width=500,
    height=250,
)

# add renderers
p.line(dates, y, color="navy", line_width=1)

# format axes ticks
p.xaxis[0].formatter = DatetimeTickFormatter(days="%m %d")

# show the results
show(p)