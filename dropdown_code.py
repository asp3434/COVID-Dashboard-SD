from bokeh.io import show
from bokeh.models import Dropdown, SetValue, CustomJS
from bokeh.layouts import row
from bokeh.events import Event

import json

web_menu_array = [("Worldometers", "worldometers")]
website_menu = Dropdown(
    label = "Website",
    button_type = "primary",
    menu = web_menu_array
    )

website_callback = SetValue(obj = website_menu, attr='label', value='Worldometers')
website_menu.js_on_event("menu_item_click", website_callback)

f = open('country_statistics1_2022-11-28.json')
data = json.load(f)

keys = data.keys()
country_menu_array = []
for i in keys:
    # for j in range(len(i)):
    #     if j == 0:
    #         letter = i[j].upper()
    country_menu_array.append((i[0].upper() + i[1:-1] + i[-1], i))

country_menu = Dropdown(
    label = "Country",
    button_type = "default",
    menu = country_menu_array
)

country_callback = SetValue(obj=country_menu, attr='label', value= "Country Selected")
country_menu.js_on_event('menu_item_click', country_callback)


show(row(website_menu, country_menu))