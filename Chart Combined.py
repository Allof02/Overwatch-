import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 

df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]]
                           )


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['dva_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['dva_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=1, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_gamewon'], name="Games Won"),
    row=1, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['dva_multikills'], name="MultiKills Best"),
    row=1, col=2, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_objkill'], name="Objective Kills"),
    row=2, col=1, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_winper'], name="Win Percentage"),
    row=2, col=1, secondary_y=True,
)
fig.update_layout(legend_title_text='dVa')
fig.show()


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

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 

df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]]
                           )


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['sig_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['sig_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=1, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_gamewon'], name="Games Won"),
    row=1, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['sig_multikills'], name="MultiKills Best"),
    row=1, col=2, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_objkill'], name="Objective Kills"),
    row=2, col=1, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_winper'], name="Win Percentage"),
    row=2, col=1, secondary_y=True,
)
fig.update_layout(legend_title_text='Sigma')
fig.show()


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 

df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]]
                           )


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['orisa_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['orisa_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=1, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_gamewon'], name="Games Won"),
    row=1, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['orisa_multikills'], name="MultiKills Best"),
    row=1, col=2, secondary_y=True,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_objkill'], name="Objective Kills"),
    row=2, col=1, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_winper'], name="Win Percentage"),
    row=2, col=1, secondary_y=True,
)
fig.update_layout(legend_title_text='Orisa')
fig.show()