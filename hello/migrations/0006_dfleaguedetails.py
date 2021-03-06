# Generated by Django 2.1.5 on 2019-03-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_managerreports'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfLeagueDetails',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('field_scoring', models.TextField(blank=True, db_column='_scoring', null=True)),
                ('admin_entry', models.BigIntegerField(blank=True, null=True)),
                ('closed', models.BooleanField(blank=True, null=True)),
                ('created', models.TextField(blank=True, null=True)),
                ('forum_disabled', models.BooleanField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('league_type', models.TextField(blank=True, null=True)),
                ('leagueban_set', models.TextField(blank=True, null=True)),
                ('make_code_public', models.BooleanField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('rank', models.TextField(blank=True, null=True)),
                ('reprocess_standings', models.BooleanField(blank=True, null=True)),
                ('short_name', models.TextField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('start_event', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'df_league_details',
                'managed': False,
            },
        ),
    ]
