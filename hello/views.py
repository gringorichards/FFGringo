from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

# https://fantasy.premierleague.com/drf/events/
def get_current_events_details():
    # ZZZ must be a quicker way to do this..
    #print('https://fantasy.premierleague.com/drf/events/')
    json_current_gw=json.loads(requests.get('https://fantasy.premierleague.com/drf/events/').text)
    list_current_gw=list(filter(lambda gw: gw['is_current'] == True, json_current_gw))
    gw_id=list_current_gw[0]['id']
    gw_name=list_current_gw[0]['name']
    gw_finished=list_current_gw[0]['finished']
    return (list_current_gw,gw_id,gw_name,gw_finished)

# https://fantasy.premierleague.com/drf/leagues-classic-standings/league_id
def get_league_classic_standings(league_id):
    #print('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id))
    json_league_standings=json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/'+ str(league_id)).text)
    list_classic_standings=(json_league_standings['standings']['results'])
    league_name=(json_league_standings['league']['name'])
    return(list_classic_standings, league_name)

# https://fantasy.premierleague.com/drf/entry/entry_id/event/gw_id/picks
def get_entry_gw_picks(list_classic_standings, gw_id):
    list_entry_gw_picks = []
    for entry in list_classic_standings:
        #print ('https://fantasy.premierleague.com/drf/entry/'+ str(entry['entry']) + '/event/' + str(gw_id) + '/picks')
        temp_dict={}
        temp_list=json.loads(requests.get('https://fantasy.premierleague.com/drf/entry/'+ str(entry['entry']) + '/event/' + str(gw_id) + '/picks').text)
        temp_dict = {'entry_id':entry['entry'], \
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
        temp_dict['adjusted_points']=temp_dict['points']-temp_dict['event_transfers_cost']
        temp_dict['mini_league_movement']=entry['movement']
        temp_dict['player_name']=entry['player_name']
        temp_dict['entry_name']=entry['entry_name']
        # Add dictionary to list
        list_entry_gw_picks.append(temp_dict)
    return (list_entry_gw_picks)

# Create your views here.
def index(request,league_id=231600):
    # Here goes!
    list_current_gw,gw_id,gw_name,gw_finished=get_current_events_details()
    list_classic_standings,league_name=get_league_classic_standings(league_id)
    gw_picks=get_entry_gw_picks(list_classic_standings,gw_id)
    list_live_leaders=sorted(gw_picks, key = lambda i: i['adjusted_points'],reverse=True)
    list_live_leaders_TopX=[x for _, x in zip(range(5), list_live_leaders)]
    max_points=max(list_live_leaders_TopX, key = lambda i: i['adjusted_points'])
    print (type(max_points))
    #live_leaders=list(filter(lambda gw: gw['rank'] <=5 , list_of_managers_and_scores))
    list_managers_of_the_week=list(filter(lambda gw: gw['adjusted_points'] == max_points['adjusted_points'],  list_live_leaders_TopX))
    print (type(list_managers_of_the_week))
    context = {'league_name': league_name, \
                'gw_name': gw_name, \
                'gw_finished': gw_finished, \
                'list_current_gw': list_current_gw, \
                'list_live_leaders_TopX' : list_live_leaders_TopX,
                'list_managers_of_the_week': list_managers_of_the_week}

    return render(request, 'index.html', context)
