def add (a,b):
    return a + b

def sub (a,b):
    return a - b

def multiply(a,b):
    return a * b

def Division(a,b):
    return a / b

try :
    num1 = int(input("Enter a first number :"))
    num2 = int(input("Enter a second number :"))
    
except ValueError:
    print("Enter a valid numbers ")
    
    
print("\n choose an operation:")
print("1.Addition ")  
print("2.Subtraction")
print("3.MUltiplication")
print("4.Division") 

choice = input("Enter a your choice (1 - 4) :") 

if choice == "1":
    result = add(num1 , num2)
    print("Result :",result)
    
elif choice == "2":
    result = sub(num1,num2)
    print("Result :",result)
    
elif choice == "3":
    result = multiply(num1,num2)
    print("Result:",result)

elif choice == "4 " :
    if num2 != 0:   
      result = Division(num1,num2) 
      print("Result :",result)
    else:
        ("can not divide by zero")
else:
    ("Invallid Choice")    
    
