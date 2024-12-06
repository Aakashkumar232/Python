num=int(input("enter the value by Aakash:"))
if(num>44):
   print("it will be positive:-")
elif(num<44):
   print("then it will be eqaul to the another value:-")
else:
   print("otherwise it will be negative:-") 

#        #SOME ADVANCE

num=int(input("enter the any no"))
if(num>45):
   print("then number will be positive")
elif(num<45):
   if(num>45):
       print("then number will be special")
   elif(num<45):
       print("then number will be super")
   else:
       print("then number above of the super")
else:
   print("then number will be negative")        
    

cp=int(input("enter the coast price:"))
sp=int(input("enter the selling price:"))
if(sp>cp):
   profit=sp-cp
   print("then we will get the profit:",profit)
elif(sp<cp):
   loss=cp-sp
   print("then we will get the loss:",loss)
else:
  print("otherwise profit and loss will be equal:")    
             
             #EXAMPLE:-
marks=float(input("enter the marks:"))
#if marks are above of the 81
if(marks>81):
   print("it will be very good student:")
#if marks are above of 61 
elif(marks>61):
   print("it will be good student:")
elif(marks>41):
    print("it will be everage student:")
#if marks are above of the 21      
else:
    print("otherwise it will be fail:")
        
                 #EXAMPLE:-

english_marks=int(input("enter the english marks:"))
math_marks=int(input("enter the math marks:"))
#if both marks english and hindi more then 80 then we can get the a grade
if(english_marks>80 and math_marks>80):
    print("we can get the A grade:")
# if either marks english and hindi more then 80 then we can get the b grade
elif(english_marks>80 or math_marks>80):
    print("we can get the B grade:")
#if neither marks english and hindi more then 80 then we can get the c grade    
else:
    print("we can get the C grade:")
    
                #EXAMPLE:-

n1=int(input("enter the number n1:"))
n2=int(input("enter the number n2:"))
n3=int(input("enter the number n3:"))

if(n1>n2 and n1>n3):
    print(n1,"is the greatest number:")
elif(n2>n1 and n2>n3):
    print(n2, "is the greatest number:")
else:
    print(n3,"is the greatest number:")      

                #EXAMPLE:-

number=75
if(number>80):
    print("it will be positive:")
elif(number<80):
    if(number>80):
        print("special number:")
    elif(number<80):
        print("it will be Aakash:")
    else:
        print("it will be negative:") 
else:
    print("it will be vikas:")     

                #EXAMPLE:- 

num=int(input("enter the any positive number:"))
if(num%15==0):
    print("it will be positive:")
else:
     if(num%3==0 or num%5==0):
          print("number is not divisible by 15 but divisible by 3 or 5:")
     else:
          print("number is neither divisivle by 3 nor 5:")         
    