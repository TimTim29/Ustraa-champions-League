import pandas as pd
from random import randrange

def generateGroup()-> dict:

    teamList = [("Rhino Hurricanes", 'UP', 'F', 2),
    ('Midnight Stars', 'J&K', 'F', 8),
    ('Rocky Assassins', 'Delhi', 'F', 0),
    ('Striking Sharpshooters', 'Delhi', 'T', 0),
    ('Skull Fireballs', 'Goa', 'F', 9),
    ('Blue Bombers', 'Haryana','T', 1),
    ('Blue Geckos', 'MP', 'T', 5),
    ('Midnight Miners', 'UP', 'T', 2),
    ('Spirit Blockers', 'AP', 'F', 4),
    ('Wind Kamikaze Pilots', 'Kerala', 'F', 10),
    ('Retro Chuckers', 'UK', 'F', 3),
    ('Venomous Cyborgs', 'West Bengal', 'F', 11),
    ('Quicksilver Ninjas', 'Sikkim', 'F', 12),
    ('Alpha Blockers', 'Rajasthan', 'T', 7),
    (' Retro Heroes', 'Haryana', 'F', 1),
    ('Lions', 'Punjab', 'F', 6),
    ('Raging Spanners', 'HP', 'F', 13),
    ('Poison Spiders', 'Odisha', 'F', 14),
    ('Black Bullets', 'UP', 'F', 2),
    ('Thunder Commandos', 'UP', 'F', 2),
    ('Venomous Sharks', 'Haryana', 'F', 1),
    ('Killer Stars', 'Nagaland', 'F', 15),
    ('Tornado Geckos', 'Punjab', 'T', 6),
    ('Knockout Busters', 'MP', 'F',5),
    ('Muffin Racers', 'Maharastra', 'T', 16),
    ('Real Madrid', 'Delhi', 'F', 0),
    ('Demolition Piledrivers', 'Rajasthan', 'F', 7),
    ('Flying Xpress', 'Delhi', 'F', 0),
    ('Silver Wasps', 'UK', 'F',3),
    ('The Showstoppers', 'Delhi', 'F', 0),
    ('Wolfsburg', 'Haryana', 'F', 1),
    ('Black & White Gangstaz', 'AP', 'T', 4)]

    teamDf = pd.DataFrame(teamList, columns = ['Club', 'State', 'isPrevQualifier', 'occurance'])
    groupA = {'groupName': 'GROUP A', 'teams': [], 'states':[]}
    groupB = {'groupName': 'GROUP B', 'teams': [], 'states':[]}
    groupC = {'groupName': 'GROUP C', 'teams': [], 'states':[]}
    groupD = {'groupName': 'GROUP D', 'teams': [], 'states':[]}
    groupE = {'groupName': 'GROUP E', 'teams': [], 'states':[]}
    groupF = {'groupName': 'GROUP F', 'teams': [], 'states':[]}
    groupG = {'groupName': 'GROUP G', 'teams': [], 'states':[]}
    groupH = {'groupName': 'GROUP H', 'teams': [], 'states':[]}

    # generating random integer 
    irand1 = randrange(0, 8)
    iterVar1 = irand1
    prevQualDf = teamDf[teamDf['isPrevQualifier'] == 'T']
    prevQualDf.reset_index(drop=True, inplace= True)
    
    groups = [groupA, groupB, groupC, groupD, groupE, groupF, groupG, groupH ]
    indGroups1 =0

    # assigning previous year qualifiers to groups
    while True:
        tempDict ={'team': prevQualDf['Club'][iterVar1], 'state':prevQualDf['State'][iterVar1]}
        groups[indGroups1]['teams'].append(tempDict)
        groups[indGroups1]['states'].append(prevQualDf['State'][iterVar1])
        iterVar1 = (iterVar1+1) % 8
        indGroups1 = indGroups1 + 1
        if iterVar1 == irand1:
            break

    # generating dataframe of list of remaining previous year non qualifiers
    nonQualDf = teamDf[teamDf['isPrevQualifier'] == 'F']
    nonQualDf.reset_index(drop=True, inplace= True)
    nonQualDf.sort_values(['occurance','State'], inplace=True,ignore_index=True)
    
    irand2 = randrange(0,1)
    
    iterVar2 = irand2
    indGroups2 = 0

    # pushing remaining 24 teams to groups
    while True:
        while True:
            if (nonQualDf['State'][iterVar2] in groups[indGroups2]['states']) or (len(groups[indGroups2]['teams'])>=4) :
                indGroups2 = (indGroups2 + 1) % 8
            else :
                tempDict ={'team': nonQualDf['Club'][iterVar2], 'state':nonQualDf['State'][iterVar2]}
                groups[indGroups2]['teams'].append(tempDict)
                groups[indGroups2]['states'].append(nonQualDf['State'][iterVar2])
                indGroups2 = (indGroups2 + 1) % 8
                break
            # print(f"group index = {indGroups2}")
        iterVar2 = (iterVar2+1) % 24
        # # print(f"df index ={iterVar2}")
        if iterVar2 == irand2:
            break

    return {'groupA': groupA, 'groupB':groupB, 'groupC': groupC, 'groupD': groupD, 'groupE': groupE, 'groupF': groupF, 'groupG':groupG,'groupH':groupH}
    
