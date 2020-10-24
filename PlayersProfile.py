import requests
import csv
import time

r = requests.get('https://ow-api.com/v1/stats/pc/us/ZEROTWO-12301/profile')
print(r.json())
data = r.json()

username = data["name"]
level = data["level"]
levelframe = data['levelIcon']
portrait = data["icon"]


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


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


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
    csv_writer.writerow(['Played:'] + [qptotal])
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
    csv_writer.writerow(['CurrentTime:'] + [current_time])

# #Example
# Username: ZEROTWO
# Level: 57
# Portrait: https://d15f34w2p8l1cc.cloudfront.net/overwatch/1d754ab4338bb097f0bb7d69fe4f14c41599bc5b3ea5fa21fef68a5a1b4f9796.png
# ---QuickPlay---
# Playtime: 47:05:46
# Won: 181
# ---Competitive---
# Playedtime: 48:49
# Won: 3
# Lost: 2
# Draw: 0
# Played: 5
# Win Rate:
# ---Ranking---
# [Tank]
# Rank: 2631
# IMG: https://d1u1mce87gyfbn.cloudfront.net/game/rank-icons/rank-PlatinumTier.png
# [Damage]
# Rank:
# IMG:
# [Support]
# Rank:
# IMG:
# CurrentTime: 13:04:33



































