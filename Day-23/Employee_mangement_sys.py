# Employee Mangement system

class Employee:
    
    company = "Tech Solution"
    
    def __init__(self,name,age,salary):
        self.name = name
        self.age  = age
        self.salary = salary
        
    def show_info(self):
        print("Information :",employee.company)
          
employee1 = Employee("Ravi",19,  10000)
employee2 = Employee("Ganu", 19 , 20000)
employee3 = Employee("Shiv", 23 , 34888)                   

print("Name :",employee1.name)
print("Age :",employee1.age)
print("Salary :",employee1.salary)
print("Company :",employee1.company)

print("Name :",employee2.name)
print("Age :",employee2.age)
print("Salary :",employee2.salary)
print("Company :",employee2.company)

print("Name :",employee3.name)
print("Age :",employee3.age)
print("Salary :",employee3.salary)
print("Company :",employee3.company)
