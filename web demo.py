
import requests

r = requests.get('https://owapi.io/profile/pc/us/ZEROTWO-12301')
print(r.json())
data = r.json()


username = data["username"]
level = data["level"]
levelframe = data['levelFrame']
portrait = data["portrait"]

quickplay = data["games"]['quickplay']
qpwon = data['games']['quickplay']['won']
qptotal = data['games']['quickplay']['played']
qptime = data['playtime']['quickplay']

comp = data["games"]['competitive']
comptime = data['playtime']['competitive']
compwon = data['games']['competitive']['won']
complose = data['games']['competitive']['lost']
compdraw = data['games']['competitive']['draw']
comptotal = data['games']['competitive']['played']
compwinrate = data['games']['competitive']['win_rate']

tankrank = data['competitive']['tank']['rank']
tankrank_img = data['competitive']['tank']['rank_img']

dpsrank = data['competitive']['damage']['rank']
dpsrank_img = data['competitive']['damage']['rank_img']

suprank = data['competitive']['support']['rank']
suprank_img = data['competitive']['support']['rank_img']

import csv

with open ('xxx.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('xxx.csv' , 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow(['Username:'] + [username])
    csv_writer.writerow(['Level:'] + [level])
    csv_writer.writerow(['Portrait:'] + [portrait])
    csv_writer.writerow(['Playtime (Quickplay):'] + [qptime])


























