from distutils.file_util import move_file
from django.db import models

# Create your models here.

class Teams(models.Model):
    acronym = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=30)
    wins = models.IntegerField()
    losses = models.IntegerField()
    pointsFor = models.IntegerField()
    pointsAgainst = models.IntegerField()
    yardsFor = models.IntegerField()
    yardsAgainst = models.IntegerField()
    passingYards = models.IntegerField()
    passingTDs= models.IntegerField()
    passingInterceptions = models.IntegerField()
    sackPercentage = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    allowedSacks = models.IntegerField()
    rushingAttempts = models.IntegerField()
    rushingYards = models.IntegerField()
    defensiveInterceptions = models.IntegerField()
    defensiveSacks = models.IntegerField()
    forcedFumbles = models.IntegerField()


class Roster(models.Model):
    rosterID = models.CharField(max_length=30, primary_key=True)
    no = models.IntegerField()
    acronym = models.ForeignKey(Teams, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2)
    gamesPlayed = models.IntegerField()
    gamesStarted = models.IntegerField()
    weight = models.IntegerField()
    height = models.CharField(max_length=4, null=True)
    college = models.CharField(max_length=100)
    birthDate = models.CharField(max_length=12)
    years = models.IntegerField()


class Offense(models.Model):
    acronym = models.ForeignKey(Teams, on_delete=models.PROTECT)
    rosterID = models.ForeignKey(Roster, on_delete=models.PROTECT)
    completions = models.IntegerField(null=True)
    attempts = models.IntegerField(null=True)
    passingYards = models.IntegerField(null=True)
    passingTDs = models.IntegerField(null=True)
    interceptions = models.IntegerField(null=True)
    qbRate = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    qbr = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    rushingAttempts = models.IntegerField(null=True)
    rushingYards = models.IntegerField(null=True)
    rushingTDs = models.IntegerField(null=True)
    rushingYPG = models.IntegerField(null=True)
    rushingAPG = models.IntegerField(null=True)
    passTargets = models.IntegerField(null=True)
    receptions = models.IntegerField(null=True)
    receivingYards = models.IntegerField(null=True)
    receivingTDs = models.IntegerField(null=True)
    catchPercentage = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    touches = models.IntegerField(null=True)
    yardsFromScrimmage = models.IntegerField(null=True)
    fumbles = models.IntegerField(null=True)

class Defense(models.Model):
    acronym = models.ForeignKey(Teams, on_delete=models.PROTECT)
    rosterID = models.ForeignKey(Roster, on_delete=models.PROTECT)
    interceptions = models.IntegerField(null=True)
    interceptionsYards = models.IntegerField(null=True)
    interceptionTDs = models.IntegerField(null=True)
    passDefended = models.IntegerField(null=True)
    forcedFumbles = models.IntegerField(null=True)
    fumblesRecovered = models.IntegerField(null=True)
    fumbleYards = models.IntegerField(null=True)
    fumbleTDs = models.IntegerField(null=True)
    sacks = models.IntegerField(null=True)
    combinedTackles = models.IntegerField(null=True)
    soloTackles = models.IntegerField(null=True)
    assistedTackles = models.IntegerField(null=True)
    tacklesForLoss = models.IntegerField(null=True)
    qbHits = models.IntegerField(null=True)
    safeties = models.IntegerField(null=True)

class SpecialTeams(models.Model):
    acronym = models.ForeignKey(Teams, on_delete=models.PROTECT)
    rosterID = models.ForeignKey(Roster, on_delete=models.PROTECT)
    AllFGA = models.IntegerField(null=True)
    AllFGM = models.IntegerField(null=True)
    twentyFGA = models.IntegerField(null=True)
    twentyFGM = models.IntegerField(null=True)
    thirtyFGA = models.IntegerField(null=True)
    thirtyFGM = models.IntegerField(null=True)
    fortyFGA = models.IntegerField(null=True)
    fortyFGM = models.IntegerField(null=True)
    fiftyPlusFGA = models.IntegerField(null=True)
    fiftyPlusFGM = models.IntegerField(null=True)
    longestFG = models.IntegerField(null=True)
    FGPercentage = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    extraPointsAttempted = models.IntegerField(null=True)
    extraPointsMade = models.IntegerField(null=True)
    kickOffs = models.IntegerField(null=True)
    kickOffYards = models.IntegerField(null=True)
    kickOffAvg = models.IntegerField(null=True)
    punts = models.IntegerField(null=True)
    puntYards = models.IntegerField(null=True)
    longestPunt = models.IntegerField(null=True)
    blockedPunts = models.IntegerField(null=True)

class CollegePlayers(models.Model):
    playerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    weight = models.IntegerField()
    height = models.IntegerField()
    position = models.CharField(max_length=5)
    athleteGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    positionGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

class DraftHistory(models.Model):
    year = models.IntegerField()
    round = models.IntegerField()
    pick = models.IntegerField()
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=30)
    position = models.CharField(max_length=10)
    college = models.CharField(max_length=100)
    athleteGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    positionGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)

class Drafted(models.Model):
    playerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    weight = models.IntegerField()
    height = models.IntegerField()
    position = models.CharField(max_length=5)
    athleteGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    positionGrade = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    team = models.CharField(max_length=3)
    drafted = models.BooleanField()
    pick = models.IntegerField(default=0)