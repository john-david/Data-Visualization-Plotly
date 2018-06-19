
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# create the DataFrame from abalone.csv
df = pd.read_csv('abalone.csv')

# print(df)

# take two random samples of different sizes

a = np.random.choice(df['rings'], 30, replace = False)
b = np.random.choice(df['rings'], 20, replace = False)

# create a data variable with two box plots

data = [go.Box(y = a, name = 'A'), go.Box(y = b, name = 'B') ]

layout = go.Layout(title = '2 random samples')

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)


