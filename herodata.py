import requests
r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/complete')
print(r.json())
data = r.json()

def get_orisa_data(data):
    orisa_gamewon = data['quickPlayStats']['careerStats']['orisa']['game']['gamesWon']
    orisa_weaponAccu = data['quickPlayStats']['careerStats']['orisa']['combat']['weaponAccuracy']
    orisa_multikills = data['quickPlayStats']['topHeroes']['orisa']["multiKillBest"] 
    orisa_objkill = data['quickPlayStats']['careerStats']['orisa']['combat']["objectiveKills"] 
    orisa_winper = data['quickPlayStats']['careerStats']['orisa']['game']["winPercentage"] 
    orisa_elimperlife = data['quickPlayStats']['careerStats']['orisa']['average']['eliminationsPerLife']

    return [orisa_gamewon, orisa_weaponAccu, orisa_multikills, orisa_objkill, orisa_winper, orisa_elimperlife]

def get_dva_data(data):
    dva_gamewon = data['quickPlayStats']['careerStats']["dVa"]['game']["gamesWon"]
    dva_weaponAccu = data['quickPlayStats']['careerStats']["dVa"]['combat']["weaponAccuracy"]
    dva_multikills = data['quickPlayStats']['careerStats']["dVa"]['best']["multikillsBest"]
    dva_objkill = data['quickPlayStats']['careerStats']["dVa"]['combat']["objectiveKills"]
    dva_winper = data['quickPlayStats']['careerStats']["dVa"]['game']["winPercentage"]
    dva_elimperlife = data['quickPlayStats']['careerStats']["dVa"]['average']["eliminationsPerLife"]

    return [dva_gamewon, dva_weaponAccu, dva_multikills, dva_objkill, dva_winper, dva_elimperlife]



def get_zarya_data(data):
    zarya_elimperlife = data['quickPlayStats']['careerStats']['zarya']['average']['eliminationsPerLife']
    zarya_weaponAcc = data['quickPlayStats']['careerStats']['zarya']['combat']['weaponAccuracy']
    zarya_gamewon = data['quickPlayStats']['careerStats']['zarya']['game']["gamesWon"] 
    zarya_multikill = data['quickPlayStats']['careerStats']['zarya']['best']["multikillsBest"] 
    zarya_objkill = data['quickPlayStats']['careerStats']['zarya']['combat']["objectiveKills"] 
    zarya_winper = data['quickPlayStats']['careerStats']['zarya']['game']["winPercentage"] 
    
    return [zarya_elimperlife, zarya_weaponAcc, zarya_gamewon, zarya_multikill, zarya_objkill, zarya_winper]

def get_sigma_data(data):
    sig_gamewon = data['quickPlayStats']['careerStats']['sigma']['game']['gamesWon']
    sig_weaponAccu = data['quickPlayStats']['topHeroes']['sigma']['weaponAccuracy']
    sig_multikills = data['quickPlayStats']['careerStats']['sigma']['best']['multikillsBest']
    sig_objkill = data['quickPlayStats']['careerStats']['sigma']['combat']['objectiveKills']
    sig_winper = data['quickPlayStats']['careerStats']['sigma']['game']['winPercentage']
    sig_elimperlife = data['quickPlayStats']['careerStats']['sigma']['average']['eliminationsPerLife']

    return [sig_gamewon, sig_weaponAccu, sig_multikills, sig_objkill, sig_winper, sig_elimperlife]




import datetime
Current_Date = datetime.date.today()

import csv


with open ('herodata.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('herodata.csv' , 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow([Current_Date] + get_zarya_data(data) + get_orisa_data(data) + get_dva_data(data) + get_sigma_data(data))



