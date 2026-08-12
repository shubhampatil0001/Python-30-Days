# Day 4 - Operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)#Arithematic operators 
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print("Equal:", a == b)
print("Not Equal:", a != b) #comparison operator
print("Greater:", a > b)
print("Less:", a < b)


#checking age using opertaorss  statemet 
age = float(input("Enter your age:"))
print( age >= 18 )

#checkinbg odd or even number using if else statement
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is an even number")
else :
    print(num, "is an odd number")