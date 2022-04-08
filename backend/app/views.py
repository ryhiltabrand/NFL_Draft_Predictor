from re import L
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


# Create your views here.

class ReactView(APIView):
    serializer_class = TeamSerializer
    def get(self, request):
        output = [{"name": output.name} for output in Teams.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
class NFLView(APIView):
    serializer_class = TeamSerializer
    def get(self, request):
        output = [{ "team": output.team, 'roster': output.roster} for output in NFL.objects.all()]
        return Response(output)
    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)