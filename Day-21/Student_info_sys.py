# student information system
class student :
    
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
     
student1 = student("Shubham",19,"Nanded")

print("Student -- 1")    
print("Name :",student1.name)
print("Age :", student1.age)
print("City :",student1.city)

student2 = student("shivam",19,"Parbhani")
print("Student -- 2")
print("Name :",student2.name)
print("Age :", student2.age)
print("City :",student2.city)   
