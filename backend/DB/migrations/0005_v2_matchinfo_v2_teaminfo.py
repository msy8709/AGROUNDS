# Generated by Django 4.2.9 on 2024-05-10 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0004_playerinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='V2_MatchInfo',
            fields=[
                ('v2_match_code', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('v2_match_host', models.CharField(blank=True, max_length=45, null=True)),
                ('v2_match_location', models.CharField(blank=True, max_length=45, null=True)),
                ('v2_match_home', models.CharField(max_length=45)),
                ('v2_match_away', models.CharField(max_length=45)),
                ('v2_match_result', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'V2_match_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='V2_TeamInfo',
            fields=[
                ('v2_team_code', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('v2_team_host', models.CharField(blank=True, max_length=45, null=True)),
                ('v2_team_players', models.JSONField(blank=True, null=True)),
                ('v2_team_logo', models.CharField(blank=True, max_length=45, null=True)),
                ('v2_team_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'V2_team_info',
                'managed': False,
            },
        ),
    ]