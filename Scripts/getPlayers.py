import json
import pandas as pd
from pprint import pprint
import cfbd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = "pv1BZu5ZeXlXrbx9qeiA9MYFgTym+f7grOE83NtED+d9YKRYyC4WmkQn4gHP8sKx"
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
df = pd.read_csv('draft_picks.csv')
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
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->player_search: %s\n" % e)
        continue
