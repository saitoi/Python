import sqlite3
import pandas as pd

pd.set_option('display.max_rows', None)

query = 'SELECT * FROM main.artists'
dfs = []
chunk_size = 10000

with sqlite3.connect('music.sqlite') as conn:
    for chunk in pd.read_sql_query(query, conn, chunksize=chunk_size):
        dfs.append(chunk)

    df = pd.concat(dfs, ignore_index=True)

print(df)

