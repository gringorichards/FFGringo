# Generated by Django 2.1.5 on 2019-03-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_auto_20190307_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfEvents',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('average_entry_score', models.BigIntegerField(blank=True, null=True)),
                ('data_checked', models.BooleanField(blank=True, null=True)),
                ('deadline_time', models.TextField(blank=True, null=True)),
                ('deadline_time_epoch', models.BigIntegerField(blank=True, null=True)),
                ('deadline_time_formatted', models.TextField(blank=True, null=True)),
                ('deadline_time_game_offset', models.BigIntegerField(blank=True, null=True)),
                ('finished', models.BooleanField(blank=True, null=True)),
                ('highest_score', models.FloatField(blank=True, null=True)),
                ('highest_scoring_entry', models.FloatField(blank=True, null=True)),
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('is_current', models.BooleanField(blank=True, null=True)),
                ('is_next', models.BooleanField(blank=True, null=True)),
                ('is_previous', models.BooleanField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'df_events',
                'managed': False,
            },
        ),
    ]
