# Task 3
import pandas as pd
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

df['strength'] = df['strength'].str.replace(r'\+', '', regex=True).str.replace(r'-.*','', regex=True).astype(float)

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Strength vs. Frequency")
fig.write_html("wind.html", auto_open=True)