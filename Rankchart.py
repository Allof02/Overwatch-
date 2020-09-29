import pandas as pd 
import plotly.express as px

df = pd.read_csv('DoomfistDamage.csv' , ' ')

fig = px.line(df, x = 'CurrentDate' , y = 'elimPerLife', title = 'Average Elimination Per Life')

fig.show()



