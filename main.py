import csv

FILE_PATH = 'biostats.csv' #we can edit whatever file gets uploaded into here to parse the data

class BioStats:
    HAS_HEADERS = True
    NAME_COL = 0
    SEX_COL = 1
    AGE_COL = 2
    HEIGHT_COL = 3
    WEIGHT_COL = 4 

with open(FILE_PATH, 'r') as f:
    reader = csv.reader(f)
    headers = []

    if BioStats.HAS_HEADERS:
        headers = next(reader)

    for line in reader:
        if line and len(line) > BioStats.WEIGHT_COL:

            name = line[BioStats.NAME_COL]
            age = int(line[BioStats.AGE_COL])

            if age > 19 and age < 30:
                print(f'{name} is {age} years old')

