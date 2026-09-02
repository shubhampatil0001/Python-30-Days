# Day - 18 Modules
import math

print("Square :",math.sqrt(49))

print("Power :",math.pow(3,3))

print("Ceil :",math.ceil(6.2))

print("Floor :", math.floor(8.49))

# using math module finding square root of 81

import math
print("Square :",math.sqrt(81))

# using math module finding ceil of 6.2

import math 
print(math.ceil(6.2))

#using math module finding floor of 9.8

import math
print(math.floor(9.8))

# using random module  

import random
print(random.randint(1,100))

# lucky number game using random module

import random
secret =random.randint(1,30)

user = int(input("Enter your number :"))

if user == secret :
    print("you are lucky")
    
else:
    print("Sorry ! Try again")    
