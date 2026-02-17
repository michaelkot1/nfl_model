import nflreadpy as nfl
import pandas as pd
import pyarrow
from sqlalchemy import create_engine

#engine = create_engine("postgresql://codewithmikey:password@localhost:5433/nfl_project_v1")

# Load Data
years_data = nfl.load_schedules()
years_data_df = years_data.to_pandas()

''' 
Games From 2010/11-2025/26 Seasons
'''

nfl_game_data_2010_and_up = years_data_df[(years_data_df['season'] >= 2010)]

''' 
dropped ('nfl_detail_id','pff','ftn'). Too many empty rows- not relevant.
wind and temp has nan values because indoor games leave them nan.
 '''
nfl_game_data_2010_and_up = nfl_game_data_2010_and_up.drop(columns={'nfl_detail_id','pff','ftn'})
nfl_game_data_2010_and_up = nfl_game_data_2010_and_up.dropna(subset=['referee','away_moneyline','home_moneyline','away_spread_odds','home_spread_odds','under_odds','over_odds'])

#change to id
nfl_game_data_2010_and_up['home_team_id'] = nfl_game_data_2010_and_up['home_team']
nfl_game_data_2010_and_up['away_team_id'] = nfl_game_data_2010_and_up['away_team']

nfl_game_data_2010_and_up = nfl_game_data_2010_and_up.drop(columns={'home_team','away_team'})

# Check for null values
na_values = nfl_game_data_2010_and_up.columns[nfl_game_data_2010_and_up.isnull().any()]
null_counts = nfl_game_data_2010_and_up[na_values].isnull().sum()

print(nfl_game_data_2010_and_up.columns)






