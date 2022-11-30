import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date

# URL1 = "https://www.worldometers.info/coronavirus/"
URL2 = "https://www.nytimes.com/interactive/2021/world/covid-cases.html"

# r1 = requests.get(URL1)
r2 = requests.get(URL2)

# soup1 = BeautifulSoup(r1.text, 'html.parser')
soup2 = BeautifulSoup(r2.text, 'html.parser')

# table = soup2.findAll('table', class_ = "g-table super-table withchildren")
# df1= pd.read_html(str(table), displayed_only=False)[0]
# M, N = df1.shape


# df1 = df1.fillna(0)

# country_statistics1 = {}
# for i in range(8, M-1, 1):
#     # an array to grab total deaths, new deaths (daily), deaths per million, and deaths per million (daily)
#     array = [df1.iloc[i, 4], df1.iloc[i, 5], df1.iloc[i, 11], df1.iloc[i, 20] ]
#     country_statistics1[df1.iloc[i, 1]] = array

# with open('country_statistics1.json', 'w') as f:
#     f.write(json.dumps(country_statistics1)) 