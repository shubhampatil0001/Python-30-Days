# Day 22 - Methods


from operator import add, sub
from unittest import result


class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
    
    def study(self):
        print(self.name,"is studying python")

student1 = Student("Shubham")
student2 = Student("Shubham")

student1.greet()

student2.study()


# calculator

class Calculator:
    
    def add(self,a,b):
     return a + b
 
calc = Calculator()
 
print(calc.add(10,20))

#new code

class Student:
    
    def __init__(self,name,marks):
      self.name = name
      self.marks = marks
    
    def show_marks(self):
        print("Marks :",self.marks)
        
student1 = Student("Shubham",90)
student2 = Student("Shubham",80)
student1.show_marks()
student2.show_marks()       
