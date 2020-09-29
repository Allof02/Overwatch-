import pandas as pd 
import plotly.express as px

df = pd.read_csv('DoomfistDamage.csv')

fig = px.line(df, x = 'CurrentTime' , y = 'Rank', title = 'RankChart')

fig.show()