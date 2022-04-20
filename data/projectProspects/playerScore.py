from turtle import position
import pandas as pd
import json

f = open("Prospects.json")
data = json.load(f)
df = pd.json_normalize(data)
QB = df.loc[df['position']=="QB"]
WR = df.loc[df['position']=="WR"]
RB = df.loc[df['position']=="RB"]
TE = df.loc[df['position']=="TE"]
OL = df.loc[df['position']=="" & df['position']=="" & df['position']=="" & df['position']==""]
EDGE = df.loc[df['position']=="EDGE"]
DT = df.loc[df['position']=="DT"]
LB = df.loc[df['position']=="LB"]
CB = df.loc[df['position']=="CB"]
S = df.loc[df['position']=="S"]

for index, row in QB.iterrows():

    print(row)
    seventeen  = pd.DataFrame(row["2017"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[seventeen.category == "defensive"].index)
        completionPercentage = 
        TDtoINT = 
        passingYards = 
        fumbles = 
    eightteen = pd.DataFrame(row["2018"])
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
        completionPercentage = 
        TDtoINT = 
        passingYards = 
        fumbles = 
    nineteen = pd.DataFrame(row["2019"])
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
        completionPercentage = 
        TDtoINT = 
        passingYards = 
        fumbles = 
    twenety = pd.DataFrame(row["2020"])
    if twenety.empty == False:
        twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
        completionPercentage = 
        TDtoINT = 
        passingYards = 
        fumbles = 
    twentyone = pd.DataFrame(row["2021"])
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[twentyone.category == "defensive"].index)
        completionPercentage = 
        TDtoINT = 
        passingYards = 
        fumbles = 

    print(twentyone)
    #exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")