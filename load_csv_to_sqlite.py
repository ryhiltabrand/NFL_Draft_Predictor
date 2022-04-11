import sqlite3
import pandas as pd

# Connect to SQLite3 Database
conn = sqlite3.connect("backend/db.sqlite3")

# Load data from CSV's into DataFrames
teams = pd.read_csv("data/csv_models/teams.csv")
rosters = pd.read_csv("data/csv_models/rosters.csv")
defense = pd.read_csv("data/csv_models/defense_models.csv")
offense = pd.read_csv("data/csv_models/offense_models.csv")
special_teams = pd.read_csv("data/csv_models/special_teams.csv")


# Rename DataFrame columns to match with the column names in the database
teams = teams.rename(columns={"Acronym" : "acronym", "Name" : "name", "Wins" : "wins", "Losses": "loses",
"PointsFor" : "pointsFor", "YardsFor" : "yardsFor", "PassingYards" : "passingYards", "PassingTDs" : "passingTDs",
"PassingInterceptions" : "passingInterceptions", "RushingAttempts" : "rushingAttempts", "RushingYards" : "rushingYards",
"DefensiveInterceptions" : "defensiveInterceptions", "Fumbles" : "forcedFumbles"})

rosters = rosters.rename(column)