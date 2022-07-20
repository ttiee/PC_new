import plotly.graph_objs as go
import plotly
from plotly.offline import init_notebook_mode, iplot
import numpy as np


init_notebook_mode(connected=True)
# 生成数据
N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# 构造trace，绘制散点图
trace = go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers'
)
data = [trace]

layout = go.Layout(title='测试',
                   titlefont={
                       'size': 20,
                       'color': '#9ed900'
                   })

fig = go.Figure(data=data, layout=layout)
# fig = dict(data=data, layout=layout)
iplot(fig)