
# distplot

import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np


x1 = np.random.randn(200) - 4
x2 = np.random.randn(200) - 2
x3 = np.random.randn(200)
x4 = np.random.randn(200) + 2
x5 = np.random.randn(200) + 4

hist_data = [x1, x2, x3, x4, x5]
group_labels = ['X1', 'X2', 'X3', 'X4', 'X5']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.2, 0.1, 0.3, 0.4, 0.3])

pyo.plot(fig)


