import matplotlib.pyplot as plt
import get_earthqwake_data as ga

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(ga.time_list, ga.mag_list, c='red', alpha=0.5)
ax.scatter(ga.time_list, ga.mag_list, alpha=0.6)

ax.axes.xaxis.set_ticks([0, 25, 50, 75, 100, 125, len(ga.time_list) - 1])
# ax.axes.xaxis.set_ticklabels([0, 25, 50, 75, 100, 125, len(ga.time_list) - 1])

fig.autofmt_xdate()

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
ax.set_title('一天内全球发生的地震', fontsize=14)
ax.set_xlabel('时间', fontsize=10)
ax.set_ylabel('震级', fontsize=10)

plt.show()
