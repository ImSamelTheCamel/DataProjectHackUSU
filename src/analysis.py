import os

file_path = '/Users/samwillden/Projects/DataProjectHackUSU/nba_2022-23_all_stats_with_salary.csv'
if os.path.exists(file_path):
    print("File found:", file_path)
else:
    print("File not found at", file_path)
