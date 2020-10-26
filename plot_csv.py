import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(
    rows=2,
    cols=3,
    subplot_titles=("Eliminations Per Life", "Weapon Accuray","Games Won", "MultiKills Best", "Objective Kills", "Win Percentage")
)


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['dva_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['dva_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=2, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_gamewon'], name="Games Won"),
    row=1, col=3, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['dva_multikills'], name="MultiKills Best"),
    row=2, col=1, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_objkill'], name="Objective Kills"),
    row=2, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['dva_winper'], name="Win Percentage"),
    row=2, col=3, secondary_y=False,
)
fig.update_layout(
    title_text='dVa'
)
fig.layout.update(showlegend=False)
fig.show()



df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(
    rows=2,
    cols=3,
    subplot_titles=("Eliminations Per Life", "Weapon Accuray","Games Won", "MultiKills Best", "Objective Kills", "Win Percentage")
)


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['Zarya_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['Zarya_weaponAcc'], name="Weapon Accuracy"),
    row=1, col=2, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_gamewon'], name="Games Won"),
    row=1, col=3, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['Zarya_multikill'], name="MultiKills Best"),
    row=2, col=1, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_objkill'], name="Objective Kills"),
    row=2, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['Zarya_winper'], name="Win Percentage"),
    row=2, col=3, secondary_y=False,
)
fig.update_layout(title_text='Zarya')
fig.layout.update(showlegend=False)
fig.show()


df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(
    rows=2,
    cols=3,
    subplot_titles=("Eliminations Per Life", "Weapon Accuray","Games Won", "MultiKills Best", "Objective Kills", "Win Percentage")
)


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['sig_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['sig_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=2, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_gamewon'], name="Games Won"),
    row=1, col=3, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['sig_multikills'], name="MultiKills Best"),
    row=2, col=1, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_objkill'], name="Objective Kills"),
    row=2, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['sig_winper'], name="Win Percentage"),
    row=2, col=3, secondary_y=False,
)
fig.update_layout(title_text='Sigma')
fig.layout.update(showlegend=False)
fig.show()




df = pd.read_csv('herodata.csv', ' ')

fig = make_subplots(
    rows=2,
    cols=3,
    subplot_titles=("Eliminations Per Life", "Weapon Accuracy","Games Won", "MultiKills Best", "Objective Kills", "Win Percentage")
)


fig.add_trace(
    go.Scatter(x = df['current_Date'], y= df['orisa_elimperlife'], name="Eliminations Per Life"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y=df['orisa_weaponAccu'], name="Weapon Accuracy"),
    row=1, col=2, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_gamewon'], name="Games Won"),
    row=1, col=3, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x= df['current_Date'], y= df['orisa_multikills'], name="MultiKills Best"),
    row=2, col=1, secondary_y=False,
)


fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_objkill'], name="Objective Kills"),
    row=2, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df['current_Date'], y=df['orisa_winper'], name="Win Percentage"),
    row=2, col=3, secondary_y=False,
)
fig.update_layout(title_text='Orisa')
fig.layout.update(showlegend=False)
fig.show()