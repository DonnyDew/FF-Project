# For this program to work properly you must have dowloaded the csv files
        
import csv

week = int(input("Choose what week #: "))   #Week 0 is used for the stats for the whole season which is 1-10
while week < 0 or week > 17:    
    print("Invalid week")       #since finishing the project
    week = input("Choose what week#: ")

#These functions are for displaying the different modes
def singleTeam():
    print("NFL Week",week)
    print("--------------")
    Points = 0
    try:
        print("QB:",quarterback,"-",format(QBPoints(quarterback),'.2f'))
        Points += QBPoints(quarterback)
    except: #Excepts are for when you mispell the player, they didn't play, don't exist, or other reasons they weren't on the file
        print("QB:",quarterback,"-", "Not found")
    try:
        print("RB1:",runningback1,"-", format(RBPoints(runningback1),'.2f'))
        Points += RBPoints(runningback1)
    except:
        print("RB1:",runningback1,"-", "Not found")
    try:
        print("RB2:",runningback2,"-", format(RBPoints(runningback2),'.2f'))
        Points += RBPoints(runningback2)
    except:
        print("RB2:",runningback2,"-", "Not found")
    try:
        print("WR1:",widereciever1,"-",format(WRPoints(widereciever1),'.2f'))
        Points += WRPoints(widereciever1)
    except:
        print("WR1:",widereciever1,"-", "Not found")
    try:
        print("WR2:",widereciever2,":",format(WRPoints(widereciever2),'.2f'))
        Points += WRPoints(widereciever2)
    except:
        print("WR2:",widereciever2,"-", "Not found")
    try:
        if flex_position.upper() == 'WR':
            print("Flex:",flex, "-", format(WRPoints(flex),'.2f'))
            Points += WRPoints(flex)
        elif flex_position.upper() == 'RB':
            print("Flex:",flex, "-", format(RBPoints(flex),'.2f'))
            Points += RBPoints(flex)
        elif flex_position.upper() == 'TE':
            print("Flex:",flex,"-", format(TEPoints(flex),'.2f'))
            Points += TEPoints(flex)
        else:
            print("Position entered incorrectly")
    except:
        print("Flex:",flex, "-","Not found")
    try:
        print("TE:",tightend,"-",format(TEPoints(tightend),'.2f'))
        Points += TEPoints(tightend)
    except:
        print("TE:",tightend,"-", "Not found")
    try:
        print("DEF:",defense,"-",format(DEFPoints(defense),'.2f'))
        Points += DEFPoints(defense)
    except:
        print("DEF:",defense,"-", "Not found")
    try:
        print("K:",kicker,"-",format(KPoints(kicker),'.2f'))
        Points += KPoints(kicker)
    except:
        print("K:",kicker,"-", "Not found")
            
    print("Total Points:",format(Points,'.2f'))
def indivPlayer():
    try:
        if position.upper() == 'QB':
            QBStats = QBPoints(quarterback)   #QBStats comes from a list on the function QBPoints
            print("Passing Yards:",format(QBStats[0],',.0f'))
            print("Passing TD's:",QBStats[1])
            print("Int:",QBStats[2])
            print("Rushing Yards:",QBStats[3])
            print("Rushing TD's:",QBStats[4])
            print("Rank:",QBStats[5])
            print("Points:",format(QBStats[6],'.2f'))
    except:
        print(quarterback,"not found")
    try:
        if position.upper() == 'RB':
            RBStats = RBPoints(runningback)     #RBStats comes from a list on the function RBPoints
            print("Rushing Yards:",format(RBStats[0],',.0f'))
            print("Rushing TDS:",RBStats[1])
            print("Receptions:",RBStats[2])
            print("Recieving yards:", format(RBStats[3],',.0f'))
            print("Recieving TDS:",RBStats[4])
            print("RB Rank:",RBStats[5])
            print("Points:",format(RBStats[6],'.2f'))
    except:
        print(runningback,"not found")
    try:
        if position.upper() == 'WR':    #WRStats comes from a list on the function WRPoints
            WRStats = WRPoints(widereciever)
            print("Receptions:", WRStats[0])
            print("Recieiving Yards:",format(WRStats[1],',.0f'))
            print("Recieiving TDS:",WRStats[2])
            print("WR Rank:",WRStats[3])
            print("Points:",format(WRStats[4],'.2f'))
    except:
        print(widereciever,"not found")
    try:
        if position.upper() == 'TE':
            TEStats = TEPoints(tightend)    #TEStats comes from a list on the function TEPoints
            print("Receptions:", TEStats[0])
            print("Recieiving Yards:",format(TEStats[1],',.0f'))
            print("Recieiving TDS:",TEStats[2])
            print("TE Rank:",TEStats[3])
            print("Points:",format(TEStats[4],'.2f'))
    except:
        print(tightend,"not found")
    try:
        if position.upper() == 'DEF':   #DEFStats comes from a list on the function DEFPoints
            DEFStats = DEFPoints(defense)
            print("Sacks:",DEFStats[0])
            print("Ints:",DEFStats[1])
            print("Fumbles Recovered:",DEFStats[3])
            print("TD's:",DEFStats[5])
            print("Points allowed:",DEFStats[6])
            print("Total Yards:",format(DEFStats[7],',.0f'))
            print("DEF Rank:",DEFStats[8])
            print("Points:",format(DEFStats[9],'.2f'))
    except:
        print(defense,"not found")
    try:
        if position.upper() == 'K':     #KStats comes from a list on the function KPoints
            KStats = KPoints(kicker)
            print("FG 1-19:",KStats[1])
            print("FG 20-29:",KStats[2])
            print("FG 30-39:",KStats[3])
            print("FG 40-49:",KStats[4])
            print("FG 50+:",KStats[5])
            print("Extra Points Made:",KStats[6])
            print("K Rank:",KStats[7])
            print("Points:",format(KStats[8],'.0f'))
    except:
        print(kicker,"not found")
