
import requests

r = requests.get('https://owapi.io/profile/pc/us/Z9HONG-1578')
print(r.json())
data = r.json()

#Variables

private = data['private']

username = data["username"]
level = data["level"]
levelframe = data['levelFrame']
portrait = data["portrait"]

quickplay = data["games"]['quickplay']
qpwon = data['games']['quickplay']['won']
#qptotal = data['games']['quickplay']['played']       !!!Some players' profile doesn't show total played games for Quickplay!!!
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

#Tring to do a loop, for example, if private is true, then stop importing csv and print 'private', if private is false, then continue to import csv
#but dont know how =.=

#if private == 'false'
   # print('Private')
        #break
#else:

import csv

#CSV WRITERS 

with open ('xxx.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('xxx.csv' , 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow(['Username:'] + [username])
    csv_writer.writerow(['Level:'] + [level])
    csv_writer.writerow(['Portrait:'] + [portrait])
    csv_writer.writerow(['---QuickPlay---'])
    csv_writer.writerow(['Playtime:'] + [qptime])
    csv_writer.writerow(['Won:'] + [qpwon])
    #csv_writer.writerow(['Played:'] + [qptotal])          
    csv_writer.writerow(['---Competitive---'])
    csv_writer.writerow(['Playedtime:'] + [comptime])
    csv_writer.writerow(['Won:'] + [compwon])
    csv_writer.writerow(['Lost:'] + [complose])
    csv_writer.writerow(['Draw:'] + [compdraw])
    csv_writer.writerow(['Played:'] + [comptotal])
    csv_writer.writerow(['Win' , 'Rate:'] + [compwinrate])
    csv_writer.writerow(['---Ranking---'])
    csv_writer.writerow(['[Tank]'])
    csv_writer.writerow(['Rank:'] + [tankrank])
    csv_writer.writerow(['IMG:'] + [tankrank_img])
    csv_writer.writerow(['[Damage]'])
    csv_writer.writerow(['Rank:'] + [dpsrank])
    csv_writer.writerow(['IMG:'] + [dpsrank_img])
    csv_writer.writerow(['[Support]'])
    csv_writer.writerow(['Rank:'] + [suprank])
    csv_writer.writerow(['IMG:'] + [suprank_img])


    
    


























