import plotly.express as px
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
fig = px.line(x=t, y=np.sin(t))
fig.show()
