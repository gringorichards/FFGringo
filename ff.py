# Check the captain points by joining the data frames...

import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import os
DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL)
import datetime
now = datetime.datetime.now()

print("I be starting")
print (now.strftime("%Y-%m-%d %H:%M"))
# Kick off by grabbing the bootstrap data - gameweek & player details are in here
# ['assists', 'bonus', 'bps', 'chance_of_playing_next_round', 'chance_of_playing_this_round', 'clean_sheets',
#'code', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall',
#'creativity', 'dreamteam_count', 'ea_index', 'element_type', 'ep_next', 'ep_this', 'event_points',
#'first_name', 'form', 'goals_conceded', 'goals_scored', 'ict_index', 'id', 'in_dreamteam', 'influence',
#'loaned_in', 'loaned_out', 'loans_in', 'loans_out', 'minutes', 'news', 'news_added', 'now_cost', 'own_goals',
#'penalties_missed', 'penalties_saved', 'photo', 'points_per_game', 'red_cards', 'saves', 'second_name',
#'selected_by_percent', 'special', 'squad_number', 'status', 'team', 'team_code', 'threat', 'total_points',
#'transfers_in', 'transfers_in_event', 'transfers_out', 'transfers_out_event', 'value_form', 'value_season', 'web_name', 'yellow_cards']
json_bootstrap = json.loads(requests.get('https://fantasy.premierleague.com/drf/bootstrap').text)
df_elements = json_normalize(json_bootstrap['elements'])
latest_gameweek= json_bootstrap['current-event']
df_events = json_normalize(json_bootstrap['events'])
df_events.to_sql('df_events',engine,if_exists='replace')
df_elements.to_sql('df_elements',engine,if_exists='replace')
print("I be finishing")
print (now.strftime("%Y-%m-%d %H:%M"))
