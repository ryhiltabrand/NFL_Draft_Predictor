# Generated by Django 4.0.3 on 2022-04-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_teams_allowedsacks_teams_defensivesacks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drafted',
            fields=[
                ('playerid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('position', models.CharField(max_length=5)),
                ('athleteGrade', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('positionGrade', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('team', models.CharField(max_length=3)),
            ],
        ),
        migrations.RenameField(
            model_name='collegeplayers',
            old_name='playeid',
            new_name='playerid',
        ),
    ]
