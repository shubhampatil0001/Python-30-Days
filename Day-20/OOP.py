# Day - 20 OOP basics (class, object, Attributes)
#student
class student:
    pass

student1 = student()

student1.name = "shubham"
student1.age = 18
student1.city = "Nanded"

print(student1.name)
print(student1.age)
print(student1.city)

# car
class car :
    pass

car1 = car() #        creating a function variable is car1 = car is class

car1.name = "Innova"
car1.no = 202
car1.model = "X01"


print(car1.name)
print(car1.no)
print(car1.model)

# Book 
class book :
    pass

book1 = book()

book1.title = "Johnny Was a Good Man"
book1.author = "Guido van Rossum"

print("Title :",book1.title)
print("Author :",book1.author)


#Mobile
class mobile :
    pass

class laptop :
    pass

mobile1 = mobile()

mobile1.brand = "iphone"
mobile1.model = "12" 
mobile1.price = 49000

laptop1 = laptop()

laptop1.brand = "Mackbook"
laptop1.model = "M2"
laptop1.price = 120000

print("Brand :",mobile1.brand)
print("Model :",mobile1.model)
print("Price :",mobile1.price)

print("Brand :",laptop1.brand)
print("Model :",laptop1.model)
print("Price :",laptop1.price)
