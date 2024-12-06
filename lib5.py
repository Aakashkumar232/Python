import plotly.express as px


# x = [1,2,3,4,5,6,7,8,9,10]
# y = [5,6,7,8,9,23,4,5,6,3]

# fig = px.bar(x = x,y=y ,title = "bar graph")
# fig.show()


# x = [1,2,3,4,5,6,7,8,9,10]
# y = [5,6,7,8,9,23,4,5,6,3]

# fig = px.line(x = x,y=y ,title = "line graph")
# fig.show()


# import plotly.graph_objects as go

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [5,6,7,8,9,23,4,5,6,3]

# fig = go.Figure(go.Scatter(x=x,y=y))
# fig.show()


    #   ADDING TITLE OR NAME OF THE GRAPH:-

# import plotly.graph_objects as go

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [5,6,7,8,9,23,4,5,6,3]

# fig = go.Figure(go.Scatter(x=x,y=y))
# fig.update_layout(title = "line graph",xaxis_title = "this is x axis",yaxis_title = "this is y axis")
# fig.show()      


# import plotly.graph_objects as go

# x1,y1 = [1,2,3,4,5],[6,7,8,9,10]
# x2,y2 = [1,2,3,4,5],[4,3,6,2,1]
# x3,y3 = [1,2,3,4,5],[6,7,8,9,10]

# fig = go.Figure()
# fig.add_trace(go.Scatter(x = x1,y= y1))
# fig.add_trace(go.Scatter(x = x2,y= y2))
# fig.add_trace(go.Scatter(x = x3,y= y3))
# fig.show()


# import plotly.graph_objects as go

# x1,y1 = [1,2,3,4,5],[6,7,8,9,10]
# x2,y2 = [1,2,3,4,5],[4,3,6,2,1]
# x3,y3 = [1,2,3,4,5],[6,7,8,9,10]

# color = "green","yellow","black"
# fig = go.Figure()
# fig.add_trace(go.Scatter(x = x1,y= y1,name = "line1",mode = "lines"))
# fig.add_trace(go.Scatter(x = x2,y= y2,name ="line2",mode ="markers"))
# fig.add_trace(go.Scatter(x = x3,y= y3,name ="line3",mode = "lines + markers"))
# fig.show()


#         #    BUBBLE CHARTS:-


# import plotly.graph_objects as go

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]

# fig = go.Figure(go.Scatter(x = x,y = y,mode = "markers",marker_size = [40,60,70,80,90]))
# fig.show()


# import plotly.graph_objects as go

# x = [1,2,3,4,5]
# y = [6,7,8,9,10]

# fig = go.Figure(go.Scatter(x = x,y = y,mode = "markers",marker_size = [40,60,70,80,90],text = ["product A","product B","product C","product D","product E"]))
# fig.show()



# import matplotlib.pyplot as plt

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [7,3,4,5,4,8,9,2,1,11]

# plt.plot(x,y,color = "red")
# plt.title("line plot")
# plt.show()


# import matplotlib.pyplot as plt
# import seaborn as sns

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [7,3,4,5,4,8,9,2,1,11]

# sns.lineplot(x = x,y = y , color = "black")
# plt.title("line plot")
# plt.show()

