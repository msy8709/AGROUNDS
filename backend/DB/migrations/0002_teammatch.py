# Generated by Django 4.0.3 on 2025-01-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_code', models.CharField(max_length=45)),
                ('team_code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'team_match',
                'managed': False,
            },
        ),
    ]