def teamvteam():
    print("NFL Week",week)
    print("--------------")
    print("Team 1:")
    Points1 = 0     #Points need to be intialized
    try:
        print("QB:",quarterback,"-",QBPoints(quarterback))
        Points1 += QBPoints(quarterback)
    except:
        print("QB:",quarterback,"-", "Not found")
    try:
        print("RB1:",runningback1,"-", format(RBPoints(runningback1),'.2f'))
        Points1 += RBPoints(runningback1)
    except:
        print("RB1:",runningback1,"-", "Not found")
    try:
        print("RB2:",runningback2,"-", format(RBPoints(runningback2),'.2f'))
        Points1 += RBPoints(runningback2)
    except:
        print("RB2:",runningback2,"-", "Not found")
    try:
        print("WR1:",widereciever1,"-",format(WRPoints(widereciever1),'.2f'))
        Points1 += WRPoints(widereciever1)
    except:
        print("WR1:",widereciever1,"-", "Not found")
    try:
        print("WR2:",widereciever2,":",format(WRPoints(widereciever2),'.2f'))
        Points1 += WRPoints(widereciever2)
    except:
        print("WR2:",widereciever2,"-", "Not found")
    try:
        if flex_position.upper() == 'WR':
            print("Flex:",flex, "-", format(WRPoints(flex),'.2f'))
            Points1 += WRPoints(flex)
        elif flex_position.upper() == 'RB':
            print("Flex:",flex, "-", format(RBPoints(flex),'.2f'))
            Points1 += RBPoints(flex)
        elif flex_position.upper() == 'TE':
            print("Flex:",flex,"-", format(TEPoints(flex),'.2f'))
            Points1 += TEPoints(flex)
        else:
            print("Flex Position entered incorrectly")
    except:
        print("Flex:",flex, "-","Not found")
    try:
        print("TE:",tightend,"-",format(TEPoints(tightend),'.2f'))
        Points1 += TEPoints(tightend)
    except:
        print("TE:",tightend,"-", "Not found")
    try:
        print("DEF:",defense,"-",format(DEFPoints(defense),'.2f'))
        Points1 += DEFPoints(defense)
    except:
        print("DEF:",defense,"-", "Not found")
    try:
        print("K:",kicker,"-",format(KPoints(kicker),'.2f'))
        Points1 += KPoints(kicker)
    except:
        print("K:",kicker,"-", "Not found")
            
    print("Team 1 Points:",format(Points1,'.2f'))
    print()
    print("--------------")     #Below is the second team
    print("Team 2:")
    Points2 = 0     #Points need to be intialized
    #The 0 before variable indicates it's part of the second team
    try:
        print("QB:",Oquarterback,"-",format(QBPoints(Oquarterback),'.2f'))
        Points2 += QBPoints(Oquarterback)
    except:
        print("QB:",Oquarterback,"-", "Not found")
    try:
        print("RB1:",Orunningback1,"-", format(RBPoints(Orunningback1),'.2f'))
        Points2 += RBPoints(Orunningback1)
    except:
        print("RB1:",Orunningback1,"-", "Not found")
    try:
        print("RB2:",Orunningback2,"-", format(RBPoints(Orunningback2),'.2f'))
        Points2 += RBPoints(Orunningback2)
    except:
        print("RB2:",Orunningback2,"-", "Not found")
    try:
        print("WR1:",Owidereciever1,"-",format(WRPoints(Owidereciever1),'.2f'))
        Points2 += WRPoints(Owidereciever1)
    except:
        print("WR1:",Owidereciever1,"-", "Not found")
    try:
        print("WR2:",Owidereciever2,":",format(WRPoints(Owidereciever2),'.2f'))
        Points2 += WRPoints(Owidereciever2)
    except:
        print("WR2:",Owidereciever2,":", "Not found")
    try:
        if Oflex_position.upper() == 'WR':
            print("Flex:",Oflex, "-", format(WRPoints(Oflex),'.2f'))
            Points2 += WRPoints(Oflex)
        elif Oflex_position.upper() == 'RB':
            print("Flex:",Oflex, "-", format(RBPoints(Oflex),'.2f'))
            Points2 += RBPoints(Oflex)
        elif Oflex_position.upper() == 'TE':
            print("Flex:",Oflex,"-", format(TEPoints(Oflex),'.2f'))
            Points2 += TEPoints(Oflex)
        else:
            print("Position entered incorrectly")
    except:
        print("Flex:",Oflex, "-","Not found")
    try:
        print("TE:",Otightend,"-",format(TEPoints(Otightend),'.2f'))
        Points2 += TEPoints(Otightend)
    except:
        print("TE:",Otightend,"-", "Not found")
    try:
        print("DEF:",Odefense,"-",format(DEFPoints(Odefense),'.2f'))
        Points2 += DEFPoints(Odefense)
    except:
        print("DEF:",Odefense,"-", "Not found")
    try:
        print("K:",Okicker,"-",format(KPoints(Okicker),'.2f'))
        Points2 += KPoints(Okicker)
    except:
        print("K:",Okicker,"-", "Not found")
            
    print("Team 2 Points:",format(Points2,'.2f'))
    print('--------------')
    print("Final Score:","\n","Team 1 -",format(Points1,'.2f'),"\n","Team 2 -",format(Points2,'.2f'))

