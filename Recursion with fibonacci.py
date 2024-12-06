         ##  Recursion:-
# a function is called itself is called recursive function.


#Base case and recursive case:-

def factorial(n):
# Base case
    if(n==0):
        return 1
    
# recursive case
    ans=n*factorial(n-1)
    return ans


            #EXAMPLE:-
#find the factorial of any number:-
 
def factorial(n):
    #base case
    if(n==0):
        return 1
    #recursive case
    ans=n*factorial(n-1)
    return ans

n=int(input("enter the n:"))
print(factorial(n)) 
       
            #EXAMPLE:-
#find the sequence in order higher to lower of the any factorial:- 

def print_n_to_1(n):
      #base case
      if(n==0):
            return
      print(n)
      #recursive case
      print_n_to_1(n-1)

n=int(input("enter the any number:"))      
print(print_n_to_1(n))


            #EXAMPLE:-
#find the sequence in order lower to higher of the any factorial:- 

def print_n_to_1(n):
      #base case
      if(n==0):
            return
      #recursive case
      print_n_to_1(n-1)
      print(n)

n=int(input("enter the any number:"))      
print(print_n_to_1(n))

            #EXAMPLE:-
#write a program to print sum from 1 to n.

def sum_1_to_N(n):
    #base case
    if(n==1):
        return 1
    #recursive case
    ans= n + sum_1_to_N(n-1)
    return ans

n=int(input("enter the n:"))
print(sum_1_to_N(n))

           #EXAPMLE:-
#make a function which calculates 'a' raised to the power 'b' using recursion.

def power_a_b(a,b):
    #base case
    if(b==0):
        return 1
    #recursive case
    ans=a*power_a_b(a,b-1)
    return ans
a=int(input("enter a:"))
b=int(input("enter b:"))
print(power_a_b(a,b))

          #EXAMPLE:-
#make a function which calculates fibonacci sequence using recursion.
    
def fibonacci(n):
    #base case
    if(n==1):
        return 0
    elif(n==2):
        return 1
    #recursive case
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
n=int(input("enter n:"))
for i in range(1,n+1):

   print(fibonacci(i))    


                




    
