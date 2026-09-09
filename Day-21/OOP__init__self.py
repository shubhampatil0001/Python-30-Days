# Day 21 using initializer method and self keyword to reduce the code redundancy


class student:
    
    def __init__(self,name,age,city):

         self.name = name
         self.age = age
         self.city = city
         
student1= student("Shubham",19,"Nanded")
student2= student("shivaji",20,"Parbhani")         
student3= student("Rahul",19,"Pune")

print("Student -- 1")
print("Name :",student1.name)
print("Age :", student1.age)
print("City :",student1.city)
print("Student -- 2")
print("Name :",student2.name)
print("Age :", student2.age)
print("City :",student2.city)   
print("Student -- 3")
print("Name :",student3.name)
print("Age :", student3.age)
print("City :",student3.city)   


# 2 objects are created using class and initializer method with self keyword to reduce the code redundancy  

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shubham", 18)
student2 = Student("Rahul", 19)


print(student1.name)
print(student2.name)

# car 

class car:
    def __init__(self,name, model ,year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

car1 = car ("BMW", "X5" , 2020 , "Black")

print("Car --1")
print("Name :",car1.name)
print("Model :",car1.model)
print("Year :", car1.year)
print("Color :",car1.color)   

car2 = car ("Audi ","A6" , 2021 , "White")
print("Car --2")
print("Name :",car2.name)
print("Model :",car2.model)
print("Year :",car2.year)
print("Color :",car2.color)

# Book
class Book :
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
Book1 = Book("Python Programming","Shubham", 500)
Book2 = Book("Java Programming","Rahul", 600)

print("Book --1")
print("Title :",Book1.title)
print("Author :",Book1.author)
print("Price :",Book1.price)

print("Book --2")
print("Title :",Book2.title)
print("Author :",Book2.author)
print("Price :",Book2.price)
