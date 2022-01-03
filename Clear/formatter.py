import json

with open('ips_located.json', 'r') as f:
    j = json.load(f)
### step 1: organize the locations
# create a list of all country codes
i = 0
countries = []
for item in j:
    for key, value in j[i].items():
        if key == 'country':
            countries.append(value)
    i = i + 1
# sort the list alphabetically 
countries.sort()
# remove duplicate country codes
countries = list(dict.fromkeys(countries))
# for each country, find all the regions
region = []
i = 0
for item in j:
    for key, value in j[i].items():
        if key == 'country':
            if value == countries[0]:
                for key, value in j[i].items():
                    if key == 'region':
                        region.append(value)
    i = i + 1
# sort each region for each country alphabetically, and remove duplicates
region.sort()
region = list(dict.fromkeys(region))
# for each region, find all cities
cities = []
i = 0
for item in j:
    for key, value in j[i].items():
        if key == 'region':
            if value == region[0]:
                for key, value in j[i].items():
                    if key == 'city':
                        cities.append(value)
    i = i + 1
# sort each city for each region alphabetically, and remove duplicates
cities.sort()
cities = list(dict.fromkeys(cities))

with open('ips_formatted.json', 'w') as o:
    json.dump(countries, o, indent=4)

