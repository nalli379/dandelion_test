import webbrowser
import csv
from api_key import api_key


API_KEY = api_key

def list_local_libraries(local_area_name):
    
    list_libraries = []
    
    with open('public_libraries_eng.csv', 'r') as file:
        csvFile = csv.DictReader(file)
        for row in csvFile:
            area_name = row['area_name']
            location = row['location']
            postcode = row['postcode']
            
            if local_area_name == area_name:
                list_libraries.append((location, postcode))
    
    return list_libraries


def local_libraries_formaturl(list_libraries):
    
    formatted_list = []
    
    for address in list_libraries:
        location, postcd = address
        loc = location.replace(',',"")
        location = loc.replace(" ", "+")
        postcode= postcd.replace(" ", "+")
        
        formatted_string = (location, postcode)
        
        formatted_list.append(formatted_string)
    
    return formatted_list


def open_url(formatted_list):
    
    test_list = formatted_list[0]
    street, postcode = test_list  
        
    map_url = f"https://www.google.com/maps/search/?api=1&query={street}%2C+{postcode}"
         
    return webbrowser.open(map_url)
    

test = local_libraries_formaturl(list_local_libraries("Barnet"))
    
open_url(test)






