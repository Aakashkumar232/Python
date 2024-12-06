# tuples always identify to immutable which can'nt be change by the another variable. 
# and as well as it always has in order sequence.
     
    #   tuples:-

fruits=("banana","apple","guava","pineapple","peace")
print(len(fruits))
print(type(fruits))

fruits=("banana")
print(fruits[1])
print(fruits[-1])
print(fruits[1:4])
print(fruits[-4:-1])

for i in fruits:
    print(i)

if "guava" in fruits:
    print("it's a part of the fruits list:")
else:
    print("it will not be part of the fruits list:")

#concatenate 2 tuples:-

more_fruits=("grapes","cherry")
fruits=fruits+more_fruits
print(fruits)

#unpacking a tuple:-

fruits1,fruits2,fruits3,fruits4,fruits5=fruits
print(fruits1,fruits2,fruits3,fruits4,fruits5)

    
    # Reverse tuple:-

input_tuple=(1,2,3,4,5,6)
list=[]

##adding reverse values in a list
for x in reversed(input_tuple):
     list.append(x)

output_tuple=tuple(list)
print(output_tuple)
