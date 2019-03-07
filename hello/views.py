from django.shortcuts import render
from django.http import HttpResponse
import csv
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO

from .models import Greeting
from .models import ManagerReports
from .models import DfLeagueDetails
from .models import DfLeagueStandings
from django.db.models import Max


# Create your views here.
def index(request):
    league_list = DfLeagueDetails.objects.values('name')
    league_standings_list = DfLeagueStandings.objects.all()
    max_event_total = DfLeagueStandings.objects.all().aggregate(Max('event_total'))
    manager_of_the_week_list =  DfLeagueStandings.objects.filter(event_total=(max_event_total['event_total__max']))
    context = {'league_list': league_list, 'league_standings_list': league_standings_list,'manager_of_the_week_list': manager_of_the_week_list}
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
