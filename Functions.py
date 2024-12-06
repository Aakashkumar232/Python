## function:-
# 1-what and why ?
# 2-types of function
# 3-creating a function
# 4-calling a function
# 5-arguments
# 6-types of arguments
# 7-difference between parameters and arguments
# 8-return type
# 9-nested functions
# 10-pass by value and pass by reference
# 11-built-in function

      #1-what and why:- they are reusable code that perfoms a specific task. 
 
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    sum+=i

print("sum of all numbers till n is:",sum)

n1=int(input("enter the another n:"))
sum1=0
for i in range(1,n+1):
    sum1+=1
    print("sum of all numbers til n is:",sum1)


         ##Types of functions:-
# 1-built in:-
print("hello world")


# 2-user defined:-
num=int(input("enter the any number:"))


         #creating a function:-
# def printHello():
print("Hello world!!")

#calling a function:-   
print()

         #Types of arguments:-

# 1-Default arguments
# 2- keyword arguments(named argumnets)
# 3- positional arsguments
# 4-arbitrary arguments(variable-lenght argumnets*args and**kwargs)

         #1-default arguments:-
# function which takes 2 numbers as input and returns their sum
# where n1 , n2 is parameters and x,y is arguments

           #positional arguments:-
def add(n1,n2): 
    print("n1:",n1)
    print("n2:",n2)
    sum = n1+n2
    return sum


x = 2
y = 3 
print("the sum is", add(2,3))

           #keyword arguments:-
print("the sum is:", add(n2=2, n1=3))

            # default arguments:-
print("the sum is",add())

            #arbitrary arguments:-
def addallnumbers(*args):
    sum=0
    for i in args:
        sum+=i
        return sum
output=addallnumbers(1,2,3,4,5)
print("the sum is",output)      

def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)
studentinfo(name="urvi",age=33,city="delhi")
studentinfo(name="ria",age=40,city="banglore")   
     

           ## pass by value and pass by reference:-

#(1):-     pass by value(immutable objects strings,integers,float,tuples) 
#when passed to function, a copy of the object is created and aassigned to local 
#variable in function.
#any change made to them in size function,do not affect the original varibale
#outside function. 

#(1)pass by value

def addOne(x):
    x=x+1
    print("inside function:",x)


x=5
addOne(x)
print("outside function:",x)

#(2):-   pass by reference(mutable objects-list,dictionary) a refernce to actual
#objects is passed to function changes inside function will affects original objects.

#pass by reference 
def modifyList(lst):
    lst.append(4)
    print("inside functin:",lst)

lst=[1,2,3]
modifyList(lst)
print("outside function:",lst)    
    


        ## built-in function
#abs()	Returns the absolute value of a number
#all()	Returns True if all items in an iterable object are true
#any()	Returns True if any item in an iterable object is true
#ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
#bin()	Returns the binary version of a number
#bool()	Returns the boolean value of the specified object
#bytearray()	Returns an array of bytes
#bytes()	Returns a bytes object