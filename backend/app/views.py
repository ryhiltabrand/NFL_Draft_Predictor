from re import L
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response
from rest_framework import viewsets
import json
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg

# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):

    queryset=Teams.objects.all()
    serializer_class = TeamSerializer
    
class RosterViewSet(viewsets.ModelViewSet):

    queryset=Roster.objects.all()
    serializer_class = RosterSerializer
    

class OffenseViewSet(viewsets.ModelViewSet):

    queryset=Offense.objects.all()
    serializer_class = OffenseSerializer
    

class DefenseViewSet(viewsets.ModelViewSet):

    queryset=Defense.objects.all()
    serializer_class = DefenseSerializer
    

class SpecialTeamsViewSet(viewsets.ModelViewSet):

    queryset = SpecialTeams.objects.all()
    serializer_class = SpecialTeamsSerializer

def AllTeamData(request, acronym):
    #team = Teams.objects.filter(acronym__exact=f'{acronym}')
    #serializer_class = TeamSerializer
    Team = [{'acronym': output.acronym, 'name': output.name, 'wins': output.wins, 'losses': output.losses, 'pointsFor': output.pointsFor, 'pointsAgainst': output.pointsAgainst, 'yardsFor': output.yardsFor, 'yardsAgainst': output.yardsAgainst,'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'passingInterceptions': output.passingInterceptions,'sackPercentage': output.sackPercentage,'allowedSacks': output.allowedSacks,'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'defensiveInterceptions': output.defensiveInterceptions, 'forcedFumbles': output.forcedFumbles, 'defensiveSacks': output.defensiveSacks} for output in Teams.objects.filter(acronym__exact=f'{acronym}')]
    Squad = [{ 'rosterID': output.rosterID,'acronym':output.acronym_id, 'no': output.no, 'name': output.name, 'position': output.position, 'gamesPlayed': output.gamesPlayed, 'gamesStarted': output.gamesStarted, 'weight': output.weight, 'height': output.height, 'college': output.college, 'birthDate': output.birthDate, 'years': output.years} for output in Roster.objects.filter(acronym__exact=f'{acronym}')]
    OffenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'completions': output.completions, 'attempts': output.attempts, 'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'interceptions': output.interceptions, 'qbRate': output.qbRate, 'qbr': output.qbr, 'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'rushingTDs': output.rushingTDs, 'rushingYPG': output.rushingYPG, 'rushingAPG': output.rushingAPG, 'passTargets': output.passTargets, 'receptions': output.receptions, 'receivingYards': output.receivingYards, 'receivingTDs': output.receivingTDs, 'catchPercentage': output.catchPercentage, 'touches': output.touches, 'yardsFromScrimmage': output.yardsFromScrimmage, 'fumbles': output.fumbles} for output in Offense.objects.filter(acronym__exact=f'{acronym}')] 
    DefenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'interceptions': output.interceptions, 'interceptionsYards': output.interceptionsYards, 'interceptionTDs': output.interceptionTDs, 'passDefended': output.passDefended, 'forcedFumbles': output.forcedFumbles, 'fumblesRecovered': output.fumblesRecovered, 'fumbleYards': output.fumbleYards, 'fumbleTDs': output.fumbleTDs, 'sacks': output.sacks, 'combinedTackles': output.combinedTackles, 'soloTackles': output.soloTackles, 'assistedTackles': output.assistedTackles, 'tacklesForLoss': output.tacklesForLoss, 'qbHits': output.qbHits, 'safeties': output.safeties} for output in Defense.objects.filter(acronym__exact=f'{acronym}')]
    SpecialTeamsDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'AllFGA': output.AllFGA, 'AllFGM': output.AllFGM, 'twentyFGA': output.twentyFGA, 'twentyFGM': output.twentyFGM, 'thirtyFGA': output.thirtyFGA, 'thirtyFGM': output.thirtyFGM, 'fortyFGA': output.fortyFGA, 'fortyFGM': output.fortyFGM, 'fiftyPlusFGA': output.fiftyPlusFGA, 'fiftyPlusFGM': output.fiftyPlusFGM, 'longestFG': output.longestFG, 'FGPercentage': output.FGPercentage, 'extraPointsAttempted': output.extraPointsAttempted, 'extraPointsMade': output.extraPointsMade, 'kickOffs': output.kickOffs,'kickOffYards': output.kickOffYards , 'kickOffAvg': output.kickOffAvg, 'punts': output.punts, 'puntYards': output.puntYards, 'longestPunt': output.longestPunt, 'blockedPunts': output.blockedPunts } for output in SpecialTeams.objects.filter(acronym__exact=f'{acronym}')]
    output = [{'Team': Team, 'Roster': Squad, 'Offense': OffenseDict, 'Defense': DefenseDict, 'Special Teams':SpecialTeamsDict}]

    return JsonResponse(output, safe=False)

