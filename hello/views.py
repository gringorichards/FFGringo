from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# Create your views here.
def index(request,league_id=231600):
    # Here goes!
    json_current_gw=json.loads(requests.get('https://fantasy.premierleague.com/drf/events/').text)
    json_league_standings=json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id)).text)
    # league_name used in title
    league_name=(json_league_standings['league']['name'])
    # Latest gameweek
    list_current_gw=list(filter(lambda gw: gw['is_current'] == True, json_current_gw))
    # Manager of the week!
    list_of_managers_and_scores=(json_league_standings['standings']['results'])
    #print (list_of_managers_and_scores)
    dict_manager_of_the_week = max(list_of_managers_and_scores, key=lambda x:x['event_total'])
    # Change this to return a list using filter by max id - sorted
    #live_leaders=list(filter(lambda gw: gw['rank'] <=5 , list_of_managers_and_scores))
    live_leaders=sorted(list_of_managers_and_scores, key = lambda i: i['event_total'],reverse=True)
    ll=[x for _, x in zip(range(5), live_leaders)]
    live_leaders=ll
    context = {'league_name': league_name, 'dict_current_gw': list_current_gw[0], 'dict_manager_of_the_week' : dict_manager_of_the_week, 'live_leaders' : live_leaders }
    return render(request, 'index.html', context)
