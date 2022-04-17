import json
import pandas as pd
from pprint import pprint
import cfbd

configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = "pv1BZu5ZeXlXrbx9qeiA9MYFgTym+f7grOE83NtED+d9YKRYyC4WmkQn4gHP8sKx"
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))

years = [2017, 2018, 2019, 2020, 2021]
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
        outfile.write(']')