from bokeh.layouts import column
from bokeh.models import (ColumnDataSource, DataTable, HoverTool, IntEditor,
                          NumberEditor, NumberFormatter, SelectEditor,
                          StringEditor, StringFormatter, TableColumn)
from bokeh.plotting import figure, show
from bokeh.sampledata.autompg2 import autompg2 as mpg

source = ColumnDataSource(mpg)
print(mpg)

manufacturers = sorted(mpg["manufacturer"].unique())

columns = [
    TableColumn(field="manufacturer", title="Manufacturer",
                editor=SelectEditor(options=manufacturers),
                formatter=StringFormatter(font_style="bold")),
    TableColumn(field="cty", title="City MPG", editor=IntEditor()),
    TableColumn(field="hwy", title="Highway MPG", editor=IntEditor()),
]
data_table = DataTable(source=source, columns=columns, editable=True, width=800,
                       index_position=-1, index_header="row index", index_width=60)

p = figure(width=800, height=300, tools="pan,wheel_zoom,xbox_select,reset", active_drag="xbox_select")

cty = p.circle(x="index", y="cty", fill_color="#396285", size=8, alpha=0.5, source=source, legend_label="total deaths")
hwy = p.circle(x="index", y="hwy", fill_color="#CE603D", size=8, alpha=0.5, source=source, legend_label="daily deaths")

tooltips = [
    ("Manufacturer", "@manufacturer")
]
cty_hover_tool = HoverTool(renderers=[cty], tooltips=tooltips + [("City MPG", "@cty")])
hwy_hover_tool = HoverTool(renderers=[hwy], tooltips=tooltips + [("Highway MPG", "@hwy")])

p.add_tools(cty_hover_tool, hwy_hover_tool)

p.legend.click_policy="hide"

show(column(p, data_table))


