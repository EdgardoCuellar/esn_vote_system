# Generated by Django 5.0.4 on 2024-05-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esn_vote_system', '0006_vote_datetime_vote_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='votesession',
            name='number_of_participants',
            field=models.IntegerField(default=0),
        ),
    ]
