from .app.models import Teams

team = Teams.objects.filter(acronym__exact=f'sfo')
print(team)
