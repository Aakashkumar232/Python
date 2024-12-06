## replace() string:- replace old substring with new substring count no. of times.

#replace substring
str1="Hello world, what a beautiful world this is!"
print(str1.replace("world","earth",))
print(str1.replace("world","earth",1))

       #split() string:- used to split the string into a list of substrings.

# splitting string 
str1="what's your good name" 
list=str1.split()
print(list)

str1="ria,mia,sia,tia" 
list=str1.split(",",2)
print(list)

#concatenation of the dtreing 
str1="Hello world!"
str2="what a great place this is."
print(str1+str2)

        #foramt() strin:- used to insert variable values in a string.

#string formatting
student_name="Aakash"
student_marks=99

str1="the student name is {s}, and marks is {n}".format(s = student_name, n=student_marks)
print(str1)



text = "the unexpected always happens"
print(text)
print(len(text))
print(text.find('pp'))
print(text[:11])
print(text.replace('always','never'))
text2=" no matter what"
new_text=text+text2
print(new_text)
  

         ## plindrome()string:-

def check_plindrome(str):
    #cleaning the string
     clean_str=(str.replace("","")).lower()
     reverse_str=clean_str[::-1]
     return clean_str==reverse_str    
str='abccba'
if check_plindrome(str):
     print("it is a plindrome string")
else:
     print("not a plindrome")     


      