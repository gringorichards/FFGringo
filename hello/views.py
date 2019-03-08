from django.shortcuts import render
from django.http import HttpResponse
import csv
import json
import requests
from pandas.io.json import json_normalize
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO

from .models import Greeting
from .models import ManagerReports
from .models import DfLeagueDetails
from .models import DfEvents
from .models import DfLeagueStandings
from django.db.models import Max


# Create your views here.
def index(request,league_id):
    # Here goes!
    json_league_standings = json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id)).text)
    # league_name used in title
    league_name=(json_league_standings['league']['name'])
    # Latest gameweek
    current_gameweek =  DfEvents.objects.get(is_current=True)
    # Manager of the week!
    list_of_managers_and_scores=(json_league_standings['standings']['results'])
    #print (list_of_managers_and_scores)
    print (type(list_of_managers_and_scores))
    dict_manager_of_the_week = max(list_of_managers_and_scores, key=lambda x:x['event_total'])
    manager_of_the_week=dict_manager_of_the_week.get('player_name')
    # Change this to return a list using filter by max id - sorted

    context = {'league_name': league_name, 'current_gameweek': current_gameweek, 'manager_of_the_week' : manager_of_the_week }
    return render(request, 'index.html', context)

def manager_of_the_week(request):
    max_event_total = DfLeagueStandings.objects.all().aggregate(Max('event_total'))
    manager_of_the_week_list =  DfLeagueStandings.objects.filter(event_total=(max_event_total['event_total__max']))
    context = {'manager_of_the_week_list': manager_of_the_week_list}
    return render(request, 'manager_of_the_week.html', context)

def reports(request):
    report_list = ManagerReports.objects.all()
    context = {'report_list': report_list}
    return render(request, 'manager_of_the_week.html', context)

def manager_reports1(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)

    # Store image in a string buffer
    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def manager_reports2(request):
    image_data = open("hello/static/point_burners.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def manager_reports3(request):
    image_data = open("hello/static/point_burners.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def manager_reports4(request):
    image_data = open("hello/static/point_burners.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
