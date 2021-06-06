import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig.show()