
# flights by day/hour heatmap

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('flights.csv')

# data variable

data =[go.Heatmap(x = df['year'], y = df['month'], z = df['passengers'])]

layout = go.Layout(title = 'flights')

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)


