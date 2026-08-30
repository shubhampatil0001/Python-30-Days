def add (a ,b):  # Addition using function parameter and return
    return  a + b # return function store sent back value
result1 = add(10, 20) # result store value act as a variable arguments also inclu
print("Addition :",result1)

# Subtraction 
def sub(a, b):
    return a - b
result2 = sub(20 ,2)
print("Subtraction:",result2)


# Square
def square(a ):
    return a * a
result3 = square(5)
print("Square :", result3)


# printing double
n = float(input("enter a number:"))
def double (number):
    return number
result = (n * 2)
print(result)

#finding a sqaure number
def square(number):
    return number * number
result = square(5)
print(result)


#price and quantity
def calculate_total(price , quantity):
    return price * quantity

result = calculate_total(400,10)
print(result)


def is_even(number):
    return number

num = int(input("Enter a number :"))
result = is_even(num)

if num % 2 == 0:
    print("EVEN TRUE :",is_even)    
else:
    print("ODD FALSE",is_even)    
