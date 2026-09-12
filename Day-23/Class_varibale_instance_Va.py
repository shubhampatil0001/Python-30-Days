# Day 23 class variable

class Employee:
    
    company = "Tech solution" # ------- class variable 
 
    def __init__(self,name,salary):
     self.name = name  
     self.salary = salary
   
employer1 = Employee("Rohan","15000")
employer2 = Employee("Sonali","20000")

print(employer1.name)
print(employer1.salary)
print(employer1.company)

# Mobile 

class Mobile:
    
    company = "Samsung"
    
    def __init__(self,model,price):
        self.model = model
        self.price = price
        
mobile1 = Mobile("Galaxy A","20000")
mobile2 = Mobile("Galaxy J2","30000")

print("Brand :",mobile1.company)
print("Model :",mobile1.model)
print("Price :",mobile1.price)
        
# student 
        
class student:
    
    school = "ABC school"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def show_info(self):
        print(student)
        
student1 = student("Om",10)
student2 = student("Raj",19)

print("Name :", student1.name)
print("Marks :",student1.marks)
print("School :",student1.school)        
            
