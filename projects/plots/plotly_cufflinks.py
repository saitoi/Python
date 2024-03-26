import pandas as pd
import numpy as np
import plotly
import cufflinks as cf

# Ensuring that Plotly and Cufflinks work in offline mode
cf.go_offline()
plotly.offline.init_notebook_mode(connected=True)

# Creating a DataFrame
df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())

# Display the first few rows of the DataFrame
print(df.head())

# Creating a scatter plot
# In an IDE like IntelliJ, you need to use plot() instead of iplot()
fig = df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10, asFigure=True)
plotly.offline.plot(fig, filename='scatter_plot.html')
