import pandas as pd
import json
import numpy as np
import sqlite3

f = open("Prospects.json")
data = json.load(f)
df = pd.json_normalize(data)
QB = df.loc[df['position']=="QB"]
#QB = QB.drop(QB[QB.category != "passing"].index)
WR = df.loc[df['position']=="WR"]
RB = df.loc[df['position']=="RB"]
TE = df.loc[df['position']=="TE"]
OL = df.loc[(df['position']=="OT") | (df['position']=="IOL")]
EDGE = df.loc[df['position']=="EDGE"]
DT = df.loc[df['position']=="DL"]
LB = df.loc[df['position']=="LB"]
CB = df.loc[df['position']=="CB"]
S = df.loc[df['position']=="S"]
P = df.loc[df['position']=="P"]
K = df.loc[df['position']=="K"]

pros = {}
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
    pros[row['id']] = s
   
for index, row in RB.iterrows():
    Tscore = {}
    print(row)
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "rushing") & (seventeen.category !="receiving") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "rushing") & (eightteen.category !="receiving")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "rushing") & (nineteen.category !="receiving")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "rushing") & (twenety.category !="receiving")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "rushing") & (twentyone.category !="receiving") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    #print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: rushingTDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "rushing")].iloc[0]["stat"]
            except: rushingTDs = 0
            try: receivingTDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: rushingYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "rushing")].iloc[0]["stat"]
            except: rushingYards=0
            try: carries = seventeen.loc[(seventeen.stat_type == "CAR") & (seventeen.category == "rushing")].iloc[0]["stat"]
            except: carries=0
            try: receivingYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = seventeen.loc[(seventeen.stat_type == "REC") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = seventeen.loc[(seventeen.stat_type == "FUM") & (seventeen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= rushingYards/carries
            except: ypc = 0
            score = ((ypc/4.5)*(30))+((rushingYards/1000)*15)+((rushingTDs/10)*20)+((receivingYards/200)*15)+((receivingTDs/3)*10)+(((1/((fumbles+.000001)/(carries+receptions)))/100)*10)

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
            try: rushingTDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "rushing")].iloc[0]["stat"]
            except: rushingTDs = 0
            try: receivingTDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: rushingYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "rushing")].iloc[0]["stat"]
            except: rushingYards=0
            try: carries = eightteen.loc[(eightteen.stat_type == "CAR") & (eightteen.category == "rushing")].iloc[0]["stat"]
            except: carries=0
            try: receivingYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = eightteen.loc[(eightteen.stat_type == "REC") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = eightteen.loc[(eightteen.stat_type == "FUM") & (eightteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= rushingYards/carries
            except: ypc = 0
            score = ((ypc/4.5)*(30))+((rushingYards/1000)*15)+((rushingTDs/10)*20)+((receivingYards/200)*15)+((receivingTDs/3)*10)+(((1/((fumbles+.000001)/(carries+receptions)))/100)*10)

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
            try: rushingTDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "rushing")].iloc[0]["stat"]
            except: rushingTDs = 0
            try: receivingTDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: rushingYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "rushing")].iloc[0]["stat"]
            except: rushingYards=0
            try: carries = nineteen.loc[(nineteen.stat_type == "CAR") & (nineteen.category == "rushing")].iloc[0]["stat"]
            except: carries=0
            try: receivingYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = nineteen.loc[(nineteen.stat_type == "REC") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = nineteen.loc[(nineteen.stat_type == "FUM") & (nineteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= rushingYards/carries
            except: ypc = 0
            score = ((ypc/4.5)*(30))+((rushingYards/1000)*15)+((rushingTDs/10)*20)+((receivingYards/200)*15)+((receivingTDs/3)*10)+(((1/((fumbles+.000001)/(carries+receptions)))/100)*10)
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
            try: rushingTDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "rushing")].iloc[0]["stat"]
            except: rushingTDs = 0
            try: receivingTDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: rushingYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "rushing")].iloc[0]["stat"]
            except: rushingYards=0
            try: carries = twenety.loc[(twenety.stat_type == "CAR") & (twenety.category == "rushing")].iloc[0]["stat"]
            except: carries=0
            try: receivingYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twenety.loc[(twenety.stat_type == "REC") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twenety.loc[(twenety.stat_type == "FUM") & (twenety.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= rushingYards/carries
            except: ypc = 0
            score = ((ypc/4.5)*(30))+((rushingYards/1000)*15)+((rushingTDs/10)*20)+((receivingYards/200)*15)+((receivingTDs/3)*10)+(((1/((fumbles+.000001)/(carries+receptions)))/100)*10)

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
            try: rushingTDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "rushing")].iloc[0]["stat"]
            except: rushingTDs = 0
            try: receivingTDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: rushingYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "rushing")].iloc[0]["stat"]
            except: rushingYards=0
            try: carries = twentyone.loc[(twentyone.stat_type == "CAR") & (twentyone.category == "rushing")].iloc[0]["stat"]
            except: carries=0
            try: receivingYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twentyone.loc[(twentyone.stat_type == "REC") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twentyone.loc[(twentyone.stat_type == "FUM") & (twentyone.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= rushingYards/carries
            except: ypc = 0
            score = ((ypc/4.5)*(30))+((rushingYards/1000)*15)+((rushingTDs/10)*20)+((receivingYards/200)*15)+((receivingTDs/3)*10)+(((1/((fumbles+.000001)/(carries+receptions)))/100)*10)
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
    s = sum(Tscore.values())/exp
    print(Tscore, s)
    pros[row['id']] = s

for index, row in WR.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "rushing") & (seventeen.category !="receiving") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "rushing") & (eightteen.category !="receiving")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "rushing") & (nineteen.category !="receiving")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "rushing") & (twenety.category !="receiving")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "rushing") & (twentyone.category !="receiving") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    #print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: receivingTDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = seventeen.loc[(seventeen.stat_type == "REC") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = seventeen.loc[(seventeen.stat_type == "FUM") & (seventeen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/70)*15)+((receivingYards/1000)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = eightteen.loc[(eightteen.stat_type == "REC") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = eightteen.loc[(eightteen.stat_type == "FUM") & (eightteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/70)*15)+((receivingYards/1000)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = nineteen.loc[(nineteen.stat_type == "REC") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = nineteen.loc[(nineteen.stat_type == "FUM") & (nineteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/70)*15)+((receivingYards/1000)*40)+((receivingTDs/12)*25)
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
            try: receivingTDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twenety.loc[(twenety.stat_type == "REC") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twenety.loc[(twenety.stat_type == "FUM") & (twenety.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/70)*15)+((receivingYards/1000)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twentyone.loc[(twentyone.stat_type == "REC") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twentyone.loc[(twentyone.stat_type == "FUM") & (twentyone.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/70)*15)+((receivingYards/1000)*40)+((receivingTDs/12)*25)
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
    s = sum(Tscore.values())/(exp-.5)
    print(row['name'],Tscore, s)
    pros[row['id']] = s
    
for index, row in TE.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "rushing") & (seventeen.category !="receiving") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "rushing") & (eightteen.category !="receiving")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "rushing") & (nineteen.category !="receiving")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "rushing") & (twenety.category !="receiving")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "rushing") & (twentyone.category !="receiving") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    #print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: receivingTDs = seventeen.loc[(seventeen.stat_type == "TD") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = seventeen.loc[(seventeen.stat_type == "REC") & (seventeen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = seventeen.loc[(seventeen.stat_type == "FUM") & (seventeen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/40)*15)+((receivingYards/400)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = eightteen.loc[(eightteen.stat_type == "TD") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = eightteen.loc[(eightteen.stat_type == "REC") & (eightteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = eightteen.loc[(eightteen.stat_type == "FUM") & (eightteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/50)*15)+((receivingYards/500)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = nineteen.loc[(nineteen.stat_type == "TD") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = nineteen.loc[(nineteen.stat_type == "REC") & (nineteen.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = nineteen.loc[(nineteen.stat_type == "FUM") & (nineteen.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/50)*15)+((receivingYards/500)*40)+((receivingTDs/12)*25)
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
            try: receivingTDs = twenety.loc[(twenety.stat_type == "TD") & (twenety.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twenety.loc[(twenety.stat_type == "REC") & (twenety.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twenety.loc[(twenety.stat_type == "FUM") & (twenety.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/50)*15)+((receivingYards/500)*40)+((receivingTDs/12)*25)

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
            try: receivingTDs = twentyone.loc[(twentyone.stat_type == "TD") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except:receivingTDs=0
            try: receivingYards = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receivingYards = 0
            try: receptions = twentyone.loc[(twentyone.stat_type == "REC") & (twentyone.category == "receiving")].iloc[0]["stat"]
            except: receptions = 0
            try: fumbles = twentyone.loc[(twentyone.stat_type == "FUM") & (twentyone.category == "fumbles")].iloc[0]["stat"]
            except: fumbles=0
            
            try: ypc= receivingYards/receptions
            except: ypc = 0
            score = ((ypc/15)*(20))+((receptions/50)*15)+((receivingYards/500)*40)+((receivingTDs/12)*25)
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
    s = sum(Tscore.values())/(exp-.5)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in EDGE.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "defensive") & (seventeen.category !="interceptions") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "defensive") & (eightteen.category !="interceptions")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "defensive") & (nineteen.category !="interceptions")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "defensive") & (twenety.category !="interceptions")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "defensive") & (twentyone.category !="interceptions") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    #print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    print(twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: sacks = seventeen.loc[(seventeen.stat_type == "SACKS") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = seventeen.loc[(seventeen.stat_type == "TFL") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = seventeen.loc[(seventeen.stat_type == "QB HUR") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = seventeen.loc[(seventeen.stat_type == "SOLO") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = seventeen.loc[(seventeen.stat_type == "TOT") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/12)*(35))+((tacklesForLoss/13)*20)+((hurry/10)*20)+((soloTackles/30)*15)+((tTackles/50)*10)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: sacks = nineteen.loc[(nineteen.stat_type == "SACKS") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = nineteen.loc[(nineteen.stat_type == "QB HUR") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/12)*(35))+((tacklesForLoss/13)*20)+((hurry/10)*20)+((soloTackles/30)*15)+((tTackles/50)*10)

            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: sacks = nineteen.loc[(nineteen.stat_type == "SACKS") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = nineteen.loc[(nineteen.stat_type == "QB HUR") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/12)*(35))+((tacklesForLoss/13)*20)+((hurry/10)*20)+((soloTackles/30)*15)+((tTackles/50)*10)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: sacks = twenety.loc[(twenety.stat_type == "SACKS") & (twenety.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twenety.loc[(twenety.stat_type == "TFL") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = twenety.loc[(twenety.stat_type == "QB HUR") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = twenety.loc[(twenety.stat_type == "SOLO") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twenety.loc[(twenety.stat_type == "TOT") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/12)*(35))+((tacklesForLoss/13)*20)+((hurry/10)*20)+((soloTackles/30)*15)+((tTackles/50)*10)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: sacks = twentyone.loc[(twentyone.stat_type == "SACKS") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twentyone.loc[(twentyone.stat_type == "TFL") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = twentyone.loc[(twentyone.stat_type == "QB HUR") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = twentyone.loc[(twentyone.stat_type == "SOLO") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twentyone.loc[(twentyone.stat_type == "TOT") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/12)*(35))+((tacklesForLoss/13)*20)+((hurry/10)*20)+((soloTackles/30)*15)+((tTackles/50)*10)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)

    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp-.7)
    print(row['name'],Tscore, s)
    pros[row['id']] = s
    
for index, row in DT.iterrows():

    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "defensive") & (seventeen.category !="interceptions") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "defensive") & (eightteen.category !="interceptions")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "defensive") & (nineteen.category !="interceptions")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "defensive") & (twenety.category !="interceptions")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "defensive") & (twentyone.category !="interceptions") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    print(twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: sacks = seventeen.loc[(seventeen.stat_type == "SACKS") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = seventeen.loc[(seventeen.stat_type == "TFL") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = seventeen.loc[(seventeen.stat_type == "QB HUR") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = seventeen.loc[(seventeen.stat_type == "SOLO") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = seventeen.loc[(seventeen.stat_type == "TOT") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(20))+((tacklesForLoss/10)*30)+((hurry/2)*15)+((soloTackles/20)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: sacks = nineteen.loc[(nineteen.stat_type == "SACKS") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = nineteen.loc[(nineteen.stat_type == "QB HUR") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(20))+((tacklesForLoss/10)*30)+((hurry/2)*15)+((soloTackles/20)*15)+((tTackles/40)*20)
            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: sacks = nineteen.loc[(nineteen.stat_type == "SACKS") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = nineteen.loc[(nineteen.stat_type == "QB HUR") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(20))+((tacklesForLoss/10)*30)+((hurry/2)*15)+((soloTackles/20)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: sacks = twenety.loc[(twenety.stat_type == "SACKS") & (twenety.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twenety.loc[(twenety.stat_type == "TFL") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = twenety.loc[(twenety.stat_type == "QB HUR") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = twenety.loc[(twenety.stat_type == "SOLO") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twenety.loc[(twenety.stat_type == "TOT") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(20))+((tacklesForLoss/10)*30)+((hurry/2)*15)+((soloTackles/20)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: sacks = twentyone.loc[(twentyone.stat_type == "SACKS") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twentyone.loc[(twentyone.stat_type == "TFL") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: hurry = twentyone.loc[(twentyone.stat_type == "QB HUR") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: hurry = 0
            try: soloTackles = twentyone.loc[(twentyone.stat_type == "SOLO") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twentyone.loc[(twentyone.stat_type == "TOT") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(20))+((tacklesForLoss/10)*30)+((hurry/2)*15)+((soloTackles/20)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp-.7)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in LB.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "defensive") & (seventeen.category !="interceptions") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "defensive") & (eightteen.category !="interceptions")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "defensive") & (nineteen.category !="interceptions")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "defensive") & (twenety.category !="interceptions")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "defensive") & (twentyone.category !="interceptions") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    print(seventeen,"\n", eightteen, "\n",nineteen,"\n", twenety, "\n",twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: sacks = seventeen.loc[(seventeen.stat_type == "SACKS") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = seventeen.loc[(seventeen.stat_type == "TFL") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = seventeen.loc[(seventeen.stat_type == "PD") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = seventeen.loc[(seventeen.stat_type == "SOLO") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = seventeen.loc[(seventeen.stat_type == "TOT") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(10))+((tacklesForLoss/10)*10)+((passDefended/3)*15)+((soloTackles/20)*35)+((tTackles/40)*30)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: sacks = eightteen.loc[(eightteen.stat_type == "SACKS") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = eightteen.loc[(eightteen.stat_type == "TFL") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = eightteen.loc[(eightteen.stat_type == "PD") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = eightteen.loc[(eightteen.stat_type == "SOLO") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = eightteen.loc[(eightteen.stat_type == "TOT") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(10))+((tacklesForLoss/10)*10)+((passDefended/3)*15)+((soloTackles/20)*35)+((tTackles/40)*30)
            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: sacks = nineteen.loc[(nineteen.stat_type == "SACKS") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = nineteen.loc[(nineteen.stat_type == "PD") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(10))+((tacklesForLoss/10)*10)+((passDefended/3)*15)+((soloTackles/20)*35)+((tTackles/40)*30)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: sacks = twenety.loc[(twenety.stat_type == "SACKS") & (twenety.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twenety.loc[(twenety.stat_type == "TFL") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twenety.loc[(twenety.stat_type == "PD") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twenety.loc[(twenety.stat_type == "SOLO") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twenety.loc[(twenety.stat_type == "TOT") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(10))+((tacklesForLoss/10)*10)+((passDefended/3)*15)+((soloTackles/20)*35)+((tTackles/40)*30)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: sacks = twentyone.loc[(twentyone.stat_type == "SACKS") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except:sacks=0
            try: tacklesForLoss = twentyone.loc[(twentyone.stat_type == "TFL") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twentyone.loc[(twentyone.stat_type == "PD") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twentyone.loc[(twentyone.stat_type == "SOLO") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twentyone.loc[(twentyone.stat_type == "TOT") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((sacks/3)*(10))+((tacklesForLoss/10)*10)+((passDefended/3)*15)+((soloTackles/20)*35)+((tTackles/40)*30)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp-.7)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in CB.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "defensive") & (seventeen.category !="interceptions") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "defensive") & (eightteen.category !="interceptions")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "defensive") & (nineteen.category !="interceptions")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "defensive") & (twenety.category !="interceptions")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "defensive") & (twentyone.category !="interceptions") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    print(twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: ints = seventeen.loc[(seventeen.stat_type == "INT") & (seventeen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = seventeen.loc[(seventeen.stat_type == "TFL") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = seventeen.loc[(seventeen.stat_type == "PD") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = seventeen.loc[(seventeen.stat_type == "SOLO") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = seventeen.loc[(seventeen.stat_type == "TOT") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/5)*(30))+((tacklesForLoss/5)*5)+((passDefended/10)*35)+((soloTackles/15)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: ints = eightteen.loc[(eightteen.stat_type == "INT") & (eightteen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = eightteen.loc[(eightteen.stat_type == "TFL") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = eightteen.loc[(eightteen.stat_type == "PD") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = eightteen.loc[(eightteen.stat_type == "SOLO") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = eightteen.loc[(eightteen.stat_type == "TOT") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/5)*(30))+((tacklesForLoss/5)*5)+((passDefended/10)*35)+((soloTackles/15)*15)+((tTackles/40)*20)
            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: ints = nineteen.loc[(nineteen.stat_type == "INT") & (nineteen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = nineteen.loc[(nineteen.stat_type == "PD") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/5)*(30))+((tacklesForLoss/5)*5)+((passDefended/10)*35)+((soloTackles/15)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: ints = twenety.loc[(twenety.stat_type == "INT") & (twenety.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = twenety.loc[(twenety.stat_type == "TFL") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twenety.loc[(twenety.stat_type == "PD") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twenety.loc[(twenety.stat_type == "SOLO") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twenety.loc[(twenety.stat_type == "TOT") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/5)*(30))+((tacklesForLoss/5)*5)+((passDefended/10)*35)+((soloTackles/15)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: ints = twentyone.loc[(twentyone.stat_type == "INT") & (twentyone.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = twentyone.loc[(twentyone.stat_type == "TFL") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twentyone.loc[(twentyone.stat_type == "PD") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twentyone.loc[(twentyone.stat_type == "SOLO") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twentyone.loc[(twentyone.stat_type == "TOT") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/5)*(30))+((tacklesForLoss/5)*5)+((passDefended/10)*35)+((soloTackles/15)*15)+((tTackles/40)*20)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp-.5)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in S.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[(seventeen.category != "defensive") & (seventeen.category !="interceptions") & (seventeen.category !="fumbles")].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[(eightteen.category != "defensive") & (eightteen.category !="interceptions")& (eightteen.category !="fumbles")].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[(nineteen.category != "defensive") & (nineteen.category !="interceptions")& (nineteen.category !="fumbles")].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[(twenety.category != "defensive") & (twenety.category !="interceptions")& (twenety.category !="fumbles")].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[(twentyone.category != "defensive") & (twentyone.category !="interceptions") & (twentyone.category !="fumbles")].index)

    #m = pd.merge(seventeen, eightteen)
    print(twentyone)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: ints = seventeen.loc[(seventeen.stat_type == "INT") & (seventeen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = seventeen.loc[(seventeen.stat_type == "TFL") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = seventeen.loc[(seventeen.stat_type == "PD") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = seventeen.loc[(seventeen.stat_type == "SOLO") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = seventeen.loc[(seventeen.stat_type == "TOT") & (seventeen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/3)*(15))+((tacklesForLoss/5)*15)+((passDefended/7)*20)+((soloTackles/30)*20)+((tTackles/70)*30)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: ints = eightteen.loc[(eightteen.stat_type == "INT") & (eightteen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = eightteen.loc[(eightteen.stat_type == "TFL") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = eightteen.loc[(eightteen.stat_type == "PD") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = eightteen.loc[(eightteen.stat_type == "SOLO") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = eightteen.loc[(eightteen.stat_type == "TOT") & (eightteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/3)*(15))+((tacklesForLoss/5)*15)+((passDefended/7)*20)+((soloTackles/30)*20)+((tTackles/70)*30)
            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: ints = nineteen.loc[(nineteen.stat_type == "INT") & (nineteen.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = nineteen.loc[(nineteen.stat_type == "TFL") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = nineteen.loc[(nineteen.stat_type == "PD") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = nineteen.loc[(nineteen.stat_type == "SOLO") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = nineteen.loc[(nineteen.stat_type == "TOT") & (nineteen.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/3)*(15))+((tacklesForLoss/5)*15)+((passDefended/7)*20)+((soloTackles/30)*20)+((tTackles/70)*30)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: ints = twenety.loc[(twenety.stat_type == "INT") & (twenety.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = twenety.loc[(twenety.stat_type == "TFL") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twenety.loc[(twenety.stat_type == "PD") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twenety.loc[(twenety.stat_type == "SOLO") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twenety.loc[(twenety.stat_type == "TOT") & (twenety.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/3)*(15))+((tacklesForLoss/5)*15)+((passDefended/7)*20)+((soloTackles/30)*20)+((tTackles/70)*30)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: ints = twentyone.loc[(twentyone.stat_type == "INT") & (twentyone.category == "interceptions")].iloc[0]["stat"]
            except:ints=0
            try: tacklesForLoss = twentyone.loc[(twentyone.stat_type == "TFL") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: passDefended = twentyone.loc[(twentyone.stat_type == "PD") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: passDefended = 0
            try: soloTackles = twentyone.loc[(twentyone.stat_type == "SOLO") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: soloTackles = 0
            try: tTackles = twentyone.loc[(twentyone.stat_type == "TOT") & (twentyone.category == "defensive")].iloc[0]["stat"]
            except: tTackles=0
            
            score = ((ints/3)*(15))+((tacklesForLoss/5)*15)+((passDefended/7)*20)+((soloTackles/30)*20)+((tTackles/70)*30)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp-.5)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in P.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[seventeen.category != "punting"].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[eightteen.category != "punting"].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[nineteen.category != "punting"].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[twenety.category != "punting"].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[twentyone.category != "punting"].index)
    print(twentyone)
    #m = pd.merge(seventeen, eightteen)
    
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: TB = seventeen.loc[(seventeen.stat_type == "TB") & (seventeen.category == "punting")].iloc[0]["stat"]
            except:TB=0
            try: LONG = seventeen.loc[(seventeen.stat_type == "LONG") & (seventeen.category == "punting")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: YDS = seventeen.loc[(seventeen.stat_type == "YDS") & (seventeen.category == "punting")].iloc[0]["stat"]
            except: YDS = 0
            try: in20 = seventeen.loc[(seventeen.stat_type == "In 20") & (seventeen.category == "punting")].iloc[0]["stat"]
            except: in20 = 0
            try: YPP = seventeen.loc[(seventeen.stat_type == "YPP") & (seventeen.category == "punting")].iloc[0]["stat"]
            except: YPP=0
            
            score = ((in20/20)*(30))+((LONG/80)*15)+((YPP/45)*20)+((TB/5)*20)+((YDS/3000)*15)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: TB = eightteen.loc[(eightteen.stat_type == "TB") & (eightteen.category == "punting")].iloc[0]["stat"]
            except:TB=0
            try: LONG = eightteen.loc[(eightteen.stat_type == "LONG") & (eightteen.category == "punting")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: YDS = eightteen.loc[(eightteen.stat_type == "YDS") & (eightteen.category == "punting")].iloc[0]["stat"]
            except: YDS = 0
            try: in20 = eightteen.loc[(eightteen.stat_type == "In 20") & (eightteen.category == "punting")].iloc[0]["stat"]
            except: in20 = 0
            try: YPP = eightteen.loc[(eightteen.stat_type == "YPP") & (eightteen.category == "punting")].iloc[0]["stat"]
            except: YPP=0
            
            score = ((in20/20)*(30))+((LONG/80)*15)+((YPP/45)*20)+((TB/5)*20)+((YDS/3000)*15)
            if score > 100:
                score = 100

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: TB = nineteen.loc[(nineteen.stat_type == "TB") & (nineteen.category == "punting")].iloc[0]["stat"]
            except:TB=0
            try: LONG = nineteen.loc[(nineteen.stat_type == "LONG") & (nineteen.category == "punting")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: YDS = nineteen.loc[(nineteen.stat_type == "YDS") & (nineteen.category == "punting")].iloc[0]["stat"]
            except: YDS = 0
            try: in20 = nineteen.loc[(nineteen.stat_type == "In 20") & (nineteen.category == "punting")].iloc[0]["stat"]
            except: in20 = 0
            try: YPP = nineteen.loc[(nineteen.stat_type == "YPP") & (nineteen.category == "punting")].iloc[0]["stat"]
            except: YPP=0
            
            score = ((in20/20)*(30))+((LONG/80)*15)+((YPP/45)*20)+((TB/5)*20)+((YDS/3000)*15)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: TB = twenety.loc[(twenety.stat_type == "TB") & (twenety.category == "punting")].iloc[0]["stat"]
            except:TB=0
            try: LONG = twenety.loc[(twenety.stat_type == "LONG") & (twenety.category == "punting")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: YDS = twenety.loc[(twenety.stat_type == "YDS") & (twenety.category == "punting")].iloc[0]["stat"]
            except: YDS = 0
            try: in20 = twenety.loc[(twenety.stat_type == "In 20") & (twenety.category == "punting")].iloc[0]["stat"]
            except: in20 = 0
            try: YPP = twenety.loc[(twenety.stat_type == "YPP") & (twenety.category == "punting")].iloc[0]["stat"]
            except: YPP=0
            
            score = ((in20/20)*(30))+((LONG/80)*15)+((YPP/45)*20)+((TB/5)*20)+((YDS/3000)*15)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: TB = twentyone.loc[(twentyone.stat_type == "TB") & (twentyone.category == "punting")].iloc[0]["stat"]
            except:TB=0
            try: LONG = twentyone.loc[(twentyone.stat_type == "LONG") & (twentyone.category == "punting")].iloc[0]["stat"]
            except: tacklesForLoss = 0
            try: YDS = twentyone.loc[(twentyone.stat_type == "YDS") & (twentyone.category == "punting")].iloc[0]["stat"]
            except: YDS = 0
            try: in20 = twentyone.loc[(twentyone.stat_type == "In 20") & (twentyone.category == "punting")].iloc[0]["stat"]
            except: in20 = 0
            try: YPP = twentyone.loc[(twentyone.stat_type == "YPP") & (twentyone.category == "punting")].iloc[0]["stat"]
            except: YPP=0
            
            score = ((in20/20)*(30))+((LONG/80)*15)+((YPP/45)*20)+((TB/5)*20)+((YDS/3000)*15)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp)
    print(row['name'],Tscore, s)
    pros[row['id']] = s

for index, row in K.iterrows():
    Tscore = {}
    seventeen  = pd.DataFrame(row["2017"])
    eightteen = pd.DataFrame(row["2018"])
    nineteen = pd.DataFrame(row["2019"])
    twenety = pd.DataFrame(row["2020"])
    twentyone = pd.DataFrame(row["2021"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[seventeen.category != "kicking"].index)
    
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[eightteen.category != "kicking"].index)
    
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[nineteen.category != "kicking"].index)
    
    if twenety.empty == False:
        twenety = twenety.drop(twenety[twenety.category != "kicking"].index)
    
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[twentyone.category != "kicking"].index)
    #m = pd.merge(seventeen, eightteen)
    
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")
    if seventeen.empty == False:
        try : 
            
            try: PCT = seventeen.loc[(seventeen.stat_type == "PCT") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except:PCT=0
            try: LONG = seventeen.loc[(seventeen.stat_type == "LONG") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except: LONG = 0
            try: FGA = seventeen.loc[(seventeen.stat_type == "FGA") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except: FGA = 0
            try: FGM = seventeen.loc[(seventeen.stat_type == "FGM") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except: FGM = 0
            try: XPA = seventeen.loc[(seventeen.stat_type == "XPA") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except: XPA=0
            try: XPM = seventeen.loc[(seventeen.stat_type == "XPM") & (seventeen.category == "kicking")].iloc[0]["stat"]
            except: XPM=0

            score = ((PCT)*(50))+((LONG/55)*15)+((FGM/FGA)*20)+((XPM/XPA)*15)

            if score > 100:
                score = 100

            Tscore["2017"] = ((score/100))
        except Exception as e:
            Tscore["2017"] =(0)
            print(e)
    else:
        Tscore["2017"] =(0)
    if eightteen.empty == False:
        try:
            #nineteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
            try: PCT = eightteen.loc[(eightteen.stat_type == "PCT") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except:PCT=0
            try: LONG = eightteen.loc[(eightteen.stat_type == "LONG") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except: LONG = 0
            try: FGA = eightteen.loc[(eightteen.stat_type == "FGA") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except: FGA = 0
            try: FGM = eightteen.loc[(eightteen.stat_type == "FGM") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except: FGM = 0
            try: XPA = eightteen.loc[(eightteen.stat_type == "XPA") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except: XPA=0
            try: XPM = eightteen.loc[(eightteen.stat_type == "XPM") & (eightteen.category == "kicking")].iloc[0]["stat"]
            except: XPM=0
            try: score = ((PCT)*(50))+((LONG/55)*15)+((FGM/FGA)*20)+((XPM/XPA)*15)
            except: score = 0
            if score > 100:
                score = 100
            if np.isnan(score):
                score = 0

            #TDtoINT = TDs/INTs
            print("2018",score)
            Tscore["2018"] =((score/100))
        except Exception as e:
            print(e)
            Tscore["2018"] =(0)
    else:
        Tscore["2018"] =(0)
    if nineteen.empty == False:
        try:
            #nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
            try: PCT = nineteen.loc[(nineteen.stat_type == "PCT") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except:PCT=0
            try: LONG = nineteen.loc[(nineteen.stat_type == "LONG") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except: LONG = 0
            try: FGA = nineteen.loc[(nineteen.stat_type == "FGA") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except: FGA = 0
            try: FGM = nineteen.loc[(nineteen.stat_type == "FGM") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except: FGM = 0
            try: XPA = nineteen.loc[(nineteen.stat_type == "XPA") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except: XPA=0
            try: XPM = nineteen.loc[(nineteen.stat_type == "XPM") & (nineteen.category == "kicking")].iloc[0]["stat"]
            except: XPM=0
            score = ((PCT)*(50))+((LONG/55)*15)+((FGM/FGA)*20)+((XPM/XPA)*15)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2019",score)

            Tscore["2019"] =((score/100))
        except Exception as e:
            Tscore["2019"] =(0)
            print(e)
    else:
         Tscore["2019"] =(0)
    if twenety.empty == False:
        try:
            #twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
            try: PCT = twenety.loc[(twenety.stat_type == "PCT") & (twenety.category == "kicking")].iloc[0]["stat"]
            except:PCT=0
            try: LONG = twenety.loc[(twenety.stat_type == "LONG") & (twenety.category == "kicking")].iloc[0]["stat"]
            except: LONG = 0
            try: FGA = twenety.loc[(twenety.stat_type == "FGA") & (twenety.category == "kicking")].iloc[0]["stat"]
            except: FGA = 0
            try: FGM = twenety.loc[(twenety.stat_type == "FGM") & (twenety.category == "kicking")].iloc[0]["stat"]
            except: FGM = 0
            try: XPA = twenety.loc[(twenety.stat_type == "XPA") & (twenety.category == "kicking")].iloc[0]["stat"]
            except: XPA=0
            try: XPM = twenety.loc[(twenety.stat_type == "XPM") & (twenety.category == "kicking")].iloc[0]["stat"]
            except: XPM=0

            score = ((PCT)*(50))+((LONG/55)*15)+((FGM/FGA)*20)+((XPM/XPA)*15)

            if score > 100:
                score = 100
            print("2020",score)

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
            try: PCT = twentyone.loc[(twentyone.stat_type == "PCT") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except:PCT=0
            try: LONG = twentyone.loc[(twentyone.stat_type == "LONG") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except: LONG = 0
            try: FGA = twentyone.loc[(twentyone.stat_type == "FGA") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except: FGA = 0
            try: FGM = twentyone.loc[(twentyone.stat_type == "FGM") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except: FGM = 0
            try: XPA = twentyone.loc[(twentyone.stat_type == "XPA") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except: XPA=0
            try: XPM = twentyone.loc[(twentyone.stat_type == "XPM") & (twentyone.category == "kicking")].iloc[0]["stat"]
            except: XPM=0

            score = ((PCT)*(50))+((LONG/55)*15)+((FGM/FGA)*20)+((XPM/XPA)*15)

            if score > 100:
                score = 100
            #TDtoINT = TDs/INTs
            print("2021",score)

            Tscore["2021"] =((score/100))
        except Exception as e:
            Tscore["2021"] =(0)
            print(e)
    else:
        Tscore["2021"] =(0)
    exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    s = sum(Tscore.values())/(exp)
    print(row['name'],Tscore, s)
    print(row['id'])
    pros[row['id']] = s

for index, row in OL.iterrows():
    Tscore = {}
    pros[row['id']] = 0

#print(pros)

scoresDF = pd.DataFrame(list(pros.items()),columns = ['id','score'])
print(df)
print(scoresDF)
df_merged = pd.merge(df, scoresDF)

del df_merged["2017"]
del df_merged["2018"]
del df_merged["2019"]
del df_merged["2020"]
del df_merged["2021"]
df_merged = df_merged.rename(columns={'id': 'playerid', 'first_name': 'firstName', 'last_name': 'lastName', 'school': 'college', 'RASS': 'athleteGrade', 'score': 'positionGrade'})
df_merged['athleteGrade'] = df_merged['athleteGrade'].fillna(0)
df_merged['team'] = 'dne'
df_merged['drafted'] = False
df_merged['pick'] = 0
print(df_merged)
conn = sqlite3.connect("C:/Users/ryhil/OneDrive/Documents/ODUCS/620/NFL_Draft_Predictor/backend/db.sqlite3")
df_merged.to_sql('app_drafted', conn, if_exists='replace', index=False)