#These getWeek functions are used for opening the right file and used in the points functions
def getWeekQB(week):
    if week == 1:
        weeknum = "QB_Stats_wk1.csv"
    elif week == 2:
        weeknum = "QB_Stats_wk2.csv"
    elif week == 3:
        weeknum = "QB_Stats_wk3.csv"
    elif week == 4:
        weeknum = "QB_Stats_wk4.csv"
    elif week == 5:
        weeknum = "QB_Stats_wk5.csv"
    elif week == 6:
        weeknum = "QB_Stats_wk6.csv"
    elif week == 7:
        weeknum = "QB_Stats_wk7.csv"
    elif week == 8:
        weeknum = "QB_Stats_wk8.csv"
    elif week == 9:
        weeknum = "QB_Stats_wk9.csv"
    elif week == 10:
        weeknum = "QB_Stats_wk10.csv"
    elif week == 11:
        weeknum = "QB_Stats_wk11.csv"
    elif week == 12:
        weeknum = "QB_Stats_wk12.csv"
    elif week == 13:
        weeknum = "QB_Stats_wk13.csv"
    elif week == 14:
        weeknum = "QB_Stats_wk14.csv"
    elif week == 15:
        weeknum = "QB_Stats_wk15.csv"
    elif week == 16:
        weeknum = "QB_Stats_wk16.csv"
    elif week == 17:
        weeknum = "QB_Stats_wk17.csv"
    elif week == 0:
        weeknum = "QB_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum
def getWeekRB(week):
    if week == 1:
        weeknum = "RB_Stats_wk1.csv"
    elif week == 2:
        weeknum = "RB_Stats_wk2.csv"
    elif week == 3:
        weeknum = "RB_Stats_wk3.csv"
    elif week == 4:
        weeknum = "RB_Stats_wk4.csv"
    elif week == 5:
        weeknum = "RB_Stats_wk5.csv"
    elif week == 6:
        weeknum = "RB_Stats_wk6.csv"
    elif week == 7:
        weeknum = "RB_Stats_wk7.csv"
    elif week == 8:
        weeknum = "RB_Stats_wk8.csv"
    elif week == 9:
        weeknum = "RB_Stats_wk9.csv"
    elif week == 10:
        weeknum = "RB_Stats_wk10.csv"
    elif week == 11:
        weeknum = "RB_Stats_wk11.csv"
    elif week == 12:
        weeknum = "RB_Stats_wk12.csv"
    elif week == 13:
        weeknum = "RB_Stats_wk13.csv"
    elif week == 14:
        weeknum = "RB_Stats_wk14.csv"
    elif week == 15:
        weeknum = "RB_Stats_wk15.csv"
    elif week == 16:
        weeknum = "RB_Stats_wk16.csv"
    elif week == 17:
        weeknum = "RB_Stats_wk17.csv"
    elif week == 0:
        weeknum = "RB_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum
def getWeekWR(week):
    if week == 1:
        weeknum = "WR_Stats_wk1.csv"
    elif week == 2:
        weeknum = "WR_Stats_wk2.csv"
    elif week == 3:
        weeknum = "WR_Stats_wk3.csv"
    elif week == 4:
        weeknum = "WR_Stats_wk4.csv"
    elif week == 5:
        weeknum = "WR_Stats_wk5.csv"
    elif week == 6:
        weeknum = "WR_Stats_wk6.csv"
    elif week == 7:
        weeknum = "WR_Stats_wk7.csv"
    elif week == 8:
        weeknum = "WR_Stats_wk8.csv"
    elif week == 9:
        weeknum = "WR_Stats_wk9.csv"
    elif week == 10:
        weeknum = "WR_Stats_wk10.csv"
    elif week == 11:
        weeknum = "WR_Stats_wk11.csv"
    elif week == 12:
        weeknum = "WR_Stats_wk12.csv"
    elif week == 13:
        weeknum = "WR_Stats_wk13.csv"
    elif week == 14:
        weeknum = "WR_Stats_wk14.csv"
    elif week == 15:
        weeknum = "WR_Stats_wk15.csv"
    elif week == 16:
        weeknum = "WR_Stats_wk16.csv"
    elif week == 17:
        weeknum = "WR_Stats_wk17.csv"
    elif week == 0:
        weeknum = "WR_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum
