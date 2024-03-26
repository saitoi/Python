import json
import urllib.request

json_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

with urllib.request.urlopen(json_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

