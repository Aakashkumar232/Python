#polymorphism:- many forms to allows objects of differents to behave as objects 
# of the same superclass.

class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
   def speaks(self):
       print("barks")
class Cat(Animal):
    def speaks(self):
        print("meow")
class Cow(Animal):
    def speaks(self):
        print("mooo") 
dog=Dog()
cat=Cat()
cow=Cow()

dog.speaks()
cat.speaks()
cow.speaks()
       

#            # types of the polymorphism:-
# 1-run time polymorphism
# 2-compile-time polymorphism           


         #compile-time polymorphism:-
#method overloading:-

class Add:
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print(a+b+c)     

#oparetor overloading:-

class complexNumber:
    def _init_(self,real,img):
        self.real=real
        self.img=img

    def _add_(self,other):
        return complexNumber(self.real+other.real,self.img+other.img)
    
    

c1=complexNumber(1,2)
c2=complexNumber(3,4)
c3=c1+c2
print(c3.real,"+i",c3.img)

            #run time polymorphism:-

class Animal:
    def speak(self):
        print("generic noise")
    
class Dog(Animal):
   def speaks(self):
       print("barks")
class Cat(Animal):
    def speaks(self):
        print("meow")
class Cow(Animal):
    def speaks(self):
        print("mooo") 
dog=Dog()
cat=Cat()
cow=Cow()

dog.speaks()
cat.speaks()
cow.speaks()


#Abstraction:-






#encapsulation:-
              

