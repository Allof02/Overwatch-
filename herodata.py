import requests
r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/complete')
print(r.json())
data = r.json()

zarya_elimperlife = data['quickPlayStats']['topHeroes']['zarya']['eliminationsPerLife']
zarya_weaponAcc = data['quickPlayStats']['topHeroes']['zarya']['weaponAccuracy']

print(zarya_elimperlife)

import datetime
Current_Date = datetime.date.today()

import csv


with open ('herodata.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('herodata.csv' , 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow([Current_Date , zarya_elimperlife , zarya_weaponAcc])