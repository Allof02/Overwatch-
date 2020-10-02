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



import datetime
Current_Date = datetime.date.today()

import csv


with open ('herosdata2.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('herosdata2.csv' , 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
     # csv_writer.writerow(['current_time', 'elimperlife', 'weaponAcc', 'gamewon', 'multikill', 'objkill', 'winper'])
    csv_writer.writerow([Current_Date , orisa_elimperlife , orisa_weaponAccu, orisa_gamewon, orisa_multikills, orisa_objkill, orisa_winper])