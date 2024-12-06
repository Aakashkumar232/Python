 #    sets is also storing multiple value in variable:-
 # sets items:-

# 1-unordered
# 2-immutable
# 3-unindexed
# 4-duplicates not allowed
# 5-any datatype
# 6-mix of different data types

names={"sia","mia","tia"}
print(names)
print(len(names))

for x in names:
    print(x)

if "sia" in names:
     print("it'll be part of the list:")
else:
     print("it will not be part of the list")    

# add element in set

names={"sia","mia","tia"} 
names.add("ria")
print(names)

# add another variable sequence in set 

names={"sia","mia","tia"} 
names_list=["jia","kia"]
names.update(names_list)
print(names)

# removing elements from a set
names={"sia","mia","tia"} 
names.remove("ria")
print(names)


# joining 2 sets
s1={"a","b","c"}
s2={"d","e","a"}
print(s1,s2)
s3=s1.union(s2)
print(s3)
s1.update(s2)
print(s1)

# keep only duplicates while joining
s1.intersection_update(s2)
print(s1)
# keep all values except duplictes
s1.symmetric_difference_update(s2)
print(s1)


# solving the questio:-
#given three arrays, we have to find common elements in three
#sorted lists using sets.

l1=[1,5,5,10]
l2=[3,4,5,5.10]
l3=[5,5,10,20]

#typecasting into sets

s1=set(l1)
s2=set(l2)
s3=set(l3)

#join using intersection_update
s1s2=s1.intersection(s2)
final_set=s1s2.intersection(s3)

final_list= list(final_set)
print(final_list)