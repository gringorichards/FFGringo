from django.shortcuts import render
from django.http import HttpResponse
import csv


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

def manager_reports(request):
    image_data = open("hello/static/point_burners.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
