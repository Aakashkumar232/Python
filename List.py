#list has always mutable which can change the anytime by the any variable. 
#and as well as it's not be order sequence.  

        # list items-

# 1-indexed
# 2-ordered
#3-duplicates allowed
#4-any datatype
#5-mix of different data types

fruits=["apple","banana","cherry"]
print(fruits)
print(type(fruits))
print(len(fruits))

#now we can check the any element present in list or not   "
if("apple" in fruits):
    print("it fruit is a part of the list:")
else:
    print("it fruit is not a part of the list:") 
      
#Accessing items of a list-

# 1-indexing
# 2-negative indexing
# 3-range of indexes
# 4-range of negative indexes

#         (0)     (1)       (2)      (3)         (4)       -:forward indexing
fruits=["apple","banana","cherry","pineapple","papaya"]
#        (-5)     (-4)     (-3)      (-2)        (-1)       -:reverse indexing

print(fruits[0])  
print(fruits[1])
print(fruits[2])
print(fruits[-2])
print(fruits[-1])  
print(fruits[-4:-1])
print(fruits[-4:-2])
print(fruits[-4:-3])  


#Adding element to a list 
#appened()
#insert()
#extend()

fruits=["apple","banana","cherry","pineapple"]
fruits.append("kiwi")  
print(fruits)
fruits.insert(3,"guawa")
print(fruits)
more_fruits=("chilly","mango")
fruits.extend(more_fruits)
print(fruits)


#removing element from a list
#remove()
#pop()

list=[10,20,40,50,60,70]
#60 will be remove from the list 
list.remove(60)
print(list)

#indexing 1 elemnet will be delete from the list  
list.pop(1) 
print(list)

#last element will be delete from the list
list.pop()
print(list)


#changing item in a list 
#at index
#in a range

list=[20,34,40,50,60]
list[1]=30
print(list)
list[2]=70
print(list)

#sorting a list
#Ascending
#Descending 
list=[20,34,40,50,60]
list.sort() #Ascending order of the list
print(list)

list.sort(reverse=True)#Descending of the list
print(list)

list.reverse()#Ascending order of the list 
print(list)

#list comprehension
fruits=["apple","banana","cherry","pineapple"]
new_fruits=[fruits for fruits in fruits if "a" in fruits]
print(new_fruits)

 #copy a list
new_fruits=fruits.copy()
print(new_fruits)

new_fruits=fruits+new_fruits
print(new_fruits)

   # nested list
fruits=["apple","banana","cherry","pineapple"]
fruits.insert(2,["guava","mango"])
print(fruits)
print(fruits[2][0])

#solve a given list python and provided the index
#of the elements, write a program to swap the two
#elements in the list

# examples swapping th list

n=int(input("enter the size of list:"))
list=[]
for i in range(n):
    num=int(input())
    list.append(num)

index1=int(input("enter the index:"))
index2=int(input("enter the index2:"))
print(list)

#swapping values at index1 and index2
temp=list[index1]            
list[index1]=list[index2]
list[index2]=temp
print(list)



#same example but different method
list=[34,78,89,45]
index1=0
index2=2
#swapping values at index1 and index2
temp=list[index1]
list[index1]=list[index2]
list[index2]=temp
print(list)
