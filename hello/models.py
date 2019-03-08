from django.db import models
import django_tables2 as tables


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class ReportCaptainPoints(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    player_name = models.TextField(blank=True, null=True)
    total_points = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_captain_points'

class ManagerReports(models.Model):
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    report_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'manager_reports'

class DfLeagueDetails(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    field_scoring = models.TextField(db_column='_scoring', blank=True, null=True)  # Field renamed because it started with '_'.
    admin_entry = models.BigIntegerField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    created = models.TextField(blank=True, null=True)
    forum_disabled = models.BooleanField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    league_type = models.TextField(blank=True, null=True)
    leagueban_set = models.TextField(blank=True, null=True)
    make_code_public = models.BooleanField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    reprocess_standings = models.BooleanField(blank=True, null=True)
    short_name = models.TextField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    start_event = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'df_league_details'

class DfLeagueStandings(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    entry = models.BigIntegerField(blank=True, null=True)
    entry_name = models.TextField(blank=True, null=True)
    event_total = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=False, primary_key=True)
    last_rank = models.BigIntegerField(blank=True, null=True)
    league = models.BigIntegerField(blank=True, null=True)
    movement = models.TextField(blank=True, null=True)
    own_entry = models.BooleanField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    rank = models.BigIntegerField(blank=True, null=True)
    rank_sort = models.BigIntegerField(blank=True, null=True)
    start_event = models.BigIntegerField(blank=True, null=True)
    stop_event = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'df_league_standings'
        get_latest_by = 'event_total'

class DfEvents(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    average_entry_score = models.BigIntegerField(blank=True, null=True)
    data_checked = models.BooleanField(blank=True, null=True)
    deadline_time = models.TextField(blank=True, null=True)
    deadline_time_epoch = models.BigIntegerField(blank=True, null=True)
    deadline_time_formatted = models.TextField(blank=True, null=True)
    deadline_time_game_offset = models.BigIntegerField(blank=True, null=True)
    finished = models.BooleanField(blank=True, null=True)
    highest_score = models.FloatField(blank=True, null=True)
    highest_scoring_entry = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=False,primary_key=True)
    is_current = models.BooleanField(blank=True, null=True)
    is_next = models.BooleanField(blank=True, null=True)
    is_previous = models.BooleanField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'df_events'

    def __str__(self):
        return (self.name)
