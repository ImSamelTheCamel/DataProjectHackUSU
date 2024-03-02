
import pandas as pd

df = pd.read_csv('/Users/samwillden/Projects/DataProjectHackUSU/nba_2022-23_all_stats_with_salary.csv')
print(df.head())

df = df.drop(['Unnamed: 0', 'Position', 'Age', 'Team', 'GS', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'ORB', 'DRB', 'PF', 'Total Minutes', 'PER', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP'], axis=1)
print(df)

df = df.replace("", 0)

df.to_csv("cleaned_data")

dataDict = df.to_dict(orient='index')

playerSalaryRating = {}

for player_id, player_info in dataDict.items():
    player = player_info['Player Name']
    salary = player_info['Salary']
    gamesPlayed = player_info['GP'] / 82 * 4
    mpg = player_info['MP'] / 19.87 * 4
    eFG = player_info['eFG%'] / 0.533 * 2
    rebounds = player_info['TRB'] / 3.528 * 5
    assists = player_info['AST'] / 2.11 * 5
    steals = player_info['STL'] / 0.61 * 3
    blocks = player_info['BLK'] / 0.379 * 3
    turnovers = player_info['TOV'] / 1.114 * 5
    points = player_info['PTS'] / 9.13 * 5
    freethrow_percentage = player_info['FT%'] / 71.6 
    score = salary / points/ gamesPlayed / mpg / eFG / rebounds / assists / steals / blocks / turnovers / points / freethrow_percentage
    print(score)
