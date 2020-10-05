import requests
r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/complete')
print(r.json())
data = r.json()

def get_orisa_data(data):
    orisa_gamewon = data['quickPlayStats']['topHeroes']['orisa']['gamesWon']
    orisa_weaponAccu = data['quickPlayStats']['topHeroes']['orisa']['weaponAccuracy']
    orisa_multikills = data['quickPlayStats']['topHeroes']['orisa']["multiKillBest"] 
    orisa_objkill = data['quickPlayStats']['topHeroes']['orisa']["objectiveKills"] 
    orisa_winper = data['quickPlayStats']['topHeroes']['orisa']["winPercentage"] 
    orisa_elimperlife = data['quickPlayStats']['topHeroes']['orisa']['eliminationsPerLife']

    return [orisa_gamewon, orisa_weaponAccu, orisa_multikills, orisa_objkill, orisa_winper, orisa_elimperlife]

def get_dva_data(data):
    dva_gamewon = data['quickPlayStats']['topHeroes']["dVa"]["gamesWon"]
    dva_weaponAccu = data['quickPlayStats']['topHeroes']["dVa"]["weaponAccuracy"]
    dva_multikills = data['quickPlayStats']['topHeroes']["dVa"]["multiKillBest"]
    dva_objkill = data['quickPlayStats']['topHeroes']["dVa"]["objectiveKills"]
    dva_winper = data['quickPlayStats']['topHeroes']["dVa"]["winPercentage"]
    dva_elimperlife = data['quickPlayStats']['topHeroes']["dVa"]["eliminationsPerLife"]

    return [dva_gamewon, dva_weaponAccu, dva_multikills, dva_objkill, dva_winper, dva_elimperlife]



def get_zarya_data(data):
    zarya_elimperlife = data['quickPlayStats']['topHeroes']['zarya']['eliminationsPerLife']
    zarya_weaponAcc = data['quickPlayStats']['topHeroes']['zarya']['weaponAccuracy']
    zarya_gamewon = data['quickPlayStats']['topHeroes']['zarya']["gamesWon"] 
    zarya_multikill = data['quickPlayStats']['topHeroes']['zarya']["multiKillBest"] 
    zarya_objkill = data['quickPlayStats']['topHeroes']['zarya']["objectiveKills"] 
    zarya_winper = data['quickPlayStats']['topHeroes']['zarya']["winPercentage"] 
    
    return [zarya_elimperlife, zarya_weaponAcc, zarya_gamewon, zarya_multikill, zarya_objkill, zarya_winper]

def get_sigma_data(data):
    sig_gamewon = data['quickPlayStats']['topHeroes']['sigma']['gamesWon']
    sig_weaponAccu = data['quickPlayStats']['topHeroes']['sigma']['weaponAccuracy']
    sig_multikills = data['quickPlayStats']['topHeroes']['sigma']['multiKillBest']
    sig_objkill = data['quickPlayStats']['topHeroes']['sigma']['objectiveKills']
    sig_winper = data['quickPlayStats']['topHeroes']['sigma']['winPercentage']
    sig_elimperlife = data['quickPlayStats']['topHeroes']['sigma']['eliminationsPerLife']

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



