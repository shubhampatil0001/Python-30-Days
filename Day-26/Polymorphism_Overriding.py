#Polymorphism in Python

class vehicle:           # parent class
    
    def move(self):
        print("Vehicle is moving")
        
class Bike(vehicle):      #child class
    
    def move(self):
        print("Bike is moving")
 
class Car(vehicle):
    def move(self):
        print("Car is moving")
        
                

bike1 = Bike()
bike1.move()  # Output: Bike is moving

car1 = Car()
car1.move()  # Output: Car is moving


#Overriding method in Python

class Employee:
    def work(self):
        print("Employee is working")
        
         
class Developer(Employee):
          def work(self):
           print("Developer is coding")
           
        
class Teacher(Employee):
    def work(self):
        print("Teacher is teaching")                

dev1 = Developer()
dev1.work()

teach1 = Teacher()
teach1.work()



# Polymorphism in Python overriding method
class shape:
    def area(self):
        return 0
    
class rectangle(shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
class square(shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    
rect1 = rectangle(5, 10)
print("Area of rectangle:", rect1.area())    

square1 = square(5)
print("Area of square:", square1.area())    
