import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import string

def scrape_country(country, url):
    
    country = country.lower()
    
    # account for different possible inputs
    ##############################################
    if country == "united states":
        country = "usa"
    elif country == "united states of america":
        country = "usa"
    elif country == "us":
        country = "usa"
          
    elif country == "north korea":
        country = "dprk"
    elif country == "n korea":
        country = "dprk"
    elif country == "n. korea":
        country = "dprk"
        
    elif country == "south korea":
        country = "s. korea"
    elif country == "s korea":
        country = "s. korea"
        
    elif country == "united kingdom":
        country = "uk"
    elif country ==  "britain":
        country = "uk"
    elif country ==  "great britain":
        country = "uk"
    elif country ==  "england":
        country = "uk"     
        
    elif country == "united arab emirates":
        country = "uae"
        
    elif country == "democratic republic of the congo":
        country = "drc"
        
    elif country == "central african republic":
        country = "car"
    #################################################    
    
    URL1 = "https://www.worldometers.info/coronavirus/"
    URL2 = "https://www.nytimes.com/interactive/2021/world/covid-cases.html"
    
    if (url == URL1):
        # Request the website and organize the html into readable data. Find the table in the html.
        # All data in this if statement is from "https://www.worldometers.info/coronavirus/"
        r = requests.get(URL1)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table')
        
        # Put the table into a Pandas data frame.
        df= pd.read_html(str(table), displayed_only=False)[0]
        M, N = df.shape
        
        # Populate a dicitionary with all the countries and 4 primary statistics.
        country_statistics1 = {}
        for i in range(8, M-1, 1):
            # An array to grab total deaths, new deaths (daily), deaths per million, and deaths per million (daily)
            array = [df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 11], df.iloc[i, 20] ]
            if df.iloc[i, 1].lower() == "total:":
                pass
            else:
                country_statistics1[df.iloc[i, 1].lower()] = array
            
        # Write the dictionary to a .json file
        with open('country_statistics1.json', 'w') as f:
            f.write(json.dumps(country_statistics1))
            
        # return the country's statistics
        if country_statistics1.get(country) == None:
            return print('The country you have entered is not in list of possible countries. Try again.')
        
        else:    
            return country_statistics1.get(country)
        
    #elif (url == URL2):
        
    # r2 = requests.get(URL2)
    # soup2 = BeautifulSoup(r2.text, 'html.parser')
    