import pandas as pd
import json

f = open("Prospects.json")
data = json.load(f)
df = pd.json_normalize(data)
QB = df.loc[df['position']=="QB"]
'''WR = df.loc[df['position']=="WR"]
RB = df.loc[df['position']=="RB"]
TE = df.loc[df['position']=="TE"]
OL = df.loc[df['position']=="" & df['position']=="" & df['position']=="" & df['position']==""]
EDGE = df.loc[df['position']=="EDGE"]
DT = df.loc[df['position']=="DT"]
LB = df.loc[df['position']=="LB"]
CB = df.loc[df['position']=="CB"]
Safty = df.loc[df['position']=="S"]'''

for index, row in QB.iterrows():

    print(row)
    seventeen  = pd.DataFrame(row["2017"])
    if seventeen.empty == False:
        try : 
            seventeen = seventeen.drop(seventeen[seventeen.category == "defensive"].index)
            completionPercentage = seventeen.loc[seventeen.stat_type == "PCT"].iloc[0]["stat"]
            TDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "passing")].iloc[0]["stat"]
            INTs = seventeen.loc[(seventeen.stat_type == "INT") & (seventeen.category == "passing")].iloc[0]["stat"]
            pYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "passing")].iloc[0]["stat"]
            pAttempts = seventeen.loc[(seventeen.stat_type == "ATT") & (seventeen.category == "passing")].iloc[0]["stat"]
            pYPA = seventeen.loc[(seventeen.stat_type == "YPA") & (seventeen.category == "passing")].iloc[0]["stat"]
            fumbles = seventeen.loc[(seventeen.stat_type == "FUM") & (seventeen.category == "fumbles")].iloc[0]["stat"]
            #TDtoINT = TDs/INTs
            print("2017",completionPercentage, TDs, INTs, pYards, pAttempts, pYPA, fumbles)
        except Exception as e:
            print(e)
    eightteen = pd.DataFrame(row["2018"])
    if eightteen.empty == False:
        try:
            eightteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            completionPercentage = eightteen.loc[eightteen.stat_type == "PCT"].iloc[0]["stat"]
            TDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "passing")].iloc[0]["stat"]
            INTs = eightteen.loc[(eightteen.stat_type == "INT") & (eightteen.category == "passing")].iloc[0]["stat"]
            pYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "passing")].iloc[0]["stat"]
            pAttempts = eightteen.loc[(eightteen.stat_type == "ATT") & (eightteen.category == "passing")].iloc[0]["stat"]
            pYPA = eightteen.loc[(eightteen.stat_type == "YPA") & (eightteen.category == "passing")].iloc[0]["stat"]
            fumbles = eightteen.loc[(eightteen.stat_type == "FUM") & (eightteen.category == "fumbles")].iloc[0]["stat"]
            #TDtoINT = TDs/INTs
            print("2018",completionPercentage, TDs, INTs, pYards, pAttempts, pYPA, fumbles)
        except Exception as e:
            print(e)

    nineteen = pd.DataFrame(row["2019"])
    if nineteen.empty == False:
        try:
            nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            completionPercentage = nineteen.loc[nineteen.stat_type == "PCT"].iloc[0]["stat"]
            TDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "passing")].iloc[0]["stat"]
            INTs = nineteen.loc[(nineteen.stat_type == "INT") & (nineteen.category == "passing")].iloc[0]["stat"]
            pYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "passing")].iloc[0]["stat"]
            pAttempts = nineteen.loc[(nineteen.stat_type == "ATT") & (nineteen.category == "passing")].iloc[0]["stat"]
            pYPA = nineteen.loc[(nineteen.stat_type == "YPA") & (nineteen.category == "passing")].iloc[0]["stat"]
            fumbles = nineteen.loc[(nineteen.stat_type == "FUM") & (nineteen.category == "fumbles")].iloc[0]["stat"]
            #TDtoINT = TDs/INTs
            print("2019",completionPercentage, TDs, INTs, pYards, pAttempts, pYPA, fumbles)
        except Exception as e:
            print(e)
    twenety = pd.DataFrame(row["2020"])
    if twenety.empty == False:
        try:
            twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            completionPercentage = twenety.loc[twenety.stat_type == "PCT"].iloc[0]["stat"]
            TDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "passing")].iloc[0]["stat"]
            INTs = twenety.loc[(twenety.stat_type == "INT") & (twenety.category == "passing")].iloc[0]["stat"]
            pYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "passing")].iloc[0]["stat"]
            pAttempts = twenety.loc[(twenety.stat_type == "ATT") & (twenety.category == "passing")].iloc[0]["stat"]
            pYPA = twenety.loc[(twenety.stat_type == "YPA") & (twenety.category == "passing")].iloc[0]["stat"]
            fumbles = twenety.loc[(twenety.stat_type == "FUM") & (twenety.category == "fumbles")].iloc[0]["stat"]
            #TDtoINT = TDs/INTs
            print("2020",completionPercentage, TDs, INTs, pYards, pAttempts, pYPA, fumbles)
        except Exception as e:
            print(e)
    twentyone = pd.DataFrame(row["2021"])
    if twentyone.empty == False:
        #print(twentyone)
        try:
            twentyone = twentyone.drop(twentyone[twentyone.category == "defensive"].index)
            completionPercentage = twentyone.loc[twentyone.stat_type == "PCT"].iloc[0]["stat"]
            TDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "passing")].iloc[0]["stat"]
            INTs = twentyone.loc[(twentyone.stat_type == "INT") & (twentyone.category == "passing")].iloc[0]["stat"]
            pYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "passing")].iloc[0]["stat"]
            pAttempts = twentyone.loc[(twentyone.stat_type == "ATT") & (twentyone.category == "passing")].iloc[0]["stat"]
            pYPA = twentyone.loc[(twentyone.stat_type == "YPA") & (twentyone.category == "passing")].iloc[0]["stat"]
            #fumbles = twentyone.loc[(twentyone.stat_type == "FUM") & (twentyone.category == "fumbles")].iloc[0]["stat"]
            #TDtoINT = TDs/INTs
            print("2021",completionPercentage, TDs, INTs, pYards, pAttempts, pYPA)
        except Exception as e:
            print(e)
                

    
    #exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")