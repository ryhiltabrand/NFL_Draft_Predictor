import sqlite3
import pandas as pd
import stringcase

# Connect to SQLite3 Database
conn = sqlite3.connect("backend/db.sqlite3")
sql = 'DELETE FROM app_roster'
cur = conn.cursor()
cur.execute(sql)
conn.commit()

# Load data from CSV's into DataFrames
#teams = pd.read_csv("data/csv_models/teams.csv")
roster = pd.read_csv("data/csv_models/rosters.csv")
#defense = pd.read_csv("data/csv_models/defense_models.csv")
#offense = pd.read_csv("data/csv_models/offense_models.csv")
#special_teams = pd.read_csv("data/csv_models/special_teams.csv")

# Rename DataFrame columns to match with the column names in the database. Also remove columns that
# are not in the database.

'''for column in teams.columns:
    if column == "Fumbles":
        teams = teams.rename(columns={column : "forcedFumbles"})
    elif column == "PassingTDS":
        teams = teams.rename(columns={column : "passingTDs"})
    else:
        teams = teams.rename(columns={column : stringcase.camelcase(column)})

teams = teams.drop(columns=["unname"])'''

for column in roster.columns:
    if column == "No.":
        roster = roster.rename(columns={column : "no"})
    elif column == "Acronym":
        roster = roster.rename(columns={column : stringcase.camelcase(column) + "_id"})
    else:
        roster = roster.rename(columns={column : stringcase.camelcase(column)})

roster = roster.drop(columns=["unname", "aV", "age"])

'''for column in defense.columns:
    if column == "RosterID" or column == "Acronym":
        defense = defense.rename(columns={column : stringcase.camelcase(column) + "_id"})
    else:
        defense = defense.rename(columns={column : stringcase.camelcase(column)})

defense = defense.drop(columns=["unname"])'''

'''for column in offense.columns:
    if column == "RosterID" or column == "Acronym":
        offense = offense.rename(columns={column : stringcase.camelcase(column) + "_id"})
    else:
        offense = offense.rename(columns={column : stringcase.camelcase(column)})

offense = offense.drop(columns=["unname"])'''

'''for column in special_teams.columns:
    if column == "RosterID" or column == "Acronym":
        special_teams = special_teams.rename(columns={column : stringcase.camelcase(column) + "_id"})
    elif column == "AllFGA" or column == "AllFGM" or column == "FGPercentage":
        pass
    else:
        special_teams = special_teams.rename(columns={column : stringcase.camelcase(column)})

special_teams = special_teams.drop(columns=["unname"])

# Filter our rows if all necessary columns are Null
special_teams = special_teams.loc[special_teams["AllFGA"].notnull()
& special_teams["AllFGM"].notnull()
& special_teams["AllFGA"].notnull()
& special_teams["twentyFGA"].notnull()
& special_teams["twentyFGM"].notnull()
& special_teams["thirtyFGA"].notnull()
& special_teams["thirtyFGM"].notnull()
& special_teams["fortyFGA"].notnull()
& special_teams["fortyFGM"].notnull()
& special_teams["fiftyPlusFGA"].notnull()
& special_teams["fiftyPlusFGM"].notnull()
& special_teams["longestFG"].notnull()
& special_teams["FGPercentage"].notnull()
& special_teams["extraPointsAttempted"].notnull()
& special_teams["extraPointsMade"].notnull()
& special_teams["kickOffs"].notnull()
& special_teams["kickOffYards"].notnull()
& special_teams["kickOffAvg"].notnull()
& special_teams["punts"].notnull()
& special_teams["puntYards"].notnull()
& special_teams["longestPunt"].notnull()
& special_teams["blockedPunts"].notnull()]'''




# Load DataFrames into the SQLite3 Database.
#teams.to_sql("app_teams", conn, if_exists="append", index = False)
roster.to_sql("app_roster", conn, if_exists="append", index = False)
#defense.to_sql("app_defense", conn, if_exists="append", index = False)
#offense.to_sql("app_offense", conn, if_exists="append", index = False)
#special_teams.to_sql("app_specialteams", conn, if_exists="append", index = False)