def getWeekTE(week):
    if week == 1:
        weeknum = "TE_Stats_wk1.csv"
    elif week == 2:
        weeknum = "TE_Stats_wk2.csv"
    elif week == 3:
        weeknum = "TE_Stats_wk3.csv"
    elif week == 4:
        weeknum = "TE_Stats_wk4.csv"
    elif week == 5:
        weeknum = "TE_Stats_wk5.csv"
    elif week == 6:
        weeknum = "TE_Stats_wk6.csv"
    elif week == 7:
        weeknum = "TE_Stats_wk7.csv"
    elif week == 8:
        weeknum = "TE_Stats_wk8.csv"
    elif week == 9:
        weeknum = "TE_Stats_wk9.csv"
    elif week == 10:
        weeknum = "TE_Stats_wk10.csv"
    elif week == 11:
        weeknum = "TE_Stats_wk11.csv"
    elif week == 12:
        weeknum = "TE_Stats_wk12.csv"
    elif week == 13:
        weeknum = "TE_Stats_wk13.csv"
    elif week == 14:
        weeknum = "TE_Stats_wk14.csv"
    elif week == 15:
        weeknum = "TE_Stats_wk15.csv"
    elif week == 16:
        weeknum = "TE_Stats_wk16.csv"
    elif week == 17:
        weeknum = "TE_Stats_wk17.csv"
    elif week == 0:
        weeknum = "TE_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum
def getWeekDEF(week):
    if week == 1:
        weeknum = "DEF_Stats_wk1.csv"
    elif week == 2:
        weeknum = "DEF_Stats_wk2.csv"
    elif week == 3:
        weeknum = "DEF_Stats_wk3.csv"
    elif week == 4:
        weeknum = "DEF_Stats_wk4.csv"
    elif week == 5:
        weeknum = "DEF_Stats_wk5.csv"
    elif week == 6:
        weeknum = "DEF_Stats_wk6.csv"
    elif week == 7:
        weeknum = "DEF_Stats_wk7.csv"
    elif week == 8:
        weeknum = "DEF_Stats_wk8.csv"
    elif week == 9:
        weeknum = "DEF_Stats_wk9.csv"
    elif week == 10:
        weeknum = "DEF_Stats_wk10.csv"
    elif week == 11:
        weeknum = "DEF_Stats_wk11.csv"
    elif week == 12:
        weeknum = "DEF_Stats_wk12.csv"
    elif week == 13:
        weeknum = "DEF_Stats_wk13.csv"
    elif week == 14:
        weeknum = "DEF_Stats_wk14.csv"
    elif week == 15:
        weeknum = "DEF_Stats_wk15.csv"
    elif week == 16:
        weeknum = "DEF_Stats_wk16.csv"
    elif week == 17:
        weeknum = "DEF_Stats_wk17.csv"
    elif week == 0:
        weeknum = "DEF_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum
def getWeekK(week):
    if week == 1:
        weeknum = "K_Stats_wk1.csv"
    elif week == 2:
        weeknum = "K_Stats_wk2.csv"
    elif week == 3:
        weeknum = "K_Stats_wk3.csv"
    elif week == 4:
        weeknum = "K_Stats_wk4.csv"
    elif week == 5:
        weeknum = "K_Stats_wk5.csv"
    elif week == 6:
        weeknum = "K_Stats_wk6.csv"
    elif week == 7:
        weeknum = "K_Stats_wk7.csv"
    elif week == 8:
        weeknum = "K_Stats_wk8.csv"
    elif week == 9:
        weeknum = "K_Stats_wk9.csv"
    elif week == 10:
        weeknum = "K_Stats_wk10.csv"
    elif week == 11:
        weeknum = "K_Stats_wk11.csv"
    elif week == 12:
        weeknum = "K_Stats_wk12.csv"
    elif week == 13:
        weeknum = "K_Stats_wk13.csv"
    elif week == 14:
        weeknum = "K_Stats_wk14.csv"
    elif week == 15:
        weeknum = "K_Stats_wk15.csv"
    elif week == 16:
        weeknum = "K_Stats_wk16.csv"
    elif week == 17:
        weeknum = "K_Stats_wk17.csv"
    elif week == 0:
        weeknum = "K_Stats_tot.csv"
    else:
        weeknum = -1
    return weeknum

