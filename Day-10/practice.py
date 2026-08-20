student = {
     "name" : "Shubham" ,
     "age"  : 18 ,
     "city" : "Nanded"
 } 
 
print(student)
#Acess
print(student["name"])

#Add
student["Course"] = "Engineering"

#Update
student["age"] = 19
student["city"] = "Pune"

#Remove
student.pop("age")

print(student)

print("Total info :",len(student))



#another task
book = {
    "title": "Python",
    "price": 600,
    "author" : "Swapyy"
}
#printing title means accesing
print(book["title"])

#Updating price of the book 
book["price"]= "1000"

#Add new key 
book ['pages'] = '230'

#length of book 
print("Total key values :", (len(book)))

print(book)

#student detalis 

print("--- STUDENT DETAILS ----")

student = {
    "name":input("Enter your name :"),
    "age" : int(input("Enter your age :")),
    "city":input("Enter your city :"),
    "course" :input ("Enter your course :")
    
}
print("STUDENT DETAILS :--",student)
