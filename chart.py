import pandas as pd 
import plotly.express as px

df = pd.read_csv('herodata.csv' , ' ')

fig = px.line(df, x = 'CurrentDate' , y = 'elimPerLife', title = 'Zarya Average Elimination Per Life')

fig.show()



