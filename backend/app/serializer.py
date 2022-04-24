from rest_framework import serializers
from . models import *

class TeamSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Teams
        fields = "__all__"
        #fields = ['acronym', 'name', 'wins', 'losses', 'pointsFor', 'pointsAgainst', 'yardsFor', 'passingYards', 'passingTDs', 'passingInterceptions', 'rushingAttempts', 'rushingYards', 'defensiveInterceptions', 'forcedFumbles' ]

class RosterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Roster
        fields = "__all__"
        #fields = ['rosterID', 'no', 'acronym', 'name', 'position', 'gamesPlayed', 'gamesStarted', 'weight', 'height', 'college', 'birthDate', 'years']
    

class OffenseSerializer(serializers.ModelSerializer):
    '''Team = TeamSerializer(many=True)
    Roster = RosterSerializer(many=True)'''
    class Meta:
        model = Offense
        fields = "__all__"
        #fields = ('acronym', 'rosterID', 'completions', 'attempts', 'passingYards', 'passingTDs', 'interceptions', 'qbRate', 'qbr', 'rushingAttempts', 'rushingYards', 'rushingTDs', 'rushingYPG', 'rushingAPG', 'passTargets', 'receptions', 'receivingYards', 'receivingTDs', 'catchPercentage', 'touches', 'yardsFromScrimmage', 'fumbles')
class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = "__all__"
        #fields = ['acronym', 'rosterID', 'interceptions', 'interceptionsYards', 'interceptionTDs', 'passDefended', 'forcedFumbles', 'fumblesRecovered', 'fumbleYards', 'fumbleTDs', 'sacks', 'combinedTackles', 'soloTackles', 'assistedTackles', 'tacklesForLoss', 'qbHits', 'safeties']
class SpecialTeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTeams
        fields = "__all__"
        #fields = ['acronym', 'rosterID', 'AllFGA', 'AllFGM', 'twentyFGA', 'twentyFGM', 'thirtyFGA', 'thirtyFGM', 'fortyFGA', 'fortyFGM', 'fiftyPlusFGA', 'fiftyPlusFGM', 'longestFG', 'FGPercentage', 'extraPointsAttempted', 'extraPointsMade', 'kickOffs', 'kickOffYards', 'kickOffAvg', 'punts', 'puntYards', 'longestPunt', 'blockedPunts']
class CollegePlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegePlayers
        fields = "__all__"
        #fields = ['playerid', 'name', 'firstname', 'lastname', 'college', 'weight', 'height', 'position', 'athleteGrade', 'postionGrade']
class DraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drafted
        fields = "__all__"
        #fields = ['playerid', 'name', 'firstname', 'lastname', 'college', 'weight', 'height', 'position', 'athleteGrade', 'postionGrade']
class DraftHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftHistory
        fields = "__all__"
        #fields = ['year', 'round', 'pick', 'name', 'team', 'postion', 'college', 'athleteGrade', 'postionGrade']

class RosterStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roster
        fields = fields = ['rosterID', 'no', 'acronym', 'name', 'position', 'gamesPlayed', 'gamesStarted', 'weight', 'height', 'college', 'birthDate', 'years', 'offense_set', 'defense_set', 'specialteams_set']