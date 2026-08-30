#SCOPE
 
 # Global variable (Outside variable)
x = 100
def global_var():
     print(x)
   
global_var()  

# Local variable  (Inside variable)
def local_var():
    x = 120
    print(x)
local_var()   

name = "shubham" # using global
def greet():
    print("Hello" ,name)
greet()    

#using local printing age
def student():
    age = 29
    print("AGE : --",age)
student()    
    
    
# used local and global together 
x = 200
def test():
    x = 50
    print(x)
    
test()
print(x)       


def calc_sqr(a):
    return a * a

result = calc_sqr(2)
print(result)
