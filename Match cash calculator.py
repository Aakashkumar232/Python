num1=int(input("enter the any number:"))
num2=int(input("enter the any number:"))

operator=input("Enter the any operator:")

match operator:
    case"+":
        print("sum is:",num1+num2)
    case"-":
        print("substraction is:",num1-num2)
    case"*":
        print("product is:",num1*num2)
    case"/":
        print("division is:",num1/num2)
    case"%":
        print("modulous is:",num1%num2)
    case"**":
        print("exponential is:",num1**num2)
    case"^":
        print("XOR is:",num1^num2)
    case"|":
        print("OR is:",num1|num2)
    case"&":
        print("AND is:",num1&num2)

