
import requests

r = requests.get('https://owapi.io/profile/pc/us/ZEROTWO-12301')
print(r.json())
data = r.json()

data["username"]
username = data["username"]

data["level"]
level = data["level"]

data["portrait"]
portrait = data["portrait"]

data["games"]['quickplay']
quickplay = data["games"]['quickplay']

data["games"]['competitive']
comp = data["games"]['competitive']


quickplay = data["games"]['quickplay']

print(quickplay)
print(comp)









