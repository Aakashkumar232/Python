a=56
b=89
c=78
d=56
e=67
x=a%b*c+(b+a)*b+c/d+a
y=56+86-67+89*86+56-45+13
print("enter the number of:",x)
print("enter the vaue of:",y)

print("sum:",4+5)
print("substraction:",4-5)
print("multiplication:",4*3)
print("division:",4%5)
print("floor division:",4//5)
print("modulous:",4%5)
print("exponantial:",4**5)


n1=5                     #Assignment operator
n2=n1
print(n2)
n2+=n1
print(n1,n2)
     
                    #comparison operator
n1=12
n2=9
print(n1>n2)

                        #logical operator
exp1=3>1 #T
exp2=5<4 #F 
print("exp1 and exp2:",exp1 and exp2)#AND
print("exp1 or exp2:",exp1 or exp2)#OR
print("not exp1:",not(exp2))#NOT

                    #identity operator
x=8
y=8
print("if x is y:",x is y)
print("if x is not y:",x is not y)

                         #membership operator 
fruits=["banana","apple","cherry","mango"]
print(" if mango is presents in fruits:","mango"in fruits)
print(" if guava is not presents in fruits:","guava"not in fruits)

                    #bitwise operator
a=5
b=8
print("a and b:",a & b)#AND 
print("a or b:",a | b)#OR
print("a xor b:",a ^ b)#XOR


      
# operator precedence
# highest precedence
#     ()
#    **
#    /,//,%
#     *
#      +,-
# bitwise shift - >>,<<
#                &,|,^
# lowest precedencde
# logical - and ,or,not