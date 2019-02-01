# Check the captain points by joining the data frames...

import pandas as pd
import json
import requests
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
pd.set_option('display.max_columns', None)

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

# Then get the league data
# ['entry', 'entry_name', 'event_total', 'id', 'last_rank', 'league', 'movement', 'own_entry',
# 'player_name', 'rank', 'rank_sort', 'start_event', 'stop_event', 'total']
json_league_standings = json.loads(requests.get('https://fantasy.premierleague.com/drf/leagues-classic-standings/231600').text)
df_league_standings = json_normalize(json_league_standings['standings'], 'results')

# Now loop through league standings and concatenate a dataframe with entry history in
# ['bank', 'entry', 'event', 'event_transfers', 'event_transfers_cost', 'id', 'movement', 'overall_rank',
# 'points', 'points_on_bench', 'rank', 'rank_sort', 'total_points', 'value']
#
# And a chip data frame
# ['chip', 'entry', 'event', 'name', 'played_time_formatted', 'status', 'time']
df_manager_history = pd.DataFrame()
df_manager_chips = pd.DataFrame()
for ls_index,ls_row in (df_league_standings.iterrows()):
    # Get history
    json_entry_history = \
     json.loads(requests.get('https://fantasy.premierleague.com/drf/entry/' + str(ls_row['entry']) + '/history').text)
    if df_manager_history.empty:
        df_manager_history = json_normalize(json_entry_history['history'])
    else:
        df_tmp = json_normalize(json_entry_history['history'])
        df_manager_history = pd.concat([df_manager_history, df_tmp], ignore_index=True)

    # Get chips
    if df_manager_chips.empty:
        df_manager_chips = json_normalize(json_entry_history['chips'])
    else:
        df_tmp = json_normalize(json_entry_history['chips'])
        df_manager_chips = pd.concat([df_manager_chips, df_tmp], ignore_index=True)


# We can use the last loop to set up the player picks for each week
# element  is_captain  is_vice_captain  multiplier  position   Entry  round
df_manager_history_picks = pd.DataFrame()
for ls_index,ls_row in (df_manager_history.iterrows()):
    #print (ls_row['entry'],ls_row['event'])
    json_manager_history_picks = \
     json.loads(requests.get('https://fantasy.premierleague.com/drf/entry/' \
                                    + str(ls_row['entry']) \
                                    + '/event/' \
                                    + str(ls_row['event']) \
                                    + '/picks').text)
    if df_manager_history_picks.empty:
        df_manager_history_picks = json_normalize(json_manager_history_picks['picks'])
        df_manager_history_picks['entry']=ls_row['entry']
        df_manager_history_picks['round']=ls_row['event']

    else:
        df_tmp = json_normalize(json_manager_history_picks['picks'])
        df_tmp['entry']=ls_row['entry']
        df_tmp['round']=ls_row['event']
        df_manager_history_picks = pd.concat([df_manager_history_picks, df_tmp], ignore_index=True)

# For each player and the round they played in - we need their points
# This will be keyed by entry and event
# Avoind picking up the player and gameweek more than once - no nned for that
#['assists', 'attempted_passes', 'big_chances_created', 'big_chances_missed', 'bonus', 'bps', 'clean_sheets',
#'clearances_blocks_interceptions', 'completed_passes', 'creativity', 'dribbles', 'ea_index', 'element',
#'errors_leading_to_goal', 'errors_leading_to_goal_attempt', 'fixture', 'fouls', 'goals_conceded', 'goals_scored',
#'ict_index', 'id', 'influence', 'key_passes', 'kickoff_time', 'kickoff_time_formatted', 'loaned_in', 'loaned_out',
#'minutes', 'offside', 'open_play_crosses', 'opponent_team', 'own_goals', 'penalties_conceded', 'penalties_missed',
#'penalties_saved', 'recoveries', 'red_cards', 'round', 'saves', 'selected', 'tackled', 'tackles', 'target_missed',
#'team_a_score', 'team_h_score', 'threat', 'total_points', 'transfers_balance', 'transfers_in', 'transfers_out',
#'value', 'was_home', 'winning_goals', 'yellow_cards']
df_manager_history_picks_players=pd.DataFrame()
list_of_unique_players=df_manager_history_picks.element.unique()
for element in list_of_unique_players:
    json_manager_history_picks_players = \
     json.loads(requests.get('https://fantasy.premierleague.com/drf/element-summary/' + str(element) ).text)
    if df_manager_history_picks.empty:
       df_manager_history_picks_players = json_normalize(json_manager_history_picks_players['history'])
    else:
       df_tmp = json_normalize(json_manager_history_picks_players['history'])
       df_manager_history_picks_players = pd.concat([df_manager_history_picks_players, df_tmp], ignore_index=True )

