import pandas as pd
import json

f = open("Prospects.json")
data = json.load(f)
df = pd.json_normalize(data)
QB = df.loc[df['position']=="QB"]
#QB = QB.drop(QB[QB.category != "passing"].index)
print(QB)
WR = df.loc[df['position']=="WR"]
RB = df.loc[df['position']=="RB"]
TE = df.loc[df['position']=="TE"]
#OL = df.loc[df['position']=="" & df['position']=="" & df['position']=="" & df['position']==""]
EDGE = df.loc[df['position']=="EDGE"]
DT = df.loc[df['position']=="DT"]
LB = df.loc[df['position']=="LB"]
CB = df.loc[df['position']=="CB"]
S = df.loc[df['position']=="S"]

for index, row in QB.iterrows():
    Tscore = {}
    print(row)
    seventeen  = pd.DataFrame(row["2017"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "passing") & (seventeen.category !="fumbles") ].index)
    eightteen = pd.DataFrame(row["2018"])
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "passing") & (eightteen.category !="fumbles")].index)
    nineteen = pd.DataFrame(row["2019"])
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "passing") & (nineteen.category !="fumbles")].index)
    twenety = pd.DataFrame(row["2020"])
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "passing") & (twenety.category !="fumbles")].index)
    twentyone = pd.DataFrame(row["2021"])
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "passing") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    if seventeen.empty == False:
        try : 
            #seventeen = seventeen.drop(seventeen[seventeen.category == "defensive"].index)
            try: completionPercentage = seventeen.loc[seventeen.stat_type == "PCT"].iloc[0]["stat"]
            except: completionPercentage = 0
            try: TDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "passing")].iloc[0]["stat"]
            except: TDs = 0
            try: INTs = seventeen.loc[(seventeen.stat_type == "INT") & (seventeen.category == "passing")].iloc[0]["stat"]
            except:INTs=0
            try: pYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "passing")].iloc[0]["stat"]
            except: pYards=0
            try: pAttempts = seventeen.loc[(seventeen.stat_type == "ATT") & (seventeen.category == "passing")].iloc[0]["stat"]
            except: pAttempts=0
            try: pYPA = seventeen.loc[(seventeen.stat_type == "YPA") & (seventeen.category == "passing")].iloc[0]["stat"]
            except: pYPA = 0
            try: fumbles = seventeen.loc[(seventeen.stat_type == "FUM") & (seventeen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            score = (completionPercentage*(20))+((TDs/25)*20)+((pYards/2800)*20)+((pYPA/8)*15)+(((1/((fumbles+.000001)/(pAttempts+.000001)))/100)*10)+(((1/((INTs+.000001)/(pAttempts+.00001)))/100)*15)

            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #eightteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: completionPercentage = eightteen.loc[eightteen.stat_type == "PCT"].iloc[0]["stat"]
            except: completionPercentage = 0
            try: TDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "passing")].iloc[0]["stat"]
            except: TDs = 0
            try: INTs = eightteen.loc[(eightteen.stat_type == "INT") & (eightteen.category == "passing")].iloc[0]["stat"]
            except:INTs=0
            try: pYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "passing")].iloc[0]["stat"]
            except: pYards=0
            try: pAttempts = eightteen.loc[(eightteen.stat_type == "ATT") & (eightteen.category == "passing")].iloc[0]["stat"]
            except: pAttempts=0
            try: pYPA = eightteen.loc[(eightteen.stat_type == "YPA") & (eightteen.category == "passing")].iloc[0]["stat"]
            except: pYPA = 0
            try: fumbles = eightteen.loc[(eightteen.stat_type == "FUM") & (eightteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            score = (completionPercentage*(20))+((TDs/25)*20)+((pYards/2800)*20)+((pYPA/8)*15)+(((1/((fumbles+.000001)/(pAttempts+.000001)))/100)*10)+(((1/((INTs+.000001)/(pAttempts+.00001)))/100)*15)


            #TDtoINT = TDs/INTs
            print("2018",score)
            if score > 100:
                score = 100
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: completionPercentage = nineteen.loc[nineteen.stat_type == "PCT"].iloc[0]["stat"]
            except: completionPercentage = 0
            try: TDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "passing")].iloc[0]["stat"]
            except: TDs = 0
            try: INTs = nineteen.loc[(nineteen.stat_type == "INT") & (nineteen.category == "passing")].iloc[0]["stat"]
            except:INTs=0
            try: pYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "passing")].iloc[0]["stat"]
            except: pYards=0
            try: pAttempts = nineteen.loc[(nineteen.stat_type == "ATT") & (nineteen.category == "passing")].iloc[0]["stat"]
            except: pAttempts=0
            try: pYPA = nineteen.loc[(nineteen.stat_type == "YPA") & (nineteen.category == "passing")].iloc[0]["stat"]
            except: pYPA = 0
            try: fumbles = nineteen.loc[(nineteen.stat_type == "FUM") & (nineteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=1
            score = (completionPercentage*(20))+((TDs/25)*20)+((pYards/2800)*20)+((pYPA/8)*15)+(((1/((fumbles+.000001)/(pAttempts+.000001)))/100)*10)+(((1/((INTs+.000001)/(pAttempts+.00001)))/100)*15)

            #TDtoINT = TDs/INTs
            print("2019",score)
            if score > 100:
                score = 100
            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: completionPercentage = twenety.loc[twenety.stat_type == "PCT"].iloc[0]["stat"]
            except: completionPercentage = 0
            try: TDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "passing")].iloc[0]["stat"]
            except: TDs = 0
            try: INTs = twenety.loc[(twenety.stat_type == "INT") & (twenety.category == "passing")].iloc[0]["stat"]
            except:INTs=0
            try: pYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "passing")].iloc[0]["stat"]
            except: pYards=0
            try: pAttempts = twenety.loc[(twenety.stat_type == "ATT") & (twenety.category == "passing")].iloc[0]["stat"]
            except: pAttempts=0
            try: pYPA = twenety.loc[(twenety.stat_type == "YPA") & (twenety.category == "passing")].iloc[0]["stat"]
            except: pYPA = 0
            try: fumbles = twenety.loc[(twenety.stat_type == "FUM") & (twenety.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            score = (completionPercentage*(20))+((TDs/25)*20)+((pYards/2800)*20)+((pYPA/8)*15)+(((1/((fumbles+.000001)/(pAttempts+.000001)))/100)*10)+(((1/((INTs+.000001)/(pAttempts+.00001)))/100)*15)

            #TDtoINT = TDs/INTs
            print("2020",score)
            if score > 100:
                score = 100
            Tscore["2020"] =((score/100))
        except Exception as e:
            Tscore["2020"] =(0)
            print(e)
    else:
        Tscore["2020"] =(0)
    if twentyone.empty == False:
        #print(twentyone)
        try:
            #twentyone = twentyone.drop(twentyone[twentyone.category == "defensive"].index)
            try: completionPercentage = twentyone.loc[twentyone.stat_type == "PCT"].iloc[0]["stat"]
            except: completionPercentage = 0
            try: TDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "passing")].iloc[0]["stat"]
            except: TDs = 0
            try: INTs = twentyone.loc[(twentyone.stat_type == "INT") & (twentyone.category == "passing")].iloc[0]["stat"]
            except:INTs=0
            try: pYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "passing")].iloc[0]["stat"]
            except: pYards=0
            try: pAttempts = twentyone.loc[(twentyone.stat_type == "ATT") & (twentyone.category == "passing")].iloc[0]["stat"]
            except: pAttempts=0
            try: pYPA = twentyone.loc[(twentyone.stat_type == "YPA") & (twentyone.category == "passing")].iloc[0]["stat"]
            except: pYPA = 0
            try: fumbles = twentyone.loc[(twentyone.stat_type == "FUM") & (twentyone.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            #score = (completionPercentage*(30))+((TDs/25)*15)+((pYards/2800)*15)+((pYPA/8)*10)+(((1/(fumbles/pAttempts))/100)*10)+(((1/(INTs/pAttempts))/100)*20)
            score = (completionPercentage*(20))+((TDs/25)*20)+((pYards/2800)*20)+((pYPA/8)*15)+(((1/((fumbles+.000001)/(pAttempts+.000001)))/100)*10)+(((1/((INTs+.000001)/(pAttempts+.00001)))/100)*15)

            #TDtoINT = TDs/INTs
            print("2021",score)
            if score > 100:
                score = 100

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)

    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    if exp < 2:
        s = sum(Tscore.values())/2
    else: 
        s = sum(Tscore.values())/(exp-.5)
    print(Tscore, s)        

    
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")