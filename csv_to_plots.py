import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load csv files
tyo = pd.read_csv('AQHI of Tokyo.csv')
ldn = pd.read_csv('AQHI of London.csv')
bj = pd.read_csv('AQHI of Beijing.csv')
la = pd.read_csv('AQHI of Los Angeles.csv')
mos = pd.read_csv('AQHI of Moscow.csv')
wash = pd.read_csv('AQHI of Washington.csv')
par = pd.read_csv('AQHI of Paris.csv')
bsn = pd.read_csv('AQHI of Busan.csv')
trt = pd.read_csv('AQHI of Toronto.csv')
van = pd.read_csv('AQHI of Vancouver.csv')

# Initialize subplots
fig = make_subplots(
    rows=2,
    cols=5,
    subplot_titles=(
        "")
)

# Add subplots
fig.add_trace(
    go.Scatter(x=tyo['Date'], y=tyo['AQHI'], name="AQHI of Tokyo"),
    row=1, col=1, secondary_y=False
)

fig.add_trace(
    go.Scatter(x=ldn['Date'], y=ldn['AQHI'], name="AQHI of London"),
    row=1, col=2, secondary_y=False
)

fig.add_trace(
    go.Scatter(x=la['Date'], y=la['AQHI'], name="AQHI of Los Angeles"),
    row=1, col=3, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=wash['Date'], y=wash['AQHI'], name="AQHI of Washington"),
    row=1, col=4, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=bj['Date'], y=bj['AQHI'], name="AQHI of Beijing"),
    row=1, col=5, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=bsn['Date'], y=bsn['AQHI'], name="AQHI of Busan"),
    row=2, col=1, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=trt['Date'], y=trt['AQHI'], name="AQHI of Toronto"),
    row=2, col=2, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=van['Date'], y=van['AQHI'], name="AQHI of Vancouver"),
    row=2, col=3, secondary_y=False
)
fig.add_trace(
    go.Scatter(x=par['Date'], y=par['AQHI'], name="AQHI of Paris"),
    row=2, col=4, secondary_y=False
)

fig.add_trace(
    go.Scatter(x=mos['Date'], y=mos['AQHI'], name="AQHI of Moscow"),
    row=2, col=5, secondary_y=False
)

fig.update_layout(
    title_text='AQHI'
)
fig.layout.update(showlegend=True)
fig.show()