# df_manager_history_with_name
# THis is combo of entry details (name and things) and the history
#['bank', 'entry', 'event', 'event_transfers', 'event_transfers_cost', 'id_x', 'movement_x',
# 'overall_rank', 'points', 'points_on_bench', 'rank_x', 'rank_sort_x', 'total_points', 'value', 'entry_name',
# 'event_total', 'id_y', 'last_rank', 'league', 'movement_y', 'own_entry', 'player_name', 'rank_y',
# 'rank_sort_y', 'start_event', 'stop_event', 'total']
df_manager_history_with_name=pd.merge(df_manager_history, df_league_standings, on='entry')

# df_manager_history_picks_with_names
# Can work out captain points from this = basically each week#s picks for each game week for each manager
#['element', 'is_captain', 'is_vice_captain', 'multiplier', 'position', 'entry',
# 'round', 'assists', 'attempted_passes', 'big_chances_created', 'big_chances_missed', 'bonus',
# 'bps', 'clean_sheets', 'clearances_blocks_interceptions', 'completed_passes', 'creativity',
# 'dribbles', 'ea_index', 'errors_leading_to_goal', 'errors_leading_to_goal_attempt', 'fixture',
# 'fouls', 'goals_conceded', 'goals_scored', 'ict_index', 'id_x', 'influence', 'key_passes', 'kickoff_time',
# 'kickoff_time_formatted', 'loaned_in', 'loaned_out', 'minutes', 'offside', 'open_play_crosses', 'opponent_team',
# 'own_goals', 'penalties_conceded', 'penalties_missed', 'penalties_saved', 'recoveries', 'red_cards', 'saves',
# 'selected', 'tackled', 'tackles', 'target_missed', 'team_a_score', 'team_h_score', 'threat', 'total_points',
# 'transfers_balance', 'transfers_in', 'transfers_out', 'value', 'was_home', 'winning_goals', 'yellow_cards',
# 'entry_name', 'event_total', 'id_y', 'last_rank', 'league', 'movement', 'own_entry', 'player_name', 'rank',
# 'rank_sort', 'start_event', 'stop_event', 'total']
df_tmp=pd.merge(df_manager_history_picks,df_manager_history_picks_players,on=['element','round'])
df_manager_history_picks_with_names=pd.merge(df_tmp,df_league_standings,on='entry')
# Captains as above but just the captain picks and points doubled = should be tripled for TC chip!
df_captains=(df_manager_history_picks_with_names[df_manager_history_picks_with_names.is_captain==True])
# This merge tells us when the chips were played and factors in 3x chip for captain points.
df_captains = pd.merge(df_captains,df_manager_chips,left_on=['entry','round'],right_on=['entry','event'] ,how='outer')
df_captains['total_captain_point_multiplier'] = np.where(df_captains['name']=='3xc',3,2)
df_captains['total_captain_points'] = np.where(1==1,df_captains['total_points'] * df_captains['total_captain_point_multiplier'],9999)

#['chip', 'entry', 'event', 'name', 'played_time_formatted', 'status', 'time',
#'entry_name', 'event_total', 'id', 'last_rank', 'league',
#'movement', 'own_entry', 'player_name', 'rank', 'rank_sort', 'start_event', 'stop_event', 'total']
df_manager_chips_names=pd.merge(df_manager_chips,df_league_standings, on='entry')

report_transfer_costs=df_manager_history_with_name['event_transfers_cost'].groupby(df_manager_history_with_name['player_name']).sum().reset_index().sort_values(by='event_transfers_cost',ascending=False)
report_transfer_costs.to_csv(r'hello\static\report_transfer_costs.csv', header=None, index=None, sep=' ', mode='a')

report_point_burner=df_manager_history_with_name['points_on_bench'].groupby(df_manager_history_with_name['player_name']).sum().reset_index().sort_values(by='points_on_bench',ascending=False)
report_point_burner.to_csv(r'hello\static\report_point_burner.csv', header=None, index=None, sep=' ', mode='a')

report_captain_points=df_captains['total_points'].groupby(df_captains['player_name']).sum().reset_index().sort_values(by='total_points',ascending=False)
report_captain_points.to_csv(r'hello\static\report_captain_points.csv', header=None, index=None, sep=' ', mode='a')

report_chips_played=df_manager_chips_names[['player_name','name','played_time_formatted','event']].sort_values(by='event')
report_chips_played.to_csv(r'hello\static\report_chips_played.csv', header=None, index=None, sep=' ', mode='a')

print("start")
from sqlalchemy import create_engine
import pandas as pd
import subprocess
proc = subprocess.Popen('heroku config:get DATABASE_URL -a ffgringo', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
engine = create_engine(db_url)
report_captain_points.to_sql('hello_captainsreport', engine)
print("done")
