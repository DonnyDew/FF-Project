import csv

with open("Playoff_Stats.csv",encoding = 'utf8') as f:
    data = csv.reader(f)
    teams = {}
    for row in data:
        teams[row[0]] = {'teamName':row[1],'year':row[2],'rWins':int(row[3]), 'seed':int(row[4]), 'difference':int(row[5]),\
             'SOS':float(row[6]),'SOV':float(row[7]),'pRound':int(row[8]),'pWins':int(row[9])}

Champs = []


for i in teams:
   if teams[i]['pRound'] == 5:
        Champs.append(teams[i]['teamName'])

for i in teams:
    if teams[i]['SOV'] < .400:
        print(teams[i]['pWins'])       

        






