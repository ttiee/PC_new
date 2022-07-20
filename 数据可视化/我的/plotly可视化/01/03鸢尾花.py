import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="petal_width", y="petal_length")
fig.show()
