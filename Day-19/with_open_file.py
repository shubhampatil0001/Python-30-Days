# Day 19 File Handling Practice

from importlib.metadata import files


with open("file.txt", "w") as files:
    files.write("Python file handling is easy to learn.")

with open("file.txt","a") as files:
   files.write("\n learning Read, Write and Append")
   
with open("file.txt","r") as files:
   data = files.read()   
   
   print("Overall :",data)
   
   
try:
     with open("student.txt","W") as file:
       data = file.write("Hello shubham")
except:
    print("Invalid input")       
    
    with open("student.txt","r") as file:
        data = file.read()
        print(data)
        
    with open("student.txt","a") as file:
        file.write("\n Hello shubham")    
