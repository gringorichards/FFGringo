# Generated by Django 2.1.5 on 2019-03-07 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20190307_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dfleaguedetails',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dfleaguestandings',
            options={'get_latest_by': 'event_total', 'managed': False},
        ),
    ]
