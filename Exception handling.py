#exception handling:-

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))

try:
    result=a/b

except ZeroDivisionError:    
    result = None
    print("Error: cannot divide by zero")

finally:
    print("Division oparation completed:",result)    