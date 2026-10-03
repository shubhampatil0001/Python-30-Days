# Inheritance in Python
from unicodedata import name


class animal:
    def eat(self):
        print("Animal is Eating...")
       
class dog(animal):
    def bark(self):
        print("Dog is Barking...")
       
dog1 = dog()
dog1.eat()
dog1.bark()

class cat(animal):
    def meow(self):
        print("Cat is Meowing...")
        
cat1 = cat()
cat1.eat()
cat1.meow()

# person and student class
class person :
    def __init__(self,name):
        self.name = name
        
class student(person):  
    def info(self):
        print("Student Name :",self.name)
        
student1 = student("Alice")
student1.info()

#3
class Human:
    def __init__(self,name):
        self.name = name
    
class Employee(Human):
    def __init__(self,name,position):
        super().__init__(name)
        self.position = position
        
    def show_info(self):
        print("Employee Name :",self.name)
        print("Position :",self.position)   
        
Employee1 = Employee("Bob","Manager")
Employee1.show_info()

#vehicle and car class
class vehicle:

    def start(self):
        print("Vehicle started")

class car(vehicle):

    def drive(self):  # Use self for instance methods
        print("Car is driving")


car1 = car()
car1.start()  # Output: Vehicle started
car1.drive()  # Output: Car is driving                  
    
   #person and teacher class 
class person:
     def __init__(self,name):
      self.name = name
    
class teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
        
    def show_info(self):
        print("Teacher Name :",self.name)
        print("Subject :",self.subject)
        
teacher1 = teacher("Rahul","Maths")
teacher1.show_info()        

#interest rate and bank account class
class Bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def show_balance(self):
        print("Account Holder :",self.name)
        print("Balance :",self.balance) 
        
class SavingsAccount(Bankaccount):
    def __init__(self,name,balance,interest_rate,):
        super().__init__(name,balance)
        self.interest_rate = interest_rate
        interest = (self.balance * self.interest_rate) / 100
        print("Interest Rate :",self.interest_rate)
        print("Interest Amount :",interest)
        
        
SavingsAccount1 = SavingsAccount("John",1000, 5)
SavingsAccount1.show_balance()
   
                
        
             
