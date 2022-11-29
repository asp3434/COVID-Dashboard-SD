import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import date
 

def scrape_country(country: str, url:str):
    
    country = country.lower()
    
    # account for different possible inputs
    ##############################################
    if country == "united states":
        country = "usa"
    elif country == "united states of america":
        country = "usa"
    elif country == "us":
        country = "usa"
    elif country == "u.s.a.":
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
    elif country == "u.k.":
        country = "uk"     
        
    elif country == "united arab emirates":
        country = "uae"
    elif country == "u.a.e.":
        country = "uae"
        
    elif country == "democratic republic of the congo":
        country = "drc"
        
    elif country == "central african republic":
        country = "car"
    #################################################    
    
    URL1 = "https://www.worldometers.info/coronavirus/"
    #URL2 = "https://www.nytimes.com/interactive/2021/world/covid-cases.html"
    
    URL_list = [URL1]#, URL2]
    
    if url not in URL_list:
        raise ValueError("The given url is not an acceptable parameter for this function. Please choose a website from the URL list.")
    
    if (url == URL1):
        # Request the website and organize the html into readable data. Find the table in the html.
        # All data in this if statement is from "https://www.worldometers.info/coronavirus/"
        r = requests.get(URL1)
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table')
        
        # Put the table into a Pandas data frame.
        df= pd.read_html(str(table), displayed_only=False)[0]
        M, N = df.shape
        df = df.fillna(0)
        
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
        today = date.today().isoformat()
        with open('country_statistics1_'+ today + '.json', 'w') as f:
            f.write(json.dumps(country_statistics1))
            
        # return the country's statistics
        if country_statistics1.get(country) == None:
            return print('The country you have entered is not in list of possible countries. Try again.')
        
        else:    
            return country_statistics1.get(country)
        
    # elif (url == URL2):
        
    #     r = requests.get(URL2)
    #     soup = BeautifulSoup(r.text, 'html.parser')
    #     table = soup.find('table')

d = scrape_country("usa", "https://www.worldometers.info/coronavirus/")