def RecommendedPositions(request, acronym):
    Team = [{'acronym': output.acronym, 'name': output.name, 'wins': output.wins, 'losses': output.losses, 'pointsFor': output.pointsFor, 'pointsAgainst': output.pointsAgainst, 'yardsFor': output.yardsFor, 'yardsAgainst': output.yardsAgainst,'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'passingInterceptions': output.passingInterceptions,'sackPercentage': output.sackPercentage,'allowedSacks': output.allowedSacks,'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'defensiveInterceptions': output.defensiveInterceptions, 'forcedFumbles': output.forcedFumbles, 'defensiveSacks': output.defensiveSacks} for output in Teams.objects.filter(acronym__exact=f'{acronym}')]
    Squad = [{ 'rosterID': output.rosterID,'acronym':output.acronym_id, 'no': output.no, 'name': output.name, 'position': output.position, 'gamesPlayed': output.gamesPlayed, 'gamesStarted': output.gamesStarted, 'weight': output.weight, 'height': output.height, 'college': output.college, 'birthDate': output.birthDate, 'years': output.years} for output in Roster.objects.filter(acronym__exact=f'{acronym}')]
    
    avgWins = Teams.objects.all().aggregate(Avg('wins'))['wins__avg']
    avgLosses = Teams.objects.all().aggregate(Avg('losses'))['losses__avg']
    avgPointsFor = Teams.objects.all().aggregate(Avg('pointsFor'))['pointsFor__avg']
    avgPointsAgainst = Teams.objects.all().aggregate(Avg('pointsAgainst'))['pointsAgainst__avg']
    avgYardsFor = Teams.objects.all().aggregate(Avg('yardsFor'))['yardsFor__avg']
    avgYardsAgainst = Teams.objects.all().aggregate(Avg('yardsAgainst'))['yardsAgainst__avg']
    avgPassingYards = Teams.objects.all().aggregate(Avg('passingYards'))['passingYards__avg']
    avgPassingTDs = Teams.objects.all().aggregate(Avg('passingTDs'))['passingTDs__avg']
    avgOInterceptions = Teams.objects.all().aggregate(Avg('passingInterceptions'))['passingInterceptions__avg']
    avgAllowedSacks = Teams.objects.all().aggregate(Avg('allowedSacks'))['allowedSacks__avg']
    avgRushingA = Teams.objects.all().aggregate(Avg('rushingAttempts'))['rushingAttempts__avg']
    avgRushingY = Teams.objects.all().aggregate(Avg('rushingYards'))['rushingYards__avg']
    avgDInterceptions = Teams.objects.all().aggregate(Avg('defensiveInterceptions'))['defensiveInterceptions__avg']
    forcedFumbles = Teams.objects.all().aggregate(Avg('forcedFumbles'))['forcedFumbles__avg']
    print("|", avgWins, "|",avgLosses, "|",avgPointsFor, "|",avgPointsAgainst,"|", avgYardsFor,"|",avgYardsAgainst, "|", avgPassingYards, "|",avgPassingTDs,"|", avgOInterceptions,"|",avgAllowedSacks,"|", avgRushingA, "|",avgRushingY,"|", avgDInterceptions,"|", forcedFumbles,"|")
    
    if Team[0]["pointsFor"] < avgPointsFor:
        print("offense sucks")
    if Team[0]["pointsAgainst"] > avgPointsAgainst:
        print("Defense is ass")
    
    OffenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'completions': output.completions, 'attempts': output.attempts, 'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'interceptions': output.interceptions, 'qbRate': output.qbRate, 'qbr': output.qbr, 'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'rushingTDs': output.rushingTDs, 'rushingYPG': output.rushingYPG, 'rushingAPG': output.rushingAPG, 'passTargets': output.passTargets, 'receptions': output.receptions, 'receivingYards': output.receivingYards, 'receivingTDs': output.receivingTDs, 'catchPercentage': output.catchPercentage, 'touches': output.touches, 'yardsFromScrimmage': output.yardsFromScrimmage, 'fumbles': output.fumbles} for output in Offense.objects.filter(acronym__exact=f'{acronym}')] 
    DefenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'interceptions': output.interceptions, 'interceptionsYards': output.interceptionsYards, 'interceptionTDs': output.interceptionTDs, 'passDefended': output.passDefended, 'forcedFumbles': output.forcedFumbles, 'fumblesRecovered': output.fumblesRecovered, 'fumbleYards': output.fumbleYards, 'fumbleTDs': output.fumbleTDs, 'sacks': output.sacks, 'combinedTackles': output.combinedTackles, 'soloTackles': output.soloTackles, 'assistedTackles': output.assistedTackles, 'tacklesForLoss': output.tacklesForLoss, 'qbHits': output.qbHits, 'safeties': output.safeties} for output in Defense.objects.filter(acronym__exact=f'{acronym}')]
    SpecialTeamsDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'AllFGA': output.AllFGA, 'AllFGM': output.AllFGM, 'twentyFGA': output.twentyFGA, 'twentyFGM': output.twentyFGM, 'thirtyFGA': output.thirtyFGA, 'thirtyFGM': output.thirtyFGM, 'fortyFGA': output.fortyFGA, 'fortyFGM': output.fortyFGM, 'fiftyPlusFGA': output.fiftyPlusFGA, 'fiftyPlusFGM': output.fiftyPlusFGM, 'longestFG': output.longestFG, 'FGPercentage': output.FGPercentage, 'extraPointsAttempted': output.extraPointsAttempted, 'extraPointsMade': output.extraPointsMade, 'kickOffs': output.kickOffs,'kickOffYards': output.kickOffYards , 'kickOffAvg': output.kickOffAvg, 'punts': output.punts, 'puntYards': output.puntYards, 'longestPunt': output.longestPunt, 'blockedPunts': output.blockedPunts } for output in SpecialTeams.objects.filter(acronym__exact=f'{acronym}')]
    output = [{'Team': Team, 'Roster': Squad, 'Offense': OffenseDict, 'Defense': DefenseDict, 'Special Teams':SpecialTeamsDict}]

    return JsonResponse(output, safe=False)

