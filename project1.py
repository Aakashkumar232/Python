             # I PHONE SALES ANALYSIS:-

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("c:\\Users\\Advance Laptop\\Downloads\\apple_products.csv")
# print(data)

    #    CHECK THE MISSING VALUE FROM THE DATA SET:-

# print(data.isnull().sum()) 

    #    STATISTICAL DATA OF THE DATA SET:-

# print(data.describe())

    #    TOP 10 I PHONE SALES ANALYSIS IN INDIA:-
       
# highest_rated = data.sort_values(by = ["Star Rating"],ascending = False)
# highest_rated = highest_rated.head(10)
# print(highest_rated["Product Name"])   


# highest_rated = data.sort_values(by = ["Number Of Reviews"],ascending = False)
# highest_rated = highest_rated.head(10)
# print(highest_rated["Product Name"])



        #  HOW MUCH TOTAL NUMBER OF THE PRODUCT WITH GRAPH:- 
                #   BASED ON NUMBER OF RATINGS:-

# highest_rated = data.sort_values(by = ["Star Rating"],ascending = False)
# highest_rated = highest_rated.head(10)
# iphones = highest_rated["Product Name"].value_counts()
# print(iphones)
# labels = iphones.index
# counts = highest_rated["Number Of Ratings"]
# figure = px.bar(highest_rated, x= labels, y= counts, title = "Number of Ratings Highest Rated I Phone")
# figure.show()


                #  BASED ON NUMBER OF REVIEWS:-

# highest_rated = data.sort_values(by = ["Star Rating"],ascending = False)
# highest_rated = highest_rated.head(10)
# iphones = highest_rated["Product Name"].value_counts()
# # print(iphones)
# labels = iphones.index
# counts = highest_rated["Number Of Reviews"]
# figure = px.bar(highest_rated, x= labels, y= counts, title = "Number of Reviews Highest Rated I Phone")
# figure.show()



# figure = px.scatter(data_frame = data, x = "Number Of Ratings",y = "Sale Price",size = "Discount Percentage",trendline = "ols", title = "Relationship between sale price and number of ratings")
# figure.show()

# figure = px.scatter(data_frame = data, x= "Number Of Ratings",y = "Discount Percentage",size = "Sale Price",trendline = "ols",title= "Relationship between discount percentage and number of ratings")
# figure.show()