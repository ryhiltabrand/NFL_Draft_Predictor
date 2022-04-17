import json
import pandas as pd
from pprint import pprint
import cfbd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = "pv1BZu5ZeXlXrbx9qeiA9MYFgTym+f7grOE83NtED+d9YKRYyC4WmkQn4gHP8sKx"
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
"""df = pd.read_csv('draft_picks.csv')
for i in df.index:
    print(df['Name'][i], df['College'][i])
    year = 2021
    position = df['Position'][i]
    team = df['College'][i]
    search_term = df['Name'][i]
    try:
        api_response = api_instance.player_search(search_term, team=team, year=year)
        for x in api_response:
            dict1 = x.__dict__
            del dict1["_configuration"]
            dict1["position"] = position
            json_object = json.dumps(dict1, indent = 4)
            with open("prospects.json", "a") as outfile:
                outfile.write(json_object)
                outfile.write(",\n")
            #file.writelines(json.dumps(dict1))
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_search: %s\n" % e)
        continue

#print(df)"""
"""years = [2017, 2018, 2019, 2020, 2021]
for year in years:
    with open(f"{year}_stats.json", "a") as outfile:
        outfile.write('[')
    try:
        api_response = api_instance.get_player_season_stats(year)
        print(type(api_response))
        for x in api_response:
                dict1 = x.__dict__
                del dict1["_configuration"]
                json_object = json.dumps(dict1, indent = 4)
                with open(f"{year}_stats.json", "a") as outfile:
                    outfile.write(json_object)
                    outfile.write(",\n")

    except Exception as e:
        print("Exception when calling PlayersApi->get_player_season_stats: %s\n" % e)
    with open(f"{year}_stats.json", "a") as outfile:
        outfile.write(']')"""

"""df17 = pd.read_json('2017_stats.json')
df18 = pd.read_json('2018_stats.json')
df19 = pd.read_json('2019_stats.json')
df20 = pd.read_json('2020_stats.json')
df21 = pd.read_json('2021_stats.json')
dfProspects = pd.read_json('prospects.json')


for i in dfProspects.index:
    id = dfProspects['_id'][i]
    name = dfProspects['_name'][i]
    school = dfProspects['_team'][i]
    first_name = dfProspects['_first_name'][i]
    last_name = dfProspects['_last_name'][i]
    weight = dfProspects['_weight'][i]
    height = dfProspects['_height'][i]
    position = dfProspects['position'][i]

    stats17 = df17[df17._player_id == id]
    stats18 = df18[df18._player_id == id]
    stats19 = df19[df19._player_id == id]
    stats20 = df20[df20._player_id == id]
    stats21 = df21[df21._player_id == id]


    Data = {
        "id" : str(id), 
        "name": name, 
        "first_name": first_name, 
        "last_name": last_name, 
        "school": school, 
        "weight": str(weight), 
        "height": str(height),
        "position" : position
        }

    stat2017json = json.loads(stats17[["_category","_stat_type", "_stat"]].to_json(orient="records"))
    stat2018json = json.loads(stats18[["_category","_stat_type", "_stat"]].to_json(orient="records"))
    stat2019json = json.loads(stats19[["_category","_stat_type", "_stat"]].to_json(orient="records"))
    stat2020json = json.loads(stats20[["_category","_stat_type", "_stat"]].to_json(orient="records"))
    stat2021json = json.loads(stats21[["_category","_stat_type", "_stat"]].to_json(orient="records"))

    if len(stat2017json) != 0:
        Data["2017"] = stat2017json
    if len(stat2018json) != 0:
        Data["2018"] = stat2018json
    if len(stat2019json) != 0:
        Data["2019"] = stat2019json
    if len(stat2020json) != 0:
        Data["2020"] = stat2020json
    if len(stat2021json) != 0:
        Data["2021"] = stat2021json
    jsonData = json.dumps(Data, indent = 4)
    with open(f"Prospects2022.json", "a") as outfile:
                    outfile.write(jsonData)
                    outfile.write(",\n")"""

df1 = pd.read_json("Prospects2022.json")
print(df1)