#These functions gather the data
def QBPoints(quarterback):
    with open(getWeekQB(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        for rank, row in enumerate(reader):
            players[row[0]] = {'rank':rank,'Yds':row[3], 'TD':row[4],'Int':row[5],'Yds.R':row[8],'2Pt.P':row[6],'TD.R':row[9],
            '2Pt.R':row[10],'Rec':row[11],'Yds.C':row[12],'TD.C':row[13],'2Pt.C':row[14],'FL':row[15],'TD.F':row[16]}
        

    qbRank = int(players[quarterback]['rank'])

    yards = float(players[quarterback]['Yds'])
    P4Y = yards / 25
    
    TD = int(players[quarterback]['TD'])
    TD4P = TD * 4
    
    Int = int(players[quarterback]['Int'])
    Int4P = Int * -2
    
    YdsR = float(players[quarterback]['Yds.R'])
    YdsR4P = YdsR * .1

    TwoPtP = int(players[quarterback]['2Pt.P'])
    TwoPtP4P = TwoPtP * 2

    TDR = int(players[quarterback]['TD.R'])
    TDR4P = TDR * 6
    
    TwoPtR = int(players[quarterback]['2Pt.R'])
    TwoPtR4P = TwoPtR * 2
    
    Rec = int(players[quarterback]['Rec'])
    Rec4P = Rec * 1
    
    YdsC = float(players[quarterback]['Yds.C'])
    YdsC4P = YdsC * .1

    TDC = int(players[quarterback]['TD.C'])
    TDC4P = TDC * 6

    TwoPtC = int(players[quarterback]['2Pt.C'])
    TwoPtC4P = TwoPtC * 2

    FL = int(players[quarterback]['FL'])
    FL4P = FL * -2

    TDF = int(players[quarterback]['TD.F'])
    TDF4P = TDF * 6
    
    Points = P4Y + TD4P + Int4P + YdsR4P + TwoPtP4P + TDR4P + TwoPtR4P + Rec4P + YdsC4P + TDC4P + TwoPtC4P + FL4P + TDF4P
    stats = [yards,TD,Int,YdsR,TDR,qbRank,Points]
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats   
def RBPoints(runningback):
    with open(getWeekRB(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        for rank,row in enumerate(reader):
            players[row[0]] = {'rank':rank,'Yds':row[3], 'TD':row[4],'Int':row[5],'Yds.R':row[8],'2Pt.P':row[6],'TD.R':row[9],
            '2Pt.R':row[10],'Rec':row[11],'Yds.C':row[12],'TD.C':row[13],'2Pt.C':row[14],'FL':row[15],'TD.F':row[16]}

    rbRank = int(players[runningback]['rank'])
    
    yards = float(players[runningback]['Yds'])
    P4Y = yards / 25
    
    TD = int(players[runningback]['TD'])
    TD4P = TD * 4
    
    Int = int(players[runningback]['Int'])
    Int4P = Int * -2
    
    YdsR = float(players[runningback]['Yds.R'])
    YdsR4P = YdsR * .1

    TwoPtP = int(players[runningback]['2Pt.P'])
    TwoPtP4P = TwoPtP * 2

    TDR = int(players[runningback]['TD.R'])
    TDR4P = TDR * 6
    
    TwoPtR = int(players[runningback]['2Pt.R'])
    TwoPtR4P = TwoPtR * 2
    
    Rec = int(players[runningback]['Rec'])
    Rec4P = Rec * 1
    
    YdsC = float(players[runningback]['Yds.C'])
    YdsC4P = YdsC * .1

    TDC = int(players[runningback]['TD.C'])
    TDC4P = TDC * 6

    TwoPtC = int(players[runningback]['2Pt.C'])
    TwoPtC4P = TwoPtC * 2

    FL = int(players[runningback]['FL'])
    FL4P = FL * -2

    TDF = int(players[runningback]['TD.F'])
    TDF4P = TDF * 6

    Points = P4Y + TD4P + Int4P + YdsR4P + TwoPtP4P + TDR4P + TwoPtR4P + Rec4P + YdsC4P + TDC4P + TwoPtC4P + FL4P + TDF4P
    stats = [YdsR,TDR,Rec,YdsC,TDC,rbRank,Points]
    
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats
def WRPoints(widereciever):
    with open(getWeekWR(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        for rank,row in enumerate(reader):
            players[row[0]] = {'rank':rank, 'Yds':row[3], 'TD':row[4],'Int':row[5],'Yds.R':row[8],'2Pt.P':row[6],'TD.R':row[9],
            '2Pt.R':row[10],'Rec':row[11],'Yds.C':row[12],'TD.C':row[13],'2Pt.C':row[14],'FL':row[15],'TD.F':row[16]}
       
    wrRank = int(players[widereciever]['rank'])
    
    yards = float(players[widereciever]['Yds'])
    P4Y = yards / 25
    
    TD = int(players[widereciever]['TD'])
    TD4P = TD * 4
    
    Int = int(players[widereciever]['Int'])
    Int4P = Int * -2
    
    YdsR = float(players[widereciever]['Yds.R'])
    YdsR4P = YdsR * .1

    TwoPtP = int(players[widereciever]['2Pt.P'])
    TwoPtP4P = TwoPtP * 2

    TDR = int(players[widereciever]['TD.R'])
    TDR4P = TDR * 6
    
    TwoPtR = int(players[widereciever]['2Pt.R'])
    TwoPtR4P = TwoPtR * 2
    
    Rec = int(players[widereciever]['Rec'])
    Rec4P = Rec * 1
    
    YdsC = float(players[widereciever]['Yds.C'])
    YdsC4P = YdsC * .1

    TDC = int(players[widereciever]['TD.C'])
    TDC4P = TDC * 6

    TwoPtC = int(players[widereciever]['2Pt.C'])
    TwoPtC4P = TwoPtC * 2

    FL = int(players[widereciever]['FL'])
    FL4P = FL * -2

    TDF = int(players[widereciever]['TD.F'])
    TDF4P = TDF * 6
    Points = P4Y + TD4P + Int4P + YdsR4P + TwoPtP4P + TDR4P + TwoPtR4P + Rec4P + YdsC4P + TDC4P + TwoPtC4P + FL4P + TDF4P
    stats = [Rec,YdsC,TDC,wrRank,Points]
    
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats
def TEPoints(tightend):
    with open(getWeekTE(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        for rank, row in enumerate(reader):
            players[row[0]] = {'rank':rank,'Yds':row[3], 'TD':row[4],'Int':row[5],'Yds.R':row[8],'2Pt.P':row[6],'TD.R':row[9],
            '2Pt.R':row[10],'Rec':row[11],'Yds.C':row[12],'TD.C':row[13],'2Pt.C':row[14],'FL':row[15],'TD.F':row[16]}

    teRank = int(players[tightend]['rank'])
    
    yards = float(players[tightend]['Yds'])
    P4Y = yards / 25
    
    TD = int(players[tightend]['TD'])
    TD4P = TD * 4
    
    Int = int(players[tightend]['Int'])
    Int4P = Int * -2
    
    YdsR = float(players[tightend]['Yds.R'])
    YdsR4P = YdsR * .1

    TwoPtP = int(players[tightend]['2Pt.P'])
    TwoPtP4P = TwoPtP * 2

    TDR = int(players[tightend]['TD.R'])
    TDR4P = TDR * 6
    
    TwoPtR = int(players[tightend]['2Pt.R'])
    TwoPtR4P = TwoPtR * 2
    
    Rec = int(players[tightend]['Rec'])
    Rec4P = Rec * 1
    
    YdsC = float(players[tightend]['Yds.C'])
    YdsC4P = YdsC * .1

    TDC = int(players[tightend]['TD.C'])
    TDC4P = TDC * 6

    TwoPtC = int(players[tightend]['2Pt.C'])
    TwoPtC4P = TwoPtC * 2

    FL = int(players[tightend]['FL'])
    FL4P = FL * -2

    TDF = int(players[tightend]['TD.F'])
    TDF4P = TDF * 6
    Points = P4Y + TD4P + Int4P + YdsR4P + TwoPtP4P + TDR4P + TwoPtR4P + Rec4P + YdsC4P + TDC4P + TwoPtC4P + FL4P + TDF4P
    stats = [Rec,YdsC,TDC,teRank,Points]
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats
def DEFPoints(defense):
    with open(getWeekDEF(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        for rank,row in enumerate(reader):
            players[row[0]] = {'rank':rank,'Sack':row[1], 'Int':row[2],'Saf':row[3],'FR':row[4],'Blk':row[5],'TD':row[6],
            'PA':row[7],'PassYds':row[8],'RushYds':row[9],'TotYds':row[10]}

    defRank = int(players[defense]['rank'])
    
    Sack = float(players[defense]['Sack'])
    Sack4P = Sack * 1
    
    Int = int(players[defense]['Int'])
    Int4P = Int * 2
    
    Saf = int(players[defense]['Saf'])
    Saf4P = Saf * 2

    FR = int(players[defense]['FR'])
    FR4P = FR * 2

    Blk = int(players[defense]['Blk'])
    Blk4P = Blk * 2

    TD = int(players[defense]['TD'])
    TD4P = TD * 6

    PA = int(players[defense]['PA'])
    PA4P = -100
    if PA == 0:                 #0
        PA4P = 5
    elif PA >= 1 and PA <= 6:   #1-6
        PA4P = 4
    elif PA >= 7 and PA <= 13:  #7-13
        PA4P = 3
    elif PA >= 14 and PA <= 17: #14-17
        PA4P = 1
    elif PA >= 18 and PA <= 27: #18-27
        PA4P = 0
    elif PA >= 28 and PA <= 34: #28-34
        PA4P = -1
    elif PA >= 35 and PA <= 45: #35-45
        PA4P = -3
    elif PA >= 46:              #46+
        PA4P = -5
    
    TotYds = float(players[defense]['TotYds'])
    TotYds4P = -100
    if TotYds < 100:
        TotYds4P = 5
    if TotYds >= 100 and TotYds < 200:  #100-199
        TotYds4P = 3
    if TotYds >= 200 and TotYds < 300:  #200-299
        TotYds4P = 2
    if TotYds >= 300 and TotYds < 350:  #300-349
        TotYds4P = 0
    if TotYds >= 350 and TotYds < 400:  #350-399
        TotYds4P = -1
    if TotYds >= 400 and TotYds < 450:  #400-449
        TotYds4P = -3
    if TotYds >= 450 and TotYds < 500:  #450-499
        TotYds4P = -5
    if TotYds >= 500 and TotYds < 550:  #500-549
        TotYds4P = -6
    if TotYds >= 550:                   #550+
        TotYds4P = -7

    Points = Sack4P + Int4P + Saf4P + FR4P + Blk4P + TD4P + PA4P + TotYds4P
    stats = [Sack, Int, Saf, FR, Blk, TD, PA, TotYds, defRank,Points]
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats
def KPoints(kicker):
    with open(getWeekK(week),'r',encoding = 'utf8') as f:
        reader = csv.reader(f)
        players = {}
        
        for rank,row in enumerate(reader):
            players[row[0]] = {'rank':rank,'FG':row[1], 'FGA':row[2],'FG1-19':row[5],'FG20-29':row[6],'FG30-39':row[7],'FG40-49':row[8],
            'FG50':row[9],'XPT':row[10]}
    
    kRank = int(players[kicker]['rank'])
    
    FG = int(players[kicker]['FG'])
        
    FGA = int(players[kicker]['FGA'])
    FGM = FGA - FG
    FGM4P = FGM * -1

    FG1_19 = int(players[kicker]['FG1-19'])
    FG1_194P = FG1_19 * 3

    FG20_29 = int(players[kicker]['FG20-29'])
    FG20_294P = FG20_29 * 3

    FG30_39 = int(players[kicker]['FG30-39'])
    FG30_394P = FG30_39 * 3

    FG40_49 = int(players[kicker]['FG40-49'])
    FG40_494P = FG40_49 * 4

    FG50 = int(players[kicker]['FG50'])
    FG504P = FG50 * 5

    XPT = int(players[kicker]['XPT'])
    XPT4P = XPT * 1

    Points = FGM4P + FG1_194P + FG20_294P + FG30_394P + FG40_494P + FG504P + XPT4P
    stats = [FGM,FG1_19,FG20_29,FG30_39,FG40_49,FG50,XPT,kRank,Points]
    if mode == 'st' or mode == 'myTeam' or mode == 'tvt':
        return Points
    if mode == 'inv':
        return stats
        

mode = input("Choose between individual player(inv), single team(st),  team vs team(tvt), or pre-set team(myTeam): ")
while mode != 'inv' and mode != 'st' and mode!= 'tvt' and mode!= 'myTeam':  #This is to make sure a valid mode is inputted
    print("Choose a valid mode. Enter what is in (): ")
    mode = input("Choose between individual player(inv), single team(st),  team vs team(tvt), or pre-set team(myTeam): ")

if mode == 'st':    #Single Team
    quarterback = input("Enter QB name: ")
    runningback1 = input("Enter RB name: ")
    runningback2 = input("Enter RB name: ")
    widereciever1 = input("Enter WR name: ")
    widereciever2 = input("Enter WR name: ")
    flex_position = input("What position is your flex? RB WR or TE? ")
    while flex_position.upper()  != 'WR' and flex_position.upper() != 'RB' and flex_position.upper() != 'TE':
        flex_position = input("enter flex position (RB,WR,TE): ") #Making sure valid position is inputted
    flex = input("Enter flex name: ")
    tightend = input("Enter TE name: ")
    defense = input("Enter Defense name: ")
    kicker = input("Enter Kicker name: ")
    singleTeam()  #Calls function on line 8
if mode == 'inv':   #This mode allows for user to input week 0 for total season stats (weeks 1-10)
    position = input("What position is this player? ")
    while position.upper() != 'QB' and position.upper() != 'RB' and position.upper() != 'WR' and position.upper() != 'TE' \
         and position.upper() != 'K' and position.upper() != 'DEF': #This is to make sure a valid mode is inputted
        position = input("What position is this player? ")
    if position.upper() == "QB":
        quarterback = input("Enter QB name: ")
    if position.upper() == 'RB':
        runningback = input("Enter RB name: ")
    if position.upper() == 'WR':
        widereciever = input("Enter WR name: ")
    if position.upper() == 'TE':
        tightend = input("Enter TE name: ")
    if position.upper() == 'DEF':
        defense = input("Enter defense name: ")
    if position.upper() == 'K':
        kicker = input("Enter kicker name: ")
    indivPlayer()  #Calles function on line 71       
if mode == 'myTeam':    #Pre set players
    Team= {
    'Week1': {'quarterback':'Carson Wentz','runningback1':'Saquon Barkley','runningback2':'Aaron Jones','widereciever1':'Cooper Kupp','widereciever2':'D.J. Chark'\
        ,'flex':'Clyde Edwards-Helaire','tightend':'Hayden Hurst','defense':'Baltimore Ravens','kicker':'Greg Zuerlein'},
    'Week2': {'quarterback':'Carson Wentz','runningback1':'Saquon Barkley','runningback2':'Aaron Jones','widereciever1':'Cooper Kupp','widereciever2':'D.J. Chark'\
        ,'flex':'Clyde Edwards-Helaire','tightend':'Hayden Hurst','defense':'Kansas City Chiefs','kicker':'Greg Zuerlein'},
    'Week3': {'quarterback':'Carson Wentz','runningback1':'Kenyan Drake','runningback2':'Aaron Jones','widereciever1':'Cooper Kupp','widereciever2':'Terry McLaurin'\
        ,'flex':'Clyde Edwards-Helaire','tightend':'Jonnu Smith','defense':'Tampa Bay Buccaneers','kicker':'Greg Zuerlein'},
    'Week4': {'quarterback':'Ryan Fitzpatrick','runningback1':'Kenyan Drake','runningback2':'Aaron Jones','widereciever1':'Cooper Kupp','widereciever2':'Terry McLaurin'\
        ,'flex':'Clyde Edwards-Helaire','tightend':'Hayden Hurst','defense':'Tampa Bay Buccaneers','kicker':'Greg Zuerlein'},    
    'Week5': {'quarterback':'Teddy Bridgewater','runningback1':'Clyde Edwards-Helaire','runningback2':'Josh Jacobs','widereciever1':'Terry McLaurin','widereciever2':'D.J. Chark'\
        ,'flex':'Jamison Crowder','tightend':'Dalton Schultz','defense':'Tampa Bay Buccaneers','kicker':'Rodrigo Blankenship'},     
    'Week6': {'quarterback':'Matthew Stafford','runningback1':'Clyde Edwards-Helaire','runningback2':'Aaron Jones','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Jamison Crowder','tightend':'Jonnu Smith','defense':'Baltimore Ravens','kicker':'Rodrigo Blankenship'},
    'Week7':{'quarterback':'Matthew Stafford','runningback1':'Clyde Edwards-Helaire','runningback2':'Josh Jacobs','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'D.J. Chark','tightend':'Jonnu Smith','defense':'Kansas City Chiefs','kicker':'Daniel Carlson'}, 
    'Week8':{'quarterback':'Ryan Tannehill','runningback1':'Clyde Edwards-Helaire','runningback2':'Josh Jacobs','widereciever1':'Brandon Aiyuk','widereciever2':'A.J. Brown'\
        ,'flex':'Jarvis Landry','tightend':'Jonnu Smith','defense':'Kansas City Chiefs','kicker':'Daniel Carlson'}, 
    'Week9':{'quarterback':'Justin Herbert','runningback1':'Josh Jacobs','runningback2':'Chase Edmonds','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Aaron Jones','tightend':'Jonnu Smith','defense':'Kansas City Chiefs','kicker':'Rodrigo Blankenship'},
    'Week10':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week11':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week12':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week13':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Cam Akers','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week14':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Irv Smith','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week15':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Miles Sanders','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week16':{'quarterback':'Justin Herbert','runningback1':'Miles Sanders','runningback2':'Aaron Jones','widereciever1':'D.J. Chark','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'},
    'Week17':{'quarterback':'Justin Herbert','runningback1':'Aaron Jones','runningback2':'Zack Moss','widereciever1':'Terry McLaurin','widereciever2':'A.J. Brown'\
        ,'flex':'Josh Jacobs','tightend':'Austin Hooper','defense':'New Orleans Saints','kicker':'Rodrigo Blankenship'}    
        }
    
    #F string uses the week to get correct key in dictionary lines 847-865
    quarterback = Team[F"Week{str(week)}"]['quarterback']
    runningback1 = Team[F"Week{str(week)}"]['runningback1']
    runningback2 = Team[F"Week{str(week)}"]['runningback2']
    widereciever1 = Team[F"Week{str(week)}"]['widereciever1']
    widereciever2 = Team[F"Week{str(week)}"]['widereciever2']
    flex = Team[F"Week{str(week)}"]['flex']
    print("What position is:",flex)
    flex_position = input()     #Flex can be RB WR or TE so the program has to know which file to use
    tightend = Team[F"Week{str(week)}"]['tightend']
    defense = Team[F"Week{str(week)}"]['defense']
    kicker = Team[F"Week{str(week)}"]['kicker']
    singleTeam()    #Calls function on line 8
if mode == 'tvt':   #Two team view
    quarterback = input("Enter QB name: ")
    runningback1 = input("Enter RB name: ")
    runningback2 = input("Enter RB name: ")
    widereciever1 = input("Enter WR name: ")
    widereciever2 = input("Enter WR name: ")
    flex_position = input("What position is your flex? RB WR or TE? ")
    while flex_position.upper()  != 'WR' and flex_position.upper() != 'RB' and flex_position.upper() != 'WR':
        flex_position = input("enter flex position (RB,WR,TE): ") #This is to make sure a valid mode is inputted
    flex = input("Enter flex name: ")
    tightend = input("Enter TE name: ")
    defense = input("Enter Defense name: ")
    kicker = input("Enter Kicker name: ")

    #The 0 indicates the variable is for the second team
    Oquarterback = input("Enter QB name: ")
    Orunningback1 = input("Enter RB name: ")
    Orunningback2 = input("Enter RB name: ")
    Owidereciever1 = input("Enter WR name: ")
    Owidereciever2 = input("Enter WR name: ")
    Oflex_position = input("What position is your flex? RB WR or TE? ")
    while Oflex_position.upper()  != 'WR' and Oflex_position.upper() != 'RB' and Oflex_position.upper() != 'WR':
        Oflex_position = input("enter flex position (RB,WR,TE): ") #This is to make sure a valid mode is inputted
    Oflex = input("Enter flex name: ")
    Otightend = input("Enter TE name: ")
    Odefense = input("Enter Defense name: ")
    Okicker = input("Enter Kicker name: ")
    teamvteam()     #Calls function on line 139





