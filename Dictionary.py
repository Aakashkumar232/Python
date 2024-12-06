##Dictionary items:-

# 1-ordered
# 2-changable
# 3-unindexed
# 4-duplicates not allowed
# 5-any datatype

# #creating a dictionary

phones={"jhon":567458,"ria":563490,"joy":677887}
print(phones)
print(type(phones))
print(len(phones))
print(phones["jhon"])

#access the phone no of the dictionary
print(phones.get("jhon"))
print(phones.keys())

#update the dictionary 
phones["jhon"]=575889
print(phones)

#add the another variable in dictionary 
phones["kia"]=687439
print(phones)

more_phones={"kia":687439}
phones.update(more_phones)
print(phones)

#remove the element from the dictionary 
phones.pop("jhon")
print(phones)

#remove the last item from the dictionary
phones.popitem()
print(phones)

#empty the all elements from the dictionary 
phones.clear()
print(phones)

#printing values of a dictionary
for x in phones.items():
  print(x)

#nested dictionary
phones={"Area1":{"x":0,"y":1,"z":2},"Area2":{"a":3,"b":4,"c":5}}

print(phones["Area1"]["y"])
print(phones["Area2"]["c"])

        # EXAMPLE:-

# given a dictionary in python, write a python program to find the 
# sum of all items in the dictionary:- 

dict={"a":100,"b":200,"c":300}
print("the sum of dictionary values is:", sum(dict.values()))

         #EXAMPLE:-

input_string=input("enter string:")
n=int(input("enter n:"))

#creating dictionary for mirror oparation
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets=alphabets[::-1]
dict1=dict(zip(alphabets,reverse_alphabets))         

# finding the part of string on which we will do mirror oparation
prefix=input_string[0:n-1]
suffix=input_string[n-1:]

#finding the mirror string 
mirror=""
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]

#creating the final  string
res=prefix+mirror
print("the result is:",res)    