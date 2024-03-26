import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
# Reconnect to the SQLite database and combine the queries and plotting in a single block of code

with sqlite3.connect('music.sqlite') as conn:
    # Query to count the number of albums per artist
    album_count_query = """
    SELECT artist, COUNT(*) as album_count 
    FROM albums 
    GROUP BY artist
    ORDER BY album_count DESC
    """
    album_count_df = pd.read_sql(album_count_query, conn)

plt.figure(figsize=(60, 32))  # Increased figure size
plt.bar(album_count_df['artist'].astype(str), album_count_df['album_count'], color='skyblue')
plt.xlabel('Artist ID')
plt.ylabel('Album Count')
plt.title('Album Count by Artist')
plt.xticks(rotation=45, fontsize=8)  # Adjusted label angle and reduced font size
plt.tight_layout()

# Display the plot
plt.show()

