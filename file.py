import csv

with open ('xxx.csv' , newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

with open('xxx.csv' , 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ' ')
    csv_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    csv_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    