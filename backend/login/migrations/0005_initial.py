# Generated by Django 5.0.1 on 2024-02-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_code', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=200)),
                ('user_birth', models.CharField(max_length=45)),
                ('user_name', models.CharField(max_length=45)),
                ('user_gender', models.CharField(max_length=45)),
                ('user_nickname', models.CharField(max_length=45)),
                ('marketing_agree', models.BooleanField()),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
