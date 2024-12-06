# EMPOLYEE CAREER SURVEY ANALYSIS:-

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:\\Users\\Advance Laptop\\Downloads\\Career Aspirations survey of GenZ.csv")
# print(data.head())


#    what is the analysis of the country with the help of the visualization:-


country = "Your Current Country."
country = data[country].value_counts()
print(country)

label = country.index
counts = country.values
colors  = ["red","lightgreen"]
fig = go.Figure(data = [go.Pie(labels = label,values = counts)])
fig.update_layout(title_text = "-:Current Country:-")
fig.update_traces(hoverinfo = "label+value",textinfo = "percent",textfont_size = 30,marker = dict(colors = colors,line =dict(color = "black",width = 3 )))

fig.show()


#     what are the factor influencing the career aspiration of genz with visualizationz:-


# question1 = "Which of the below factors influence the most about your career aspirations ?"
# question1 = data[question1].value_counts()
# print(question1)

# label = question1.index
# counts = question1.values
# colors = ["yellow","green"]
# fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
# fig.update_layout(title_text = "-:Factors influencing career inspirations:-")
# fig.update_traces(hoverinfo = "label+value",textinfo = "percent",textfont_size = 30,marker = dict(colors = colors,line = dict(color = "black",width = 3)))

# fig.show()
 

#     how many want to pursue higher education outside india with their investment with visualization:-


# question2 = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
# question2 = data[question2].value_counts()
# # print(question2)

# label = question2.index
# counts = question2.values
# colors = ["yellow","green"]
# fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
# fig.update_layout(title_text = "-:higher education outside india with their investment:-")
# fig.update_traces(hoverinfo = "label+value",textinfo = "percent",textfont_size = 30,marker = dict(colors = colors,line = dict(color = "black",width = 3)))

# fig.show()


#     how likly genz is to work for one company for three years or more with visualization:-


# question3 = "How likely is that you will work for one employer for 3 years or more ?"
# question3 = data[question3].value_counts()
# # print(question3)

# label = question3.index
# counts = question3.values
# colors = ["yellow","green"]
# fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
# fig.update_layout(title_text = "-:genz is to work for one company for three years or more:-")
# fig.update_traces(hoverinfo = "label+value",textinfo = "percent",textfont_size = 30,marker = dict(colors = colors,line = dict(color = "black",width = 3)))

# fig.show()


#  what is the preferred working environment of the genz with visualization:-


# question4 = "What is the most preferred working environment for you."
# question4 = data[question4].value_counts()
# # print(question4)

# label = question4.index
# counts = question4.values
# colors = ["yellow","green"]
# fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
# fig.update_layout(title_text = "-:preferred working environment of the genz:-")
# fig.update_traces(hoverinfo = "label+value",textinfo = "percent",textfont_size = 30,marker = dict(colors = colors,line = dict(color = "black",width = 3)))

# fig.show()

