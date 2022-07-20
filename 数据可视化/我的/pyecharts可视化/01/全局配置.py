from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    # Bar(init_opts=opts.InitOpts(theme='dark'))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title='销售量', subtitle='数量'))
)

bar.render('my_echarts01.html')
