import requests
r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/complete')
print(r.json())
data = r.json()


orisa_gamewon = data['quickPlayStats']['topHeroes']['orisa']['gamesWon']
orisa_weaponAccu = data['quickPlayStats']['topHeroes']['orisa']['weaponAccuracy']
orisa_multikills = data['quickPlayStats']['topHeroes']['orisa']["multiKillBest"] 
orisa_objkill = data['quickPlayStats']['topHeroes']['orisa']["objectiveKills"] 
orisa_winper = data['quickPlayStats']['topHeroes']['orisa']["winPercentage"] 
orisa_elimperlife = data['quickPlayStats']['topHeroes']['orisa']['eliminationsPerLife']

def get_zarya_data(data):
    zarya_elimperlife = data['quickPlayStats']['topHeroes']['zarya']['eliminationsPerLife']
    zarya_weaponAcc = data['quickPlayStats']['topHeroes']['zarya']['weaponAccuracy']
    zarya_gamewon = data['quickPlayStats']['topHeroes']['zarya']["gamesWon"] 
    zarya_multikill = data['quickPlayStats']['topHeroes']['zarya']["multiKillBest"] 
    zarya_objkill = data['quickPlayStats']['topHeroes']['zarya']["objectiveKills"] 
    zarya_winper = data['quickPlayStats']['topHeroes']['zarya']["winPercentage"] 
    
    return [zarya_elimperlife, zarya_weaponAcc, zarya_gamewon, zarya_multikill, zarya_objkill, zarya_winper]




import datetime
Current_Date = datetime.date.today()

import csv


with open ('herodata.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('herodata.csv' , 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow([Current_Date] + get_zarya_data(data))



