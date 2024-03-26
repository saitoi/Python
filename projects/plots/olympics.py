import pandas as pd
import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file)
    [print(row) for row in reader]

df = pd.read_csv(csv_filename, index_col='Rank')

print(df)
