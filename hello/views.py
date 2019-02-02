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
    latest_question_list = ManagerReports.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'reports.html', context)

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
