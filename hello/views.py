from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# https://fantasy.premierleague.com/drf/events/
def get_current_gw_details():
    # ZZZ must be a quicker way to do this..
    json_current_gw=json.loads(requests.get('https://fantasy.premierleague.com/drf/events/').text)
    list_current_gw=list(filter(lambda gw: gw['is_current'] == True, json_current_gw))
    return (list_current_gw)

# https://fantasy.premierleague.com/drf/leagues-classic-standings/league_id
def get_league_classic_standings(league_id)
    json_league_standings=json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id)).text)
    list_classic_standings=(json_league_standings['standings']['results'])
    league_name=(json_league_standings['league']['name'])
    return(list_classic_standings, league_name)

# https://fantasy.premierleague.com/drf/entry/entry_id/event/gw_id/picks
def get_entry_gw_picks(list_classic_standings, list_current_gw)
    list_entry_gw_picks = []
    for entry in list_classic_standings:
        temp_dict={}
        gw_id=(list_current_gw[0]['id'])
        temp_list=json.loads(requests.get('https://fantasy.premierleague.com/drf/entry/'+ str(entry['entry']) + '/event/' + str(gw_id) + '/picks').text)
        temp_dict = {'entry_id':entry, \
                    'active_chip':temp_list['active_chip'], \
                    'points':temp_list['entry_history']['points'], \
                    'overall_total_points':temp_list['entry_history']['total_points'], \
                    'event_transfers':temp_list['entry_history']['event_transfers'], \
                    'event_transfers_cost':temp_list['entry_history']['event_transfers_cost'], \
                    'value':temp_list['entry_history']['value'], \
                    'points_on_bench':temp_list['entry_history']['points_on_bench'], \
                    'bank':temp_list['entry_history']['bank']}
        temp_dict['rank']=entry['rank']
        temp_dict['last_rank']=entry['last_rank']
        temp_dict['movement']=entry['movement']
        temp_dict['rank_sort']=entry['rank_sort']
        temp_
        dict['adjusted_points']=temp_dict['points']-temp_dict['event_transfers_cost']
        temp_dict['mini_league_movement']=entry['movement']
        temp_dict['player_name']=entry['player_name']
        temp_dict['entry_name']=entry['entry_name']
        # Add dictionary to list
        list_entry_gw_picks.append(temp_dict)
        return (list_entry_gw_picks)

# Create your views here.
def index(request,league_id=231600):
    # Here goes!
    # Get the info on the vurrent gameweek - contains gw_id and gw_name
    list_current_gw=get_current_gw_details()

    #json_current_gw=json.loads(requests.get('https://fantasy.premierleague.com/drf/events/').text)
    #json_league_standings=json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id)).text)
    # league_name used in title
    league_name=(json_league_standings['league']['name'])
    list_live_leaders=sorted(list_of_dictionaries_mgr_summary, key = lambda i: i['adjusted_points'],reverse=True)
    live_leaders=[x for _, x in zip(range(5), list_live_leaders)]
    # Latest gameweek
    #list_current_gw=list(filter(lambda gw: gw['is_current'] == True, json_current_gw))
    # Manager of the week!
    #list_of_managers_and_scores=(json_league_standings['standings']['results'])
    #print (list_of_managers_and_scores)
    #dict_manager_of_the_week = max(list_of_managers_and_scores, key=lambda x:x['event_total'])
    # Change this to return a list using filter by max id - sorted
    #live_leaders=list(filter(lambda gw: gw['rank'] <=5 , list_of_managers_and_scores))
    #list_live_leaders=sorted(list_of_managers_and_scores, key = lambda i: i['event_total'],reverse=True)
    #live_leaders=[x for _, x in zip(range(5), list_live_leaders)]

    # Create a list of dictionary data that we are interested in
    # You could move this into a function
    # And create a function that gives top n

    context = {'league_name': league_name, \
                'dict_current_gw': list_current_gw[0], \
                'dict_manager_of_the_week' : dict_manager_of_the_week, \
                'live_leaders' : live_leaders,}

    return render(request, 'index.html', context)
