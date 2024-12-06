        ## string():- 
# string is a sequence of character as well as immutable. 

#using single quote:- 'HELLO, WORLD!'
#using double quote:-  "HELLO WORLD"
#using triple qoute:-  '''HELLO WORLD''' 


name1='collage wallah'
name2="physics wallah"
name3='''MBA wallah'''
print(name1,name2,name3)
print(type(name1)) 
print(type(name2))
print(type(name3))      

name1='collage wallah'
print(name1[1])
print(name1[5:-1])
print(name1[-6:-2])
print(name1[0:8])


#traverse the string
name1='collage wallah'
for i in name1:
    print(i)

#using list comprehension
name1='collage wallah'
list=[char for char in name1 ]
for i in list:
    print(i)


name1='collage wallah'
print(len(name1))
print(name1.find('g'))
print(name1.find('a'))
print(name1.replace("collage","school"))
print(name1.replace("wallah","allah"))

