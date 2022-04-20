from turtle import position
import pandas as pd
import json

f = open("Prospects.json")
data = json.load(f)
df = pd.json_normalize(data)
QB = df.loc[df['position']=="QB"]
for index, row in QB.iterrows():

    print(row)
    seventeen  = pd.DataFrame(row["2017"])
    if seventeen.empty == False:
        seventeen = seventeen.drop(seventeen[seventeen.category == "defensive"].index)
    eightteen = pd.DataFrame(row["2018"])
    if eightteen.empty == False:
        eightteen = eightteen.drop(eightteen[eightteen.category == "defensive"].index)
    nineteen = pd.DataFrame(row["2019"])
    if nineteen.empty == False:
        nineteen = nineteen.drop(nineteen[nineteen.category == "defensive"].index)
    twenety = pd.DataFrame(row["2020"])
    if twenety.empty == False:
        twenety = twenety.drop(twenety[twenety.category == "defensive"].index)
    twentyone = pd.DataFrame(row["2021"])
    if twentyone.empty == False:
        twentyone = twentyone.drop(twentyone[twentyone.category == "defensive"].index)

    print(twentyone)
    #exp = [seventeen.empty, eightteen.empty, nineteen.empty, twenety.empty, twentyone.empty].count(False)
    #print(f"2017:{seventeen.empty}, 2018:{eightteen.empty}, 2019:{nineteen.empty}, 2020:{twenety.empty}, 2021:{twentyone.empty}, {exp}")