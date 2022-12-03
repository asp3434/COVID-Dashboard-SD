from bokeh.io import show
from bokeh.models import Dropdown, SetValue, CustomJS, Select
from bokeh.layouts import row
from bokeh.events import Event
from bokeh.events import ButtonClick
import json

web_menu_array = [("Worldometers", "worldometers")]
#Old Dropdown code
#website_menu = Dropdown(
#    label = "Website",
#    button_type = "primary",
#    menu = web_menu_array
#    )
#website_callback = SetValue(obj = website_menu, attr='label', value='Worldometers')
#website_menu.js_on_event("menu_item_click", website_callback)

f = open('country_statistics1_2022-11-28.json')
data = json.load(f)

keys = data.keys()
country_menu_array = []
for i in keys:
    country_menu_array.append((i[0].upper() + i[1:-1] + i[-1], i))

#Old Dropdown Code
#country_menu = Dropdown(
#    label = "Country",
#    button_type = "default",
#    menu = country_menu_array
#)
#def grabcountryname(event):
#    if event.item in country_menu_array:  
#country_callback = SetValue(obj=country_menu, attr='label', value= "country selected")
#country_menu.js_on_change('value', country_callback)

select_country = Select(title="Select Country:",  
                options= country_menu_array)
select_country.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())"""))

select_website = Select(title="Select Website:",  
                options= web_menu_array)
select_website.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())"""))


show(row(select_website, select_country))