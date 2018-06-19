
# bar chart 2

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("mocksurvey.csv", index_col = 0)

print(df)

data = [go.Bar(x = df.index, y = df[response], name = response)
    for response in df.columns]

layout = go.Layout(title = "Survey Results", barmode = 'stack')

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)

### horizontal

data = [go.Bar(x = df[response], y = df.index, orientation = 'h', name = response)
    for response in df.columns]

layout = go.Layout(title = "Survey Results", barmode = 'stack')

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)


