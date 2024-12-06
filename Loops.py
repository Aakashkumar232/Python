#for loop 
for i in range(200):
     print(i)

for i in range(1,200):
     print(i) 

list =[1,2,3,4,5]
fruits=["bananna","apple","pineaple"]
for i in fruits:
    print(i)


#while loop

i=1
while(i<35):
    print(i)
    i+=1
    
i=3
while(i<10):
    print(i)
    i+=1     

j=8
while(j<10):
     if(j>7):
        break
     else:
         print(j)
         j=j+1


x=4
y=0
while(x>=0):
    x=x-1
    y=y+1
    if(x==y):
        continue
    else:
        print(x,y)

x=5
y=0
while(x>=0):
    x=x-1
    y=y+1
    if(x==y):
        continue
    else:
        print(x,y)

x=4
y=0
while (x>=0):
    if(x==y):
        break
    else:
        print(x,y)
        x=x-1
        y=y+1




x=78
y=98
while(x<y):
    if(x==y):
        break
    else:
        print(x,y)
        x=x+1
        y=y-1

n=int(input("enter n:"))
for _ in range(n):
    print("*"*5)

     #output:-
#enter n:7
# *****
# *****
# *****
# *****
# *****
# *****
# *****

n=int(input("enter n:"))

for i in range(n):
    for j in range(1,n+1):
      print(j, end="")
    print() 

#     output:-
#enter n:7
1234567
1234567
1234567
1234567
1234567
1234567
1234567

n=int(input("enter n:"))

for i in range(1,n+1):
    for j in range(1,i+1):
      print(j, end="")
    print() 

       #     output:-
       #enter n:7
1
12
123
1234
12345
123456
1234567

n=int(input("enter n:"))

for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()
     
     #output:-
#enter n:7
1
123
12345
1234567
123456789
1234567891011
12345678910111213


