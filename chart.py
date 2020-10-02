import pandas as pd 
import plotly.express as px

df = pd.read_csv('herodata.csv', ' ')

fig = px.line(df, x = 'current_time' , y = 'elimperlife', title = 'Zarya Average Elimination Per Life')

fig.show()



