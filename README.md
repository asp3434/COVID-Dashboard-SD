# COVID-Dashboard-SD
A COVID dashboard project for ME EN 5900/6900 at the University of Utah.

### ScrapeWebsite.py
A module for scraping the following websites:

"https://www.worldometers.info/coronavirus/"

"https://www.nytimes.com/interactive/2021/world/covid-cases.html"

#### scrape_country
This is a function in the ScrapeWebsite.py module that takes two parameter inputs and returns an array. The first input is a string of the country that the user wants to pull statistics for e.g. "USA" or "Iran". The second input is the exact url that the user desires to pull information from. If the url is not in the list of possible websites, the code will raise an error (this function is not yet implemented). Given both parameters that are entered into the function are valid, it will return the following: [Total number of deaths, New deaths today, Total number of deaths per million of population, New deaths today per million of population].

The output is a json file sorted country by country with the four statistics corresponding to each country:
                {"usa": [1105663.0, 79.0, 3302.0, 0.2], "india": [530620.0, 0.0, 377.0, 0.0] ...
                
To run scrape_country you can run the scrape_website.py script.
You can also run DataDisplayCurrent.py to see a plot of statistics for a country
            
