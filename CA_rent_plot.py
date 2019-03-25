import numpy as np
import pandas as pd
import plotly
import plotly.figure_factory as ff
from plotly.offline import *
from colour import Color
# To initiate ploty to run offline
init_notebook_mode(connected=True)

df = pd.read_csv('county_avg_rent.csv')
df_sub = pd.read_csv('countyfips.csv')

# Filter out counties not in CA
df_sub = df_sub[(df_sub.fips>=6000) & (df_sub.fips<=7000)]
# This is full join
df = pd.merge(df, df_sub, on='countyname', sort=False)
# Extract the county FIPS and median rent of each county
counties = df['fips'].tolist()
price = df['median_sqft_price'].tolist()
"""
# This is not working
red = Color('red')
heatmap_color = list(red.range_to(Color('yellow'), 5))
"""
heatmap_color = [
    'rgb(193, 193, 193)',
    'rgb(239, 239, 239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]
"""
heatmap_color = [
    'rgb(255, 0, 0)',
    'rgb(255, 51 ,0)',
    'rgb(255, 102, 0)',
    'rgb(255, 153, 0)',
    'rgb(255, 204, 0)',
    'rgb(255, 255, 0)'
]
"""
endpts = list(range(1,6))

# Reference:
# https://medium.com/@plotlygraphs/what-is-a-fips-code-county-level-charts-in-python-4eff383a4cf6
# https://plot.ly/~Dreamshot/9218/import-plotly-plotly-version-/#/
fig = ff.create_choropleth(
	  fips = counties, values = price, colorscale = heatmap_color,
	  show_state_data = True, scope = ['CA'],
	  binning_endpoints=endpts,
	  county_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  state_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  legend_title='Median Rent', title='Median Rent per Square Foot by County'
	  )
plotly.offline.plot(fig, filename='MedianRentByCounty.html')