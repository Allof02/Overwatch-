# try to have all your imports at the beginning of each file

# install "Trailing spaces" extension in VS code, this will highlight all the extra white spaces at the end of the file and you can remove them

import requests

# if you're using an api, it's common to have some sample in the code file to explain the expected behaviour.
'''
    https://ow-api.com/v1/stats/pc/us/Z9HONG-1578/heroes/roadhog      API for specific heroes
    https://ow-api.com/v1/stats/pc/us/Z9HONG-1578/complete  MORE INFO

    Example output:

        Username: Z9HONG
        Level: 57
        Portrait: https://d15f34w2p8l1cc.cloudfront.net/overwatch/1d754ab4338bb097f0bb7d69fe4f14c41599bc5b3ea5fa21fef68a5a1b4f9796.png
        ---QuickPlay---
        Playtime: 47:05:46
        Won: 181
        ---Competitive---
        Playedtime: 48:49
        Won: 3
        Lost: 2
        Draw: 0
        Played: 5
        Win Rate: 
        ---Ranking---
        [Tank]
        Rank: 2631
        IMG: https://d1u1mce87gyfbn.cloudfront.net/game/rank-icons/rank-PlatinumTier.png
        [Damage]
        Rank: 
        IMG: 
        [Support]
        Rank: 
        IMG: 
        CurrentTime: 13:04:33
'''


r = requests.get('https://owapi.io/profile/pc/us/ZEROTWO-12301')
print(r.json())
data = r.json()



private = data['private']

username = data["username"]
level = data["level"]
levelframe = data['levelFrame']
portrait = data["portrait"]

quickplay = data["games"]['quickplay']
qpwon = data['games']['quickplay']['won']
# remove comment
#qptotal = data['games']['quickplay']['played']       !!!Some players' profile doesn't show total played games for Quickplay!!! 下周一对此处修改
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

# try to have all your imports at the beginning of each file

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#do a loop, for example, if private is true, then stop importing csv and print 'private', if private is false, then continue to import csv
#

# Remove testing code, only leave in comments to explain things
#if private == 'false'
   # print('Private')
        #break
#else:

# try to have all your imports at the beginning of each file

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
    csv_writer.writerow(['---QuickPlay---'])
    csv_writer.writerow(['Playtime:'] + [qptime])
    csv_writer.writerow(['Won:'] + [qpwon])
    # remove comments
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
    csv_writer.writerow(['CurrentTime:'] + [current_time])




#  maybe move this to top above r = requests.get(...) line.

   ### https://ow-api.com/v1/stats/pc/us/Z9HONG-1578/heroes/roadhog      API for specific heroes ###
   ### https://ow-api.com/v1/stats/pc/us/Z9HONG-1578/complete  MORE INFO ###


    
    


























