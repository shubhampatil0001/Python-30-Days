#Abstract class and abstract method in python

from abc import ABC, abstractmethod

class vehicle(ABC): #abstract class
    
    @abstractmethod #abstract method
    def start(self):
        pass
    
class car(vehicle):
    def start(self):
        print("car starts with a key")
        
class bike(vehicle):
    def start(self):
        print("bike starts with a button")
        
car1 = car()
bike1= bike()                    

car1.start()
bike1.start()

#rectangle and circle class with abstract class and abstract method

from abc import ABC, abstractmethod

class shape(ABC):
    
    @abstractmethod 
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        
        def area (self):
            return 3.14 * self.radius * self.radius
        
rect1 = rectangle(5,10)
print("Area of rectangle :",rect1.area())   

circle1 = circle(7)
print("Area of circle :",circle1.area())            
