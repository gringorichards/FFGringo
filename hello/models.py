from django.db import models

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
