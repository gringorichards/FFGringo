from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class CaptainsReport(models.Model):
    manager_name = models.CharField(max_length=100)
    points = models.IntegerField()
