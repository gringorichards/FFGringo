from django.shortcuts import render
from django.http import HttpResponse
import csv
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import StringIO

from .models import Greeting
from .models import ManagerReports

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def reports(request):
    report_list = ManagerReports.objects.all()
    context = {'report_list': report_list}
    return render(request, 'reports.html', context)

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
    buffer = StringIO()
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
