# Employee-
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: ₹{self.salary}")


# २ Employees object
emp1 = Employee("Rohan shinde", 50000)
emp2 = Employee("priya patil", 65000)


emp1.show_details()
emp2.show_details()

emp2.show_details()
emp2.show_details()


#Inheritance

class person :
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        
    def show_detail(self):
     print(f"NAME :{self.name},   AGE:{self.age}")    
     
class student(person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course 
        
    def show_info(self):
      self.show_detail()
      print(f"COURSE :{self.course}")
      
student1 = student("Rohan",20,"Python")
student2 = student("Priya",21,"Java")

student1.show_info()
student2.show_info()      



# POlymorphism
class circle:

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius


class rectangle:

    def __init__(self, length, width):
        self.length = length  
        self.width = width  

    def area(self):
        return self.length * self.width


circle1 = circle(7)
rectangle1 = rectangle(10, 5)


print("Circle Area:", circle1.area())  # Output: 153.86
print("Rectangle Area:", rectangle1.area())  # Output: 50
