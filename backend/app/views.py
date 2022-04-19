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
import pandas as pd
import os
from django.conf import settings
import decimal

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
    #Creating Array of dictionaries of SQLite db
    Team = [{'acronym': output.acronym, 'name': output.name, 'wins': output.wins, 'losses': output.losses, 'pointsFor': output.pointsFor, 'pointsAgainst': output.pointsAgainst, 'yardsFor': output.yardsFor, 'yardsAgainst': output.yardsAgainst,'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'passingInterceptions': output.passingInterceptions,'sackPercentage': output.sackPercentage,'allowedSacks': output.allowedSacks,'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'defensiveInterceptions': output.defensiveInterceptions, 'forcedFumbles': output.forcedFumbles, 'defensiveSacks': output.defensiveSacks} for output in Teams.objects.filter(acronym__exact=f'{acronym}')]
    Squad = [{ 'rosterID': output.rosterID,'acronym':output.acronym_id, 'no': output.no, 'name': output.name, 'position': output.position, 'gamesPlayed': output.gamesPlayed, 'gamesStarted': output.gamesStarted, 'weight': output.weight, 'height': output.height, 'college': output.college, 'birthDate': output.birthDate, 'years': output.years} for output in Roster.objects.filter(acronym__exact=f'{acronym}')]
    OffenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'completions': output.completions, 'attempts': output.attempts, 'passingYards': output.passingYards, 'passingTDs': output.passingTDs, 'interceptions': output.interceptions, 'qbRate': output.qbRate, 'qbr': output.qbr, 'rushingAttempts': output.rushingAttempts, 'rushingYards': output.rushingYards, 'rushingTDs': output.rushingTDs, 'rushingYPG': output.rushingYPG, 'rushingAPG': output.rushingAPG, 'passTargets': output.passTargets, 'receptions': output.receptions, 'receivingYards': output.receivingYards, 'receivingTDs': output.receivingTDs, 'catchPercentage': output.catchPercentage, 'touches': output.touches, 'yardsFromScrimmage': output.yardsFromScrimmage, 'fumbles': output.fumbles} for output in Offense.objects.filter(acronym__exact=f'{acronym}')] 
    DefenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'interceptions': output.interceptions, 'interceptionsYards': output.interceptionsYards, 'interceptionTDs': output.interceptionTDs, 'passDefended': output.passDefended, 'forcedFumbles': output.forcedFumbles, 'fumblesRecovered': output.fumblesRecovered, 'fumbleYards': output.fumbleYards, 'fumbleTDs': output.fumbleTDs, 'sacks': output.sacks, 'combinedTackles': output.combinedTackles, 'soloTackles': output.soloTackles, 'assistedTackles': output.assistedTackles, 'tacklesForLoss': output.tacklesForLoss, 'qbHits': output.qbHits, 'safeties': output.safeties} for output in Defense.objects.filter(acronym__exact=f'{acronym}')]

    #Creating DFs from above arrays
    OffenseDF = pd.DataFrame(OffenseDict)
    DefenseDF = pd.DataFrame(DefenseDict)
    RosterDF = pd.DataFrame(Squad)
    file = os.path.join(settings.BASE_DIR, 'PositionalImportance.csv')
    PositionalImportanceDF = pd.read_csv(file)

    temp = RosterDF.loc[RosterDF['position']=='QB']
    Starting_QB=[temp.loc[temp['gamesStarted']==temp['gamesStarted'].max()].iloc[0]['rosterID']]
    temp = RosterDF.loc[RosterDF['position']=='RB']
    Starting_RB=[temp.loc[temp['gamesStarted']==temp['gamesStarted'].max()].iloc[0]['rosterID']]
    temp = RosterDF.loc[RosterDF['position']=='WR']
    Starting_WR_DF=temp.nlargest(n=3, columns=['gamesStarted'])
    Starting_WR=[Starting_WR_DF.iloc[0]['rosterID'],Starting_WR_DF.iloc[1]['rosterID'],Starting_WR_DF.iloc[2]['rosterID']]
    temp = RosterDF.loc[RosterDF['position']=='TE']
    Starting_TE=[temp.nlargest(n=1, columns=['gamesStarted']).iloc[0]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='T') | (RosterDF['position']=='OT') | (RosterDF['position']=='OL') | (RosterDF['position']=='OG') | (RosterDF['position']=='G')| (RosterDF['position']=='C')]
    Starting_OL_DF=temp.nlargest(n=5, columns=['gamesStarted'])
    Starting_OL=[Starting_OL_DF.iloc[0]['rosterID'],Starting_OL_DF.iloc[1]['rosterID'],Starting_OL_DF.iloc[2]['rosterID'],Starting_OL_DF.iloc[3]['rosterID'],Starting_OL_DF.iloc[4]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='DL') | (RosterDF['position']=='EDGE') | (RosterDF['position']=='DE')]
    Starting_Edge_DF=temp.nlargest(n=2, columns=['gamesStarted'])
    Starting_Edge=[Starting_Edge_DF.iloc[0]['rosterID'],Starting_Edge_DF.iloc[1]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='DT')|(RosterDF['position']=='NT')]
    Starting_DT_DF=temp.nlargest(n=2, columns=['gamesStarted'])
    Starting_DT=[Starting_DT_DF.iloc[0]['rosterID'],Starting_DT_DF.iloc[1]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='S') | (RosterDF['position']=='SS') | (RosterDF['position']=='FS')]
    Starting_S_DF=temp.nlargest(n=2, columns=['gamesStarted'])
    Starting_S=[Starting_S_DF.iloc[0]['rosterID'],Starting_S_DF.iloc[1]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='OLB') | (RosterDF['position']=='LB') | (RosterDF['position']=='ILB')| (RosterDF['position']=='LILB')| (RosterDF['position']=='RILB')| (RosterDF['position']=='ROLB')| (RosterDF['position']=='LOLB')]
    Starting_LB_DF=temp.nlargest(n=2, columns=['gamesStarted'])
    Starting_LB=[Starting_LB_DF.iloc[0]['rosterID'],Starting_LB_DF.iloc[1]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='CB')]
    Starting_CB_DF=temp.nlargest(n=3, columns=['gamesStarted'])
    Starting_CB=[Starting_CB_DF.iloc[0]['rosterID'],Starting_CB_DF.iloc[1]['rosterID'],Starting_CB_DF.iloc[2]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='K')]
    Starting_K=[temp.loc[temp['gamesStarted']==temp['gamesStarted'].max()].iloc[0]['rosterID']]
    temp = RosterDF.loc[(RosterDF['position']=='P')]
    Starting_P=[temp.loc[temp['gamesStarted']==temp['gamesStarted'].max()].iloc[0]['rosterID']]
    #print(Starting_Edge_DF)
    Starters={"QB": Starting_QB,"RB": Starting_RB,"WR": Starting_WR,"TE": Starting_TE,"OL": Starting_OL,"Edge": Starting_Edge,"DT": Starting_DT,"LB": Starting_LB,"CB": Starting_CB,"S": Starting_S,"K": Starting_K,"P": Starting_P}
    
    print(Starters)

    #print(OffenseDF)
    #print(DefenseDF)

    #Getting LEague avgs
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
    #print("|", avgWins, "|",avgLosses, "|",avgPointsFor, "|",avgPointsAgainst,"|", avgYardsFor,"|",avgYardsAgainst, "|", avgPassingYards, "|",avgPassingTDs,"|", avgOInterceptions,"|",avgAllowedSacks,"|", avgRushingA, "|",avgRushingY,"|", avgDInterceptions,"|", forcedFumbles,"|")
    DefenseScore = 0
    OffenseScore = 0
    
    if Team[0]["pointsFor"] < avgPointsFor:
        OffenseScore = OffenseScore - 1
    if Team[0]["yardsFor"] < avgYardsFor:
        OffenseScore = OffenseScore - 1
    if Team[0]["pointsAgainst"] > avgPointsAgainst:
        DefenseScore = DefenseScore - 1
    if Team[0]["yardsAgainst"] > avgYardsAgainst:
        DefenseScore = DefenseScore - 1
    
    positions = ["QB", "RB", "WR", "TE", "OT", "IOL", "Edge", "DL", "LB", "CB", "S"]
    pon = {}
    '''if DefenseScore < 0 and OffenseScore < 0:
        pon=positions
    elif DefenseScore < 0 and OffenseScore>= 0:
        pon = ["Edge", "DL", "LB", "CB", "S"]
    elif OffenseScore < 0 and DefenseScore>= 0:
        pon = ["QB", "RB", "WR", "TE", "OT", "IOL"]
    else:
        pon = positions'''
    
    """
    Good Stats ever per metric
    QBR:105.8
    Rating:104
    Yards: 3500
    TDs: 20
    Int: 12
    RushingYards: 
    """

    #Worse then 58 is pon
    pon["QB"] = ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['qbr'])/105)*(35)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['qbRate'])/104)*(35)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['passingYards']+OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['rushingYards'])/5000)*(10)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['passingTDs']+OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['rushingTDs'])/40)*(10)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['QB'][0]].iloc[0]['interceptions']-12)/12)*(10))

    #Worse then 50 is pon
    pon['RB'] = ((((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['RB'][0]].iloc[0]['rushingYards']))/(decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['RB'][0]].iloc[0]['rushingAttempts'])))/decimal.Decimal(5.5))*(30)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['RB'][0]].iloc[0]['rushingTDs'])/18)*(30)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['RB'][0]].iloc[0]['receivingYards'])/647)*(25)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['RB'][0]].iloc[0]['receivingTDs'])/8)*(15)) \
    
    pon['WR1'] = ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][0]].iloc[0]['receivingYards'])/1000)*(40)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][0]].iloc[0]['receivingTDs'])/6)*(20)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][0]].iloc[0]['catchPercentage'])/65)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][0]].iloc[0]['receptions'])/50)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][0]].iloc[0]['passTargets'])/70)*(15))
    
    pon['WR2'] = ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][1]].iloc[0]['receivingYards'])/1000)*(40)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][1]].iloc[0]['receivingTDs'])/6)*(20)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][1]].iloc[0]['catchPercentage'])/65)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][1]].iloc[0]['receptions'])/50)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][1]].iloc[0]['passTargets'])/70)*(15))

    pon['WR3'] = ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][2]].iloc[0]['receivingYards'])/1000)*(40)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][2]].iloc[0]['receivingTDs'])/6)*(20)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][2]].iloc[0]['catchPercentage'])/65)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][2]].iloc[0]['receptions'])/50)*(15)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['WR'][2]].iloc[0]['passTargets'])/70)*(15))

    #Worse then 70 is pon
    pon['TE'] = ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['TE'][0]].iloc[0]['receivingYards'])/500)*(60)) \
                + ((decimal.Decimal(OffenseDF.loc[OffenseDF['rosterID']==Starters['TE'][0]].iloc[0]['receivingTDs'])/4)*(40))

    pon["OL1"] = (decimal.Decimal(RosterDF.loc[RosterDF['rosterID']==Starters['OL'][0]].iloc[0]['gamesStarted']/17)*(50)) \
                + ((decimal.Decimal(Team[0]["allowedSacks"]-decimal.Decimal(avgAllowedSacks))/decimal.Decimal(avgAllowedSacks))*(25)) \
                + (decimal.Decimal(Team[0]["sackPercentage"])/decimal.Decimal(6))*(25)

    pon["OL2"] = (decimal.Decimal(RosterDF.loc[RosterDF['rosterID']==Starters['OL'][1]].iloc[0]['gamesStarted']/17)*(50)) \
                + ((decimal.Decimal(Team[0]["allowedSacks"]-decimal.Decimal(avgAllowedSacks))/decimal.Decimal(avgAllowedSacks))*(25)) \
                + (decimal.Decimal(Team[0]["sackPercentage"])/decimal.Decimal(6))*(25)
    pon["OL3"] = (decimal.Decimal(RosterDF.loc[RosterDF['rosterID']==Starters['OL'][2]].iloc[0]['gamesStarted']/17)*(50)) \
                + ((decimal.Decimal(Team[0]["allowedSacks"]-decimal.Decimal(avgAllowedSacks))/decimal.Decimal(avgAllowedSacks))*(25)) \
                + (decimal.Decimal(Team[0]["sackPercentage"])/decimal.Decimal(6))*(25)

    pon["OL4"] = (decimal.Decimal(RosterDF.loc[RosterDF['rosterID']==Starters['OL'][3]].iloc[0]['gamesStarted']/17)*(50)) \
                + ((decimal.Decimal(Team[0]["allowedSacks"]-decimal.Decimal(avgAllowedSacks))/decimal.Decimal(avgAllowedSacks))*(25)) \
                + (decimal.Decimal(Team[0]["sackPercentage"])/decimal.Decimal(6))*(25)

    pon["OL5"] = (decimal.Decimal(RosterDF.loc[RosterDF['rosterID']==Starters['OL'][4]].iloc[0]['gamesStarted']/17)*(20)) \
                + ((decimal.Decimal(Team[0]["allowedSacks"]-decimal.Decimal(avgAllowedSacks))/decimal.Decimal(avgAllowedSacks))*(25)) \
                + (decimal.Decimal(Team[0]["sackPercentage"])/decimal.Decimal(6))*(25)

    pon["EDGE"] = 1

    pon["DT"] = 1

    pon["LB"] = 1

    pon["CB"] = 1

    pon["S"] = 1
 
    #(Team[0]["passingInterceptions"]+Team[0]["passingYards"]+Team[0]["passingTDs"])/(avgPassingTDs+avgPassingYards+avgOInterceptions)
    print(pon)
    
    #pon["WR"] = 
    
    #pon["RB"] = (Team[0]())/(avgRushingTD+(avgRushingY/avgRushingA))
   
    DefenseDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'interceptions': output.interceptions, 'interceptionsYards': output.interceptionsYards, 'interceptionTDs': output.interceptionTDs, 'passDefended': output.passDefended, 'forcedFumbles': output.forcedFumbles, 'fumblesRecovered': output.fumblesRecovered, 'fumbleYards': output.fumbleYards, 'fumbleTDs': output.fumbleTDs, 'sacks': output.sacks, 'combinedTackles': output.combinedTackles, 'soloTackles': output.soloTackles, 'assistedTackles': output.assistedTackles, 'tacklesForLoss': output.tacklesForLoss, 'qbHits': output.qbHits, 'safeties': output.safeties} for output in Defense.objects.filter(acronym__exact=f'{acronym}')]
    #SpecialTeamsDict = [{'rosterID': output.rosterID_id,'acronym':output.acronym_id,'AllFGA': output.AllFGA, 'AllFGM': output.AllFGM, 'twentyFGA': output.twentyFGA, 'twentyFGM': output.twentyFGM, 'thirtyFGA': output.thirtyFGA, 'thirtyFGM': output.thirtyFGM, 'fortyFGA': output.fortyFGA, 'fortyFGM': output.fortyFGM, 'fiftyPlusFGA': output.fiftyPlusFGA, 'fiftyPlusFGM': output.fiftyPlusFGM, 'longestFG': output.longestFG, 'FGPercentage': output.FGPercentage, 'extraPointsAttempted': output.extraPointsAttempted, 'extraPointsMade': output.extraPointsMade, 'kickOffs': output.kickOffs,'kickOffYards': output.kickOffYards , 'kickOffAvg': output.kickOffAvg, 'punts': output.punts, 'puntYards': output.puntYards, 'longestPunt': output.longestPunt, 'blockedPunts': output.blockedPunts } for output in SpecialTeams.objects.filter(acronym__exact=f'{acronym}')]
    
    output = [{"Positions of Need": pon}]

    return JsonResponse(output, safe=False)


    