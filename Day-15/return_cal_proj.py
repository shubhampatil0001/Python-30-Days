def add (a , b): 
    return( a + b)           #🧠 इथे प्रत्येक function:
                             #a आणि b घेतो → parameters
def sub (a , b):             #calculation करतो
  return a - b               #answer return करतो

def multi ( a ,b):
    return a * b

def Division ( a, b):
    return a / b

num1 = float (input("Enter a first number  :")) # taking input from user
num2 = float (input("Enter a second number :"))


print("\n choose an operation :") # Menu
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice(1-4) :")

if choice == "1":  # if - elif - elif - else condition using
    result = add(num1 ,num2)
    print("Result :",result)
    
elif choice == "2":
    result = sub(num1 , num2)
    print("Result :",result)
    
elif choice == "3":
     result = multi(num1, num2)
     print("Result :",result)
     
elif choice == "4":
    if num2  != 0 : 
        result = Division(num1, num2)
        print("Result :", result)    
    else:
        print("Can not divide by zero ")
  
  
else:
    ("Invalid choice")                    
