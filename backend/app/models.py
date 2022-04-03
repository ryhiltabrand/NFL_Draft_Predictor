from django.db import models

# Create your models here.
class React(models.Model):
    player = models.CharField(max_length=30)
    team = models.CharField(max_length=3)

class NFL(models.Model):
    team = models.CharField(max_length=10)
    roster = models.CharField(max_length=10)