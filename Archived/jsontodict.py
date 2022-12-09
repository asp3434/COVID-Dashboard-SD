# importing the module
import json
 
# Opening JSON file
with open('country_statistics1_2022-11-28.json') as json_file:
    data = json.load(json_file)
    # Print the type of data variable
    array =list(data.keys())
    print("Type:", array)
 