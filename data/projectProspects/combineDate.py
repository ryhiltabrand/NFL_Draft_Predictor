from os import listdir
from os.path import isfile, join
import os
import pandas as pd
import json
import re
import math
'''path = r"/Combine"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]'''
Prospects = pd.read_json('Prospects2022.json')
'''Score = pd.read_csv("RASS.csv")
for index, row in Score.iterrows():
    name = f'{row["Name"]}'
    Prospects.loc[Prospects['name'] == name, "RASS"] = row["RAS"]
print(Prospects)
Prospects.to_json('temp.json', orient='records', indent=4)'''
#print(Prospects)
arr = os.listdir('C:/Users/ryhil/OneDrive/Desktop/cs620/projectProspects/Combine')
for x in arr:
    combineDF = pd.read_csv(f'Combine/{x}')
    #print(x)
    for index, row in combineDF.iterrows():
        name = f'{row["FIRST NAME"]} {row["LAST NAME"]}'
        #combinedata = json.loads(row[["HEIGHT","WEIGHT","HAND","ARM","WING","10 SPLT","40 TIME","BENCH","VERT","BROAD","20S","3-CONE"]].to_json(orient="records"))
        playerData = Prospects.loc[Prospects['name'] == name]
        if playerData.empty == False:
            combinedata = {'HEIGHT': row['HEIGHT'], "WEIGHT": row["WEIGHT"], "HAND": row["HAND"],"ARM": row["ARM"],"WING": row["WING"],"10 SPLT": row["10 SPLT"], "40 TIME": row["40 TIME"],"BENCH": row["BENCH"],"VERT": row["VERT"],"BROAD": row["BROAD"],"20S": row["20S"],"3-CONE": row["3-CONE"]}
            #print(combinedata)
            #Prospects.loc[Prospects['name'] == name, 'Combine'] = combinedata
            results = x[x.find('(')+1:x.find(')')]
            #print(results)
            nm = name
            pos = playerData["position"].values[0]
            '''if
            MAKE AN IF FOR POSITION BASED ON WHAT IT SAYS ONLINE at RASS
            '''
            if pos == "S":
                pos = "FS"
            if pos == "IOL":
                if results == "C":
                    pos = "OC"
                elif results == "G":
                    pos = "OG"
                elif results == "OT":
                    pos = "OT"
                else:
                    pos = x
            if pos == "P" or pos == "K":
                pos = "PK"
            if pos == "EDGE":
                pos = "DE"
            if pos == "DL":
                pos = "DT"
            
            hd = combinedata["HAND"]
            cg = playerData["school"]
            am = combinedata["ARM"]
            ht = combinedata["HEIGHT"]
            wt = combinedata["WEIGHT"]
            ft = combinedata["40 TIME"]
            tn = combinedata["10 SPLT"]
            bn = combinedata["BENCH"]
            vt = combinedata["VERT"]
            bd = combinedata["BROAD"]
            sh = combinedata["20S"]
            cn = combinedata["3-CONE"]
            #print(pos.values, cg.values)
            #print(index)
            if math.isnan(hd):
                hd = ''
            if math.isnan(am):
                am = ''
            if math.isnan(ht):
                ht = ''
            if math.isnan(wt):
                wt = ''
            if math.isnan(ft):
                ft = ''
            if math.isnan(tn):
                tn = ''
            if math.isnan(bn):
                bn = ''
            if math.isnan(vt):
                vt = ''
            if isinstance(bd, str) == False:
                if math.isnan(bd):
                    bd = ''
            else:
                fiie = bd.split("'")
                feet = fiie[0]
                inch = fiie[1]+'0'
                bd = feet+inch
            if math.isnan(sh):
                sh = ''
            if math.isnan(cn):
                cn = ''

            print(nm, pos, hd, cg.values[0], am, ht, wt, ft, tn, bn, vt, bd, sh, cn)
            url = f"https://ras.football/ras-calculator/?nm={nm}&pos={pos}&hd={hd}&cg={cg.values[0]}&am={am}&ht={ht}&wt={wt}&ft={ft}&tw=&tn={tn}&bn={bn}&vt={vt}&bd={bd}&sh={sh}&cn={cn}"
            print(url.replace(' ', '+'))
#Prospects.to_json('temp.json', orient='records', lines=True)