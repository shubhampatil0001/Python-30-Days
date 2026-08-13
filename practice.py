# if or else staemt using for checking adult or not
age = int(input("Enter your age:"))
if age >= 18:
    print("Adult")
else:
    print("Minor")
    

#even or odd using if else statement
num = int(input("Enter a number:"))
if num % 2== 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number") 
    
    
#marks and grades 
marks = int(input("Enter a marks"))

if marks >=90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A ")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")               
    
 
#Voting eligiblity
age = int(input("Enter your age:"))
if age >= 18:
    print(" You are eligible for vote")
else:
    print("You are not eligible for vote")
            
            
pass = [7672]
a = int(input("Enter your password:"))
if a == pass[0]:
    print("Access granted") 
else:
    print("Access denied")               
    
    