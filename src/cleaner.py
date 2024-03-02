import pandas as pd

df = pd.read_csv('../nba_2022-23_all_stats_with_salary.csv')
print(df.head())

df = df.drop(['Unnamed: 0', 'Position', 'Age', 'Team', 'GS', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'FT', 'FTA', 'ORB', 'DRB', 'PF', 'Total Minutes', 'PER', '3PAr', 'FTr', 'ORB%', 'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP'], axis=1)
print(df)

df = df.replace(None, 0)

pd.to_csv("cleaned_data")

