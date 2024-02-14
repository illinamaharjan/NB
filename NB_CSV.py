import csv
import requests

api_token = 'a2dfaadc1888855e9fc90a221d47993680a3f638'
headers = {
    'Authorization': f'Token {api_token}',
    'Content-Type': 'application/json',
}
url = 'https://192.168.200.21/api/dcim/sites/'

with open(r'C:\Users\illina.maharjan\OneDrive - hotwirecommunication.com\Hotwire Project\Netbox_data\All-Active-Properties.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        property_name = row['PROPERTY NAME']
        street = row['STREET']
        city = row['CITY']
        
        data = {
            'name': property_name,
            'address': f'{street}, {city}',
        }
        
        response = requests.post(url, headers=headers, json=data)
        

        if response.status_code == 201:
            print(f"Object {property_name} created successfully")
        else:
            print(f"Error creating object {property_name}: {response.status_code} - {response.text}")