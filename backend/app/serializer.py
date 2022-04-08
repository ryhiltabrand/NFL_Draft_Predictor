from rest_framework import serializers
from . models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ['acronym', 'name', 'wins', 'loses', 'pointsFor', 'pointsAgainst', 'yardsFor', 'passingYards', 'passingTDs', 'passingInterceptions', 'rushingAttempts', 'rushingYards', 'defensiveInterceptions', 'forcedFumbles' ]

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = ['rosterID', 'no', 'acronym', 'name', 'position', 'gamesPlayed', 'gameseStarted', 'weight', 'height', 'college', 'birthDate', 'years']

class OffenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offense
        fields = ['acronym', 'rosterID', 'completions', 'attempts', 'passingYards', 'passingTDs', 'interceptions', 'qbRate', 'qbr', 'rushingAttempts', 'rushingYards', 'rushingTDs', 'rushingYPG', 'rushingAPG', 'passTargets', 'receptions', 'receivingYards', 'receivingTDs', 'catchPercentage', 'touches', 'yardsFromScrimage', 'fumbles']
class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = ['acronym', 'rosterID', 'interceptions', 'interceptionYards', 'interceptionTDs', 'passDefended', 'forcedFumbles', 'fumblesRecovered', 'fumbleYards', 'fumbleTDs', 'sacks', 'combinedTackles', 'soloTackles', 'assistedTackles', 'tacklesForLoss', 'qbHits', 'safteys']
class SpecialTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTeams
        fields = ['acronym', 'rosterID', 'AllFGA', 'ALlFGM', 'twentyFGA', 'twentyFGM', 'thirtyFGA', 'thirtyFGM', 'fortyFGA', 'fortyFGM', 'fiftyPlusFGA', 'fiftyPlusFGM', 'longestFG', 'FGPercentage', 'extraPointsAttempted', 'extraPointsMade', 'kickOffs', 'kickOffYards', 'kickOffAvg', 'punts', 'puntYards', 'longestPunt', 'blockedPunts']
class CollegePlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePlayers
        fields = ['playerid', 'name', 'firstname', 'lastname', 'college', 'weight', 'height', 'position', 'athleteGrade', 'postionGrade']
class DraftHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftHistory
        fields = ['year', 'round', 'pick', 'name', 'team', 'postion', 'college', 'athleteGrade', 'postionGrade']