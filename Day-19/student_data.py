name = input("Enter your name :")
age = int(input("Enter your age :"))
city = input("Enter your city :")

with open ("student.txt","w") as file :
    file.write(f"Name : {name}\n Age : {age}\n City : {city}")  
    
    student = ( name , age , city)
    print(student)
