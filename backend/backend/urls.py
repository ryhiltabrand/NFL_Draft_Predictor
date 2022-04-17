"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from app.views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'Team', TeamViewSet, 'team')
router.register(r'Roster', RosterViewSet, 'Roster')
router.register(r'Offense', OffenseViewSet, 'Offense')
router.register(r'Defense', DefenseViewSet, 'Defesne')
router.register(r'ST', SpecialTeamsViewSet, 'SpecialTeams')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('PON/', PositionsOfNeed.as_view(), name="PON"),
    path('AtoT/<acronym>/', AtoT, name="T")
    #path('Team/', TeamView.as_view(), name="Team"),
    #path('Roster/', RosterView.as_view(), name="Roster"),
    #path('Offense/', OffenseView.as_view(), name="Offense"),
    #path('Defense/', DefenseView.as_view(), name="Defense"),
    #path('ST/', SpecialTeamsView.as_view(), name="SpecialTeams"),
    #path('', include(router.urls)),
]

