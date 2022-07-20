import plotly.express as px

df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", color="continent", size='pop', hover_name="country",
                     projection='natural earth')
fig.show()
