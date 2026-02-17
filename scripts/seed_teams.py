import pandas as pd 
import nflreadpy as nfl
import pyarrow
from sqlalchemy import create_engine

''' 
    Won't be removing ['St. Louis Rams','Oakland Raiders','San Diego Chargers'].
    Will be used later for the RAG system to pull data uniquiley for them.
    nfl_team_table = logos[~logos['team_name'].isin(remove_teams)].reset_index(drop=True)
'''


# Start Engine Port
engine = create_engine("postgresql://codewithmikey:password@localhost:5433/nfl_project_v1")

# Load Teams - Convert to Pandas
teams = nfl.load_teams()
nfl_team_table = teams.select(['team_abbr', 'team_name', 'team_conf', 'team_division']).to_pandas()

'''
    Duplicate of LA Rams - team_abbr 'LA' is removed
    Adding '_' to able to add in values to postgreSQl
'''
nfl_team_table = nfl_team_table.reset_index(drop=True)
nfl_team_table['team_name'] = nfl_team_table['team_name'].str.replace(" ","_")
nfl_team_table['team_division'] = nfl_team_table['team_division'].str.replace(" ","_")
nfl_team_table = nfl_team_table[~(nfl_team_table['team_abbr'] == 'LAR')]

#

nfl_team_table.to_sql('nfl_team',engine,if_exists='append',index=False)






