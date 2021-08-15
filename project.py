import pandas as pd
import plotly.express as px
df = pd.read_csv("covid19.csv")
fig = px.scatter(df,x="date",y="cases",color="country",title="Table in python")
fig.show()