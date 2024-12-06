## class constructor:- special function that gets involved every time an
#object is created for that class.

class Rectangle:

    def __init__(self,height,width):
        print(f"A rectangle is created with height:{height} and width:{width}")
        self.height=height
        self.width=width

    def set_dimension(self,height,width):
         self.height=height
         self.width=width
        

    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)

    #creating objects
rectangle1 = Rectangle(4,3)
rectangle2 = Rectangle(5,7)
rectangle3 = Rectangle(2,8)

#                 #Attributes:-

class student:

    def set_name(self,name):
        self.name=name  #class attributes

    def get_name(self):
        return self.name
    
student1=student()
student1.set_name("shahnaaz")
print(student1.get_name())
student1.eng_marks=45  #instances attributes
print(student1.eng_marks)

student2=student()
student2.set_name("parag")
print(student2.get_name())



            ## Access modifier:-

# 1-public modifier
# 2-protected modifier
# 3-private modifier

                #public modifier:-when using the single underscore after def function.

class ABC:
    def _init_(self):
        self.public_attribute=None #public attribute

    def public_function(): #public function
        pass



             #private modifier:- when using the double underscore after def function.


class ABC:
    def __init__(self):
        self.public_attribute=10 #private attribute

    def __public_function(): #private function
        pass

 
             #protected modifier:-

class ABC:
    def __init__(self):
        self.public_attribute=10 #protected attribute

    def _public_function(): #protected function
        pass

