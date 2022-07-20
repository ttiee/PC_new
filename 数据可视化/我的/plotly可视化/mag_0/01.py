import plotly.express as px
import plotly
import get_earthqwake_data as ga
import pandas as pd

data = pd.DataFrame(data=zip(ga.x_s, ga.y_s, ga.place_list, ga.mag_list, ga.time_list), columns=['经度', '纬度', '位置', '震级', '时间'])

fig = px.scatter(
    data_frame=data,
    x=ga.x_s,
    y=ga.y_s,
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1400,
    height=700,
    title='过去一个月内全球地震散点图',

    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
    hover_data=['时间']
)

plotly.offline.plot(fig, filename='一天.html')
print('保存成功')
fig.show()

