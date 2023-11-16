import requests

respose = requests.get(url="http://api.open-notify.org/iss-now.json")
respose.raise_for_status()

data = respose.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
print('te')