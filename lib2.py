import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df)
print(df.head())
print(df.tail())
print(df.head(10))
print(df.tail(10))

print(df.dtypes)
print(df.describe())
print(df[['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']])
print(df.info())
print(df.dtypes == "object")
print(df.dtypes == "float64")
print(df[df.dtypes[df.dtypes == "float64"].index])
print(df[df.dtypes[df.dtypes == "int64"].index])
print(df.columns)
print(df[["Ticket"]])
print(df[["Ticket"]][4:16])
print(df[["Ticket"]][4:16:2])
print(df[["Ticket","Cabin"]][4:16:3])

df['new_col'] = "burger"
print(df.head(10))

print(df.insert(loc = 3, column = "food", value = "pizza"))
print(df.head(10))


print(df["Name"][0:10])
print(type(df["Name"][0:10]))

a = df["Name"][0:10]
l = ["swati","a1","a2","a3","a4","a5","a7","a8","a9","a10"]
print(pd.Series(a,index = l))
print(pd.Series(list(a),index = l))

   #CONCATENATE FOR THE M1 AND M2:-

m1 = pd.Series([100,200,300,400,500], index = [1,2,3,4,5])
m2 = pd.Series([600,700,800,900,1000], index = [1,2,3,4,5])
m3 = pd.concat([m1,m2])
print(m3)

     
   #MULTIPLICATION FOR THE M1 AND M2:-
m1 = pd.Series([100,200,300,400,500], index = [1,2,3,4,5])
m2 = pd.Series([600,700,800,900,1000], index = [1,2,3,4,5])
m3 = m1*m2
print(m3)

   #  ADDITION FOR THE M1 AND M2:-

m1 = pd.Series([100,200,300,400,500], index = [1,2,3,4,5])
m2 = pd.Series([600,700,800,900,1000], index = [1,2,3,4,5])
m3 = m1+m2
print(m3)
    
        # DROP AND DELETE THE DATA FROM THE TABLE;-

   
print(df.drop("PassengerId",axis = 1))                 # passenger id column will not be parmanently deleted from the table.
df.drop("Survived", axis = 1, inplace = True)          # survived column will be parmanently deleted from the table.
print(df)

print(df.drop(3))                                      # third row will be deleted but not parmanently.
print(df.drop(3,inplace = True))                       # third row will be deleted parmanently.
print(df)

print(df.set_index("Name"))                            # name will be set in first column of the table but not set parmanently. 
print(df.set_index("Name",inplace = True))             # name will be set in first column of the table but set parmanently. 
print(df)

print(df.reset_index())


         # MAKE IN DATAFRAME FROM THE DICTIONARY:-

d = { "key1" :[1,2,3,4,5],
      "key2" :[6,7,8,9,10],
      "key3" :[11,12,13,14,15]}   
print(d)      
 
print(pd.DataFrame(d)) 



print(df.dropna())                                   # blank column will be deleted from the table.
df.dropna(inplace = True)                            # blank column will be deleted from the table parmanently.
print(df)

print(df.fillna("swati"))                                   # change the name of any column 








