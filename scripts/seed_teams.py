import pandas as pd 
import nflreadpy as nfl
import pyarrow
from sqlalchemy import create_engine

engine = create_engine("postgresql://codewithmikey:password@localhost:5433/nfl_project_v1")

teams = nfl.load_teams()

nfl_team_table = teams.select(['team_abbr', 'team_name', 'team_conf', 'team_division']).to_pandas()

nfl_team_table = nfl_team_table.reset_index(drop=True)

nfl_team_table['team_name'] = nfl_team_table['team_name'].str.replace(" ","_")
nfl_team_table['team_division'] = nfl_team_table['team_division'].str.replace(" ","_")

# DOUBLE LA RAMS - TEAM_ABBR 'LA' is not appropriate
nfl_team_table = nfl_team_table[~(nfl_team_table['team_abbr'] == 'LA')]


nfl_team_table.to_sql('nfl_team',engine,if_exists='append',index=False)





''' 
    Won't Remove these teams,will later use them for the future RAG system to pull data on them before the name change.
    remove_teams = ['St. Louis Rams','Oakland Raiders','San Diego Chargers']

    nfl_team_table = logos[~logos['team_name'].isin(remove_teams)].reset_index(drop=True)
'''


