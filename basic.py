
import numpy as np 
import plotly.offline as pyo 
import plotly.graph_objs as go 

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

trace = go.Scatter(
	x = random_x, 
	y = random_y, 
	mode='markers',
	marker=dict(
		size=12,
		color='rgb(255, 0, 0)',
		symbol='pentagon',
		line= {'width': 2}
	))

data = [trace]

layout = go.Layout(title = "first plot", 
					xaxis = {'title': 'Special X AXIS'},
					yaxis = dict(title="Very Special Y AXIS"),
					hovermode = 'closest')

fig = go.Figure(data = data, layout = layout)
pyo.plot(data, filename = "scatter.html")



