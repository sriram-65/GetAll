import requests
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/sriIp')  
db = client['sriIP']  
collection = db['getip']  


phone_number = input("Please enter your phone number (in international format, e.g., +919876543210): ")


ip_response = requests.get('https://api.ipify.org?format=json')
ip_data = ip_response.json()
ip_address = ip_data['ip']


location_response = requests.get(f'https://ipinfo.io/{ip_address}/json')
location_data = location_response.json()


latitude_longitude = location_data.get('loc')
city = location_data.get('city')
region = location_data.get('region')
country = location_data.get('country')
postal = location_data.get('postal')
timezone = location_data.get('timezone')


document = {
    "phone_number": phone_number,
    "ip_address": ip_address,
    "location": {
        "latitude_longitude": latitude_longitude,
        "city": city,
        "region": region,
        "country": country,
        "postal_code": postal,
        "timezone": timezone
    }
}


result = collection.insert_one(document)


print("\nHere are the details based on your IP address:")
print(f"Your IP Address: {ip_address}")
print(f"Location (Lat, Long): {latitude_longitude}")
print(f"City: {city}")
print(f"Region: {region}")
print(f"Country: {country}")
print(f"Postal Code: {postal}")
print(f"Timezone: {timezone}")


print("*" * 30)


RED_BOLD = "\033[1;31m"
RESET = "\033[0m"

print(f"{RED_BOLD}Coded by Sriram{RESET}")


