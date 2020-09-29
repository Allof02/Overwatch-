import requests
r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/heroes/doomfist')
print(r.json())
data = r.json()

elimPerLife = data['quickPlayStats']['topHeroes']['doomfist']['eliminationsPerLife']

print(elimPerLife)

import datetime
Current_Date = datetime.date.today()

import csv


with open ('DoomfistDamage.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('DoomfistDamage.csv' , 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow(['CurrentDate', 'elimPerLife'])
    csv_writer.writerow([Current_Date , elimPerLife])