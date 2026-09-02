# DAY 16 Exception Handling
try:
    
 num = int ( input("ENTER A NUMBER :"))
 print("YOU ENTERED :", num)

except  ValueError :
    print("Invalid input, Enter a valid number")
 
 
 
 
 
 # task 2   
try :    
    num1 = int (input("Enter a first number :"))    
    num2 = int (input("Enter a second number:"))

    result = num1 / num2
    
    print("Result :", result)
    
except ValueError:
    print("Enter a valid numbers ")
    
except ZeroDivisionError:
    print("can not divide by zero")    
