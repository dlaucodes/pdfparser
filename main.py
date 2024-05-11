import csv

FILE_PATH = 'biostats.csv' #we can edit whatever file gets uploaded into here to parse the data

with open(FILE_PATH, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)