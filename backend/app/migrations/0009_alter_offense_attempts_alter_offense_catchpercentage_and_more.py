# Generated by Django 4.0.3 on 2022-04-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_yardsfromscrimage_offense_yardsfromscrimmage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offense',
            name='attempts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='catchPercentage',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='completions',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='fumbles',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='passTargets',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='passingTDs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='passingYards',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='qbRate',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='qbr',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='receivingTDs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='receivingYards',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='receptions',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='rushingAPG',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='rushingAttempts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='rushingTDs',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='rushingYPG',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='rushingYards',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='touches',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offense',
            name='yardsFromScrimmage',
            field=models.IntegerField(null=True),
        ),
    ]
