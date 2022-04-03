from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['player', 'team']
class NFLSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFL
        fields = ['team', 'roster']