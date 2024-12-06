#object oriented programing:-

# is a programing paradism where the software design revolves around objects
# or data rather then function.

# OOPS in python:-

# helps to mimic real world entities & their interaction.
# code reusing
# organization and maintainbility of code

            #print the namew with the help of class function:-

class student:

    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
student1=student()
student1.set_name("shahnaaz")
print(student1.name)    


        #rectangle of area with perimeter:-

class rectangle:

    def set_dimension(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2*(self.height+self.width)

    #creating objects
rectangle1 = rectangle()
rectangle1.set_dimension(4,3)
print("the height and width are:",rectangle1.height,rectangle1.width)    
print("the area is:",rectangle1.area())
print("the perimeter is:",rectangle1.perimeter())

             
