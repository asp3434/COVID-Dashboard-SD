from bokeh.io import show
from bokeh.models import CustomJS, DatePicker
 
dp = DatePicker(title = 'Select date', value = "2021-06-09",
                min_date = "2020-10-01", max_date = "2021-12-31")

show(dp)

from bokeh.io import show
from bokeh.models import CustomJS, Dropdown
 
menu = [("First", "First"), ("Second", "Second"), ("Third", "Third")]
 
dropdown = Dropdown(label="Dropdown Menu", button_type="success", menu=menu)
 
dropdown.js_on_event("menu_item_click", CustomJS(
    code="console.log('dropdown: ' + this.item, this.toString())"))
 
show(dropdown)