import seaborn as sns
import matplotlib.pyplot as plt

# var = [1,2,3,4,5,6,7,8]
# var1 = [8,7,6,5,4,3,2,1]

# sns.lineplot(x = var,y = var1)
# plt.show()


# import pandas as pd
# var = [1,2,3,4,5,6,7,8]
# var1 = [8,7,6,5,4,3,2,1]
 
# df = pd.DataFrame({"var":var,"var1":var1})
# print(df)


# import pandas as pd
# var = [1,2,3,4,5,6,7,8]
# var1 = [8,7,6,5,4,3,2,1]

# df = pd.DataFrame({"var":var,"var1":var1})
# sns.lineplot(x = "var",y = "var1", data = df)
# plt.show()

#     #    NOW DATA SET WILL BE THE PRINTED:-

# df1 = sns.load_dataset("penguins")
# print(df1)

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df1)
# plt.show()

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df1,hue = "sex")
# plt.show()

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df1,hue = "sex", palette = "rocket_r")
# plt.show()

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df1,hue = "sex",style = "sex", palette = "rocket_r",markers = ["o",">"])
# plt.show()

     

#     #  NOW TAKEN THE SOME DATA FROM THE PENGUINS TABLE:-

# df2 = sns.load_dataset("penguins").head(20)

# print(df2)

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df2,hue = "sex",style = "sex", palette = "rocket_r",markers = ["o",">"])
# plt.show()

# sns.lineplot(x = "bill_depth_mm",y = "flipper_length_mm", data = df2,hue = "sex",style = "sex", palette = "rocket_r",markers = ["o",">"])

# plt.title("penguins chart")
# plt.grid()
# plt.show()


#     #   -:SECOND DAY OF THE SEABORN LIBRARY:-


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

df3 =  sns.load_dataset("penguins")

# sns.barplot(x = df3.island, y = df3.bill_length_mm)
# plt.show()

# sns.barplot(x = "island",y = "bill_length_mm",data = df3, hue = "sex")
# plt.show()

# order1 = ["Dream","Torgersen","Biscoe"]
# sns.barplot(x = "island",y = "bill_length_mm",data = df3, hue = "sex",order = order1 )
# plt.show()



#     #  HUE ORDER MEANS INTERCHANGE THE COLOR OF MALE AND FEMALE AND AS WELL AS CATAGORIES TO THE MALE OR FEMALE BY THE COLOR :-

# order1 = ["Dream","Torgersen","Biscoe"]
# sns.barplot(x = "island",y = "bill_length_mm",data = df3, hue = "sex",order = order1, hue_order = ["female","male"])
# plt.show()


#           #NOW CHANGE THE COLOR:-

# order1 = ["Dream","Togersen","Biscoe"]
# sns.barplot(x = "island", y = "bill_length_mm",data = df3, color = "pink")
# plt.show()

# order1 = ["Dream","Togersen","Biscoe"]
# sns.barplot(x = "island", y = "bill_length_mm",data = df3, color = "red")
# plt.show()


# sns.barplot(x ="island", y = "bill_length_mm",data = df3, hue= "sex",palette = "rocket")
# plt.show()


# sns.barplot(x ="island", y = "bill_length_mm",data = df3, hue= "sex",palette = "rocket",saturation = 2)
# plt.show()


#            # HISTOGRAM IN SEABORN LIBRARY:-

sns.histplot(df3["flipper_length_mm"])   
plt.show()        

sns.displot(df3["flipper_length_mm"], bins = [170,180,190,200,210,220,230,240])
plt.show()

sns.displot(df3["flipper_length_mm"], bins = [170,180,190,200,210,220,230,240],color = "red")
plt.show()

sns.displot(df3["flipper_length_mm"], bins = [170,180,190,200,210,220,230,240],kde = True,color = "red")
plt.show()