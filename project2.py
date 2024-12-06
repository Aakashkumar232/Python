# IPL DATA ANALYSIS PROJECT:-

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:\\Users\\Advance Laptop\\Downloads\\archive.zip")
# print(data)

# NUMBER OF MATCHES WON BY EACH TEAM IN IPL 2022:-

# figure = px.bar(data, x = data["match_winner"],title = "Number of matches won in ipl 2022")
# figure.show()

# data["won_by"] = data["won_by"].map({"wickets":"Chasing","Runs":"Defending"})
# won_by = data["won_by"].value_counts()
# label = won_by.index
# counts = won_by.values

# colors = ["red","lightgreen"]

# fig  = go.Figure(data=[go.Pie(labels = label,values = counts)])
# fig.update_layout(title_text = "Number of matches won by defending or chasing")
# fig.update_traces(hoverinfo = "label+percent",textinfo = "value",textfont_size = 30,marker = dict(colors = colors,line = dict(color = "black",width = 3)))
# fig.show()

# figure = px.bar(data["best_bowling"],title = "Best boller in ipl 2022")
# figure.show()

# figure = px.bar(data,x = ["player_of_the_match"],title = "player of the match award")
# figure.show()



  #   TOP SCORER IN IPL 2022:-

# figure = px.bar(data,x = data["top_scorer"], y = data["highscore"],color = data["highscore"],title = "top scorer in ipl 2022")
# figure.show()  