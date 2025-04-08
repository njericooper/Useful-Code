import requests
import csv


r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36') 

r_text = r.text
r_json = r.json()

# Access data as JSON string
print(r.text)
 
# Access decoded JSON data as Python object
print(r.json())

print(r_text)
print(r_json)

with open('census.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())


r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())

r_json = r.json()
