import geojson
import pandas as pd
import plotly.graph_objects as go

with open("file.geojson", "r", encoding="utf-8") as f:
    geometry = geojson.load(f)

fig = go.Figure([
    go.Choropleth(
        geojson = geometry,
        locations = df["code"],
        z = df["crude_rate"],
        text = df["label"]
    )])

fig.update_geos(
    fitbounds="locations",
    resolution=50,
    visible=False,
    showframe=False,
    projection={"type": "mercator"},
)
