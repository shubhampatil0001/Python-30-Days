# Day 3 - User Input and Type Conversion
#TASK 1

name = input("Enter your name:")
print("Hello",name)

age = int(input("Enter your age:"))
print("Your age is:",age)

percentage = float(input("Enter your percentage:"))
print("Your percentage is:",percentage)

#using type function for checking data type of variable

print(type(name))
print(type(age))
print(type(percentage))



#TASK 2
#Taking data from the user of name and city
name = str(input("Enter your name:"))
city = str(input("Enter your city:"))



#TASK 3
#taking 2 intergers from the user and performing arithmetic operations
a = int(input("Enter a first integer:"))
b = int(input("Enter a second :"))
print("Addition:",a+b)
print("Subtraction:",a-b)


#length and width of rectangle
length = float(input("Enter length of rectangle:"))
width = float(input('Enter width of rectangle:'))
area = length * width
print("Area of rectangle is:",area)


#finding dattype of celsius 
temprature = float(input("Enter temperature in celsius:"))
print("Data type of temperature:", type(temprature))