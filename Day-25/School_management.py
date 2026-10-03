class person:
       def __init__(self,name,age):
        self.name = name
        self.age = age  
    
       def show_info(self):
        print("Person Name :",self.name)
        print("Person Age :",self.age)
            
class student(person):
       def __init__(self,name,age,marks):
           super().__init__(name,age)
           self.marks = marks
           
       def show_info (self):
           print("Student Name :",self.name)
           print("Student Age :",self.age)
           print("Student Marks :",self.marks)

class teacher(person):
        def __init__(self,name,age,subject):
            super().__init__(name,age)
            self.subject = subject
            
        def show_info(self):
            print("Teacher Name :",self.name)
            print("Teacher Age :",self.age)
            print("Teacher Subject :",self.subject) 
 
 
 
print("_____SCHOOL__INFORMATION_______")                          
student1 = student("Alice",20,90)
student1.show_info()
teacher1 = teacher("Bob",45,"Math")
teacher1.show_info()
