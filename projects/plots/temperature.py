import pandas as pd
import json

json_source = 'data.json'

with open(json_source, 'r', encoding='utf-8') as data:
    # Extracting complete dict
    full_data = json.load(data)

    # Converting dictionary to a list of tuples
    year_temp_pairs = list(full_data['data'].items())

    # Formatting properly columns and rows
    df = pd.DataFrame(year_temp_pairs, columns=['Year', 'Temperature Anomaly'])

    print(df)
