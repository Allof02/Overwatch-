import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 

df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]]
                           )


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['Zarya_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['Zarya_weaponAcc'], name="Weapon Accuracy"),
    row=1, col=1, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_gamewon'], name="Games Won"),
    row=1, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['Zarya_multikill'], name="MultiKills Best"),
    row=1, col=2, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_objkill'], name="Objective Kills"),
    row=2, col=1, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_winper'], name="Win Percentage"),
    row=2, col=1, secondary_y=True,
)
fig.update_layout(legend_title_text='Zarya')
fig.show()