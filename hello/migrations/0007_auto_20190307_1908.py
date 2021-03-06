# Generated by Django 2.1.5 on 2019-03-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_dfleaguedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfLeagueStandings',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('entry', models.BigIntegerField(blank=True, null=True)),
                ('entry_name', models.TextField(blank=True, null=True)),
                ('event_total', models.BigIntegerField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('last_rank', models.BigIntegerField(blank=True, null=True)),
                ('league', models.BigIntegerField(blank=True, null=True)),
                ('movement', models.TextField(blank=True, null=True)),
                ('own_entry', models.BooleanField(blank=True, null=True)),
                ('player_name', models.TextField(blank=True, null=True)),
                ('rank', models.BigIntegerField(blank=True, null=True)),
                ('rank_sort', models.BigIntegerField(blank=True, null=True)),
                ('start_event', models.BigIntegerField(blank=True, null=True)),
                ('stop_event', models.BigIntegerField(blank=True, null=True)),
                ('total', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'df_league_standings',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='dfleaguedetails',
            options={'get_latest_by': 'rating', 'managed': False},
        ),
    ]
