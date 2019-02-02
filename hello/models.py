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
