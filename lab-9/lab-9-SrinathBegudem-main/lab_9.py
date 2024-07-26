# Lab 9
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
import requests
from bs4 import BeautifulSoup
import json

def sky_scraper(url):
    # Send a GET request to fetch the web page content
    response = requests.get(url)

    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing space launches
    launch_table = soup.find('table', class_='wikitable')

    all_rows = launch_table.find_all('tr')[1:]
    filtered_rows = []
    for i, row in enumerate(all_rows):
        columns = row.find_all('td')
        if len(columns) == 5 or len(columns) == 6:
            filtered_rows.append(row)
        else:
            continue

    i = 0
    main_list = []
    while i < len(filtered_rows):
        row = filtered_rows[i]
        columns = row.find_all('td')
        rocket_launch = {}
        if len(columns) == 5:
            rocket_launch['datetime'] = " ".join(columns[0].stripped_strings)
            alt_text = ""
            img_tag = columns[1].find('img')
            if img_tag:
                alt_text = img_tag.get('alt')
            rocket_launch['rocket'] = columns[1].text.strip()
            rocket_launch['country'] = alt_text
            rocket_launch['flight_number'] = columns[2].text.strip()
            rocket_launch['launch_site'] = columns[3].text.strip()
            rocket_launch['lsp'] = columns[4].text.strip()
        i += 1
        pay_load = []
        while i < len(filtered_rows) and len(filtered_rows[i].find_all('td')) == 6:
            d = {}
            columns = filtered_rows[i].find_all('td')
            alt_text = ""
            img_tag = columns[0].find('img')
            if img_tag:
                alt_text = img_tag.get('alt')
            d["satellite"] = alt_text + " " + columns[0].text.strip()
            d["country"] = alt_text
            d["operator"] = columns[1].text.strip()
            d["orbit"] = columns[2].text.strip()
            d["function"] = columns[3].text.strip()
            d["decay"] = columns[4].text.strip()
            d["outcome"] = columns[5].text.strip()
            pay_load.append(d)
            i += 1

        rocket_launch['payload'] = pay_load
        main_list.append(rocket_launch)
    
    # Convert the list to JSON
    json_data = json.dumps(main_list)

    # Write JSON data to a file
    filename = "space_launches.json"
    with open(filename, "w") as json_file:
        json_file.write(json_data)

    return filename

# Test the function
url = 'https://en.wikipedia.org/wiki/List_of_spaceflight_launches_in_January%E2%80%93June_2022'
json_filename = sky_scraper(url)
print("JSON filename:", json_filename)



# ----------------- Question 2 -----------------


import requests
import xml.etree.ElementTree as ET

API_KEY = "86832188539a4bf3a768fc5706e567c0"

def get_coordinates(city):
    url = f"https://api.opencagedata.com/geocode/v1/json?key={API_KEY}&language=en&q={city}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and data['results']:
        result = data['results'][0]  # Assuming the first result is correct
        latitude = result['geometry']['lat']
        longitude = result['geometry']['lng']
        return latitude, longitude
    else:
        return None, None

def land_scraper(cities_file):
    # Read cities from file
    with open(cities_file, 'r') as file:
        cities = file.read().splitlines()

    # Create list of dictionaries containing city data
    city_data = []
    for city in cities:
        latitude, longitude = get_coordinates(city)
        if latitude is not None and longitude is not None:
            city_data.append({
                "name": city,
                "latitude": latitude,
                "longitude": longitude
            })

    # Create XML tree
    root = ET.Element("cities")
    for city in city_data:
        city_element = ET.SubElement(root, "city")
        name_element = ET.SubElement(city_element, "name")
        name_element.text = city["name"]
        latitude_element = ET.SubElement(city_element, "latitude")
        latitude_element.text = str(city["latitude"])
        longitude_element = ET.SubElement(city_element, "longitude")
        longitude_element.text = str(city["longitude"])

    # Create XML file
    xml_filename = "cities.xml"
    tree = ET.ElementTree(root)
    tree.write(xml_filename)

    return xml_filename


