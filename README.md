# COVID-Dashboard-SD
A COVID dashboard project for ME EN 5250/6250 at the University of Utah.

### ScrapeWebsite.py
A module for scraping the following website:

"https://www.worldometers.info/coronavirus/"

#### scrape_country
This is a function in the ScrapeWebsite.py module that takes two parameter inputs and returns an array. The first input is a string of the country that the user wants to pull statistics for e.g. "USA" or "Iran". The second input is the exact url that the user desires to pull information from. If the url is not in the list of possible websites, the code will raise an error. Given both parameters that are entered into the function are valid, it will return the following: [Total number of deaths, New deaths today, Total number of deaths per million of population, New deaths today per million of population].

The output is a json file sorted country by country with the four statistics corresponding to each country:
                {"usa": [1105663.0, 79.0, 3302.0, 0.2], "india": [530620.0, 0.0, 377.0, 0.0] ...
                
To run scrape_country you can run the scrape_website.py script.
You can also run DataDisplayCurrent.py to see a plot of statistics for a country
            
### DataDisplayCurrent.py
This script uses the bokeh module to load the .json files from ScrapeWebsite.py and display them on four plots in a web browser. The user must scroll horizontally and vertically to view all the data. Currently, it uses data from eight different .json files to show the COVID statistics over time (eight days). It takes approximately 3 minutes from the time the user runs the code to generate the plots. To let the user know that the script is running in this interval, the code prints "Code is running..." to the terminal. Each of the plots are interactive and allow the user to select an item in the legend to display the graph of a specific country. A table is shown below the graphs to give the numerical value of the data seen in the plots.