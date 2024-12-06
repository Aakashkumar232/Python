                   # Inheritence:-

class parent:
    def _init_(self):
        self.super_attribiute=True
        print("this is parent class:")

class child(parent):
    def _init_(self):
        super()._init_()
        print("this is a child class")
        print(self.super_attribute)


child1=child()


#                 types of inheritence:-

# 1-single inheritence
# 2-multiple inheritence                
# 3-multilevel inheritence
# 4-hierarchical inheritence 
# 5-hybrid inheritence


#                 EXAMPLE:-
class Vehicle:

    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
    
    def get_fare(self):
        return self.seating_capacity*100
    
class Bus(Vehicle):

    def __init__(self,seating_capacity):
        super()._init_(seating_capacity)
    
    def get_fare(self):
        Vehicle_fare = super().get_fare()
        maintenance_fare = 0.1 * Vehicle_fare
        total_fare = Vehicle_fare + maintenance_fare 
        return total_fare
    
Vehicle1=Vehicle(50)
print("vehicle fare:",Vehicle1.get_fare())

bus1=Bus(50)
print("bus fare:",bus1.get_fare())


