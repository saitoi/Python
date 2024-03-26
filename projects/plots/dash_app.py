import pandas as pd
import cufflinks as cf
from plotly.offline import plot

# Assuming Cufflinks and Plotly are already installed and set up
cf.go_offline()

# Create a Plotly figure (using Cufflinks for simplicity)
df = pd.read_csv('OlympicMedals_2020.csv')
fig = df.iplot(kind='bar', asFigure=True)

# Convert the figure to an HTML div string
div = plot(fig, output_type='div', include_plotlyjs=False)

# Embed the div in an HTML template
html_string = f"""
<html>
<head>
<title>Plotly Chart</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>My Interactive Plotly Chart</h1>
    {div}
</body>
</html>
"""

# Save the HTML content to a file
with open('plotly_chart.html', 'w') as f:
    f.write(html_string)
