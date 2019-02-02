from django.shortcuts import render
from django.http import HttpResponse
import csv


from .models import Greeting
from .models import ReportCaptainPoints

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def reports(request):
    reportcaptain = ReportCaptainPoints.objects.all()
    output = ', '.join([p.player_name for p in reportcaptain])
    return HttpResponse(output)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
