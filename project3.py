#  NETFLIX STOCK ANALYSIS PROJECT:-

import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

data = pd.read_csv("C:\\Users\\Advance Laptop\\Downloads\\archive (1)\\NFLX.csv")
# print(data.head())


# data["Date"] = pd.to_datetime(data["Date"])
# data = data.set_index("Date")
# print(data.head())



                   # FIND THE TOP 5 DATA IN A TABLE:-


# a =data.sort_values(by = "High",ascending = False).head()
# print(a)


# FIND THE LOWER 5 DATA IN A TABLE:-

# b =data.sort_values(by ="Low", ascending =True).head()
# print(b)



                   #   WITH THE HELP OF THE VISUALIZATION:-


# fig,axis = plt.subplots(nrows = 1,ncols = 2,sharex = True,figsize =(12,5))
# fig.suptitle("High & Low values stock per period of time",fontsize = 18)
# sns.lineplot(ax =axis[0],y= data["High"],x =data.index,color = "green")
# plt.show()


# fig,axis = plt.subplots(nrows = 1,ncols = 2,sharex = True,figsize =(12,5))
# fig.suptitle("High & Low values stock per period of time",fontsize = 18)
# sns.lineplot(ax =axis[0],y= data["High"],x =data.index,color = "green")
# sns.lineplot(ax = axis[1],y = data["Low"],x = data.index,color = "red")
# plt.show()
              

# data.plot(x = 'Date', y = 'Volume')
# plt.title("volume of the stock")
# plt.show()


# data.plot(x='Date', y=['High', 'Close', 'Open'])
# plt.title('Netflix Stock Price')
# plt.show()



# fig,(ax1,ax2,ax3) = plt.subplots(3, figsize = (15,10))
# data.groupby(data.index.day).mean().plot(y = "Volume",ax = ax1, xlabel = "Day")
# data.groupby(data.index.month).mean().plot(y = "Volume",ax = ax2, xlabel = "month")
# data.groupby(data.index.year).mean().plot(y = "Volume",ax = ax3, xlabel = "year")
# plt.show()


