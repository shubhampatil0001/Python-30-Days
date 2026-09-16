# Day 24 class method, instance method , static method

#class method ( cls )
class college:
    
    name = "SRTMUN COLLEGE "
    
    @classmethod
    def show_info(cls):
        print("NAME :",cls.name)
        
college.show_info()        

# static method

class calculator :
   
    @staticmethod
    
    def add( a, b):
       return a + b
   
    def sub( a , b):
       return a - b
   
    def mul( a , b):
       return a * b
   
print(calculator.add(20, 20))
print(calculator.sub( 90 , 30))
print(calculator.mul( 2 , 2)) 

# 3
class student :
    #class variable
    school = "School of computational science"
    
    #constructor for instance variable
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    #Instance method    
    def show_info(self):
        print(self.name)
    
    #class method    
    @classmethod
    def show_school(cls):
        print(cls.school)
        
    @staticmethod
    def is_pass(marks):
        """Return the student's result based on the passing mark."""
        return "Pass" if marks >= 40 else "Fail"
       
# class method calling                         
student.show_school()

# creating a object
s1 = student("Shiv",20)
s2 = student("OM",21)

# Calling  instance
s1.show_info()
s2.show_school()

#Static method using
print(f"Rahul Result: {student.is_pass(s1.marks)}")
print(f"Priya Result: {student.is_pass(s2.marks)}")