'''class TeamView(APIView):
    serializer_class = TeamSerializer
    def get(self, request):
        output = [{'acronym': output.acronym, 'name': output.name, 'wins': output.wins, 'losses': output.losses, 'pointsFor': output.pointsFor, 'pointsAgainst': output.pointsAgainst, 'yardsFor': output.yardsFor, 'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'passingInterceptions': output.passingInterceptions, 'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'defensiveInterceptions': output.defensiveInterceptions, 'forcedFumbles': output.forcedFumbles  } for output in Teams.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
class RosterView(APIView):
    serializer_class = RosterSerializer
    def get(self, request):
        output = [{ 'rosterID': output.rosterID, 'no': output.no, """'acronym': output.acronym,""" 'name': output.name, 'position': output.position, 'gamesPlayed': output.gamesPlayed, 'gamesStarted': output.gamesStarted, 'weight': output.weight, 'height': output.height, 'college': output.college, 'birthDate': output.birthDate, 'years': output.years} for output in Roster.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = RosterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class OffenseView(APIView):
    serializer_class = OffenseSerializer
    """'acronym': output.acronym, 'rosterID': output.rosterID,"""
    def get(self, request):
        output = [{'completions': output.completions, 'attempts': output.attempts, 'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'interceptions': output.interceptions, 'qbRate': output.qbRate, 'qbr': output.qbr, 'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'rushingTDs': output.rushingTDs, 'rushingYPG': output.rushingYPG, 'rushingAPG': output.rushingAPG, 'passTargets': output.passTargets, 'receptions': output.receptions, 'receivingYards': output.receivingYards, 'receivingTDs': output.receivingTDs, 'catchPercentage': output.catchPercentage, 'touches': output.touches, 'yardsFromScrimmage': output.yardsFromScrimmage, 'fumbles': output.fumbles} for output in Offense.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = OffenseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class DefenseView(APIView):
    serializer_class = DefenseSerializer
    """'acronym': output.acronym, 'rosterID': output.rosterID,"""
    def get(self, request):
        output = [{'interceptions': output.interceptions, 'interceptionsYards': output.interceptionsYards, 'interceptionTDs': output.interceptionTDs, 'passDefended': output.passDefended, 'forcedFumbles': output.forcedFumbles, 'fumblesRecovered': output.fumblesRecovered, 'fumbleYards': output.fumbleYards, 'fumbleTDs': output.fumbleTDs, 'sacks': output.sacks, 'combinedTackles': output.combinedTackles, 'soloTackles': output.soloTackles, 'assistedTackles': output.assistedTackles, 'tacklesForLoss': output.tacklesForLoss, 'qbHits': output.qbHits, 'safeties': output.safeties} for output in Defense.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = DefenseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class SpecialTeamsView(APIView):
    serializer_class = SpecialTeamsSerializer
    """'acronym': output.acronym, 'rosterID': output.rosterID,"""
    def get(self, request):
        output = [{'AllFGA': output.AllFGA, 'AllFGM': output.AllFGM, 'twentyFGA': output.twentyFGA, 'twentyFGM': output.twentyFGM, 'thirtyFGA': output.thirtyFGA, 'thirtyFGM': output.thirtyFGM, 'fortyFGA': output.fortyFGA, 'fortyFGM': output.fortyFGM, 'fiftyPlusFGA': output.fiftyPlusFGA, 'fiftyPlusFGM': output.fiftyPlusFGM, 'longestFG': output.longestFG, 'FGPercentage': output.FGPercentage, 'extraPointsAttempted': output.extraPointsAttempted, 'extraPointsMade': output.extraPointsMade, 'kickOffs': output.kickOffs,'kickOffYards': output.kickOffYards , 'kickOffAvg': output.kickOffAvg, 'punts': output.punts, 'puntYards': output.puntYards, 'longestPunt': output.longestPunt, 'blockedPunts': output.blockedPunts } for output in SpecialTeams.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = SpecialTeamsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)'''


    