marks = [20, 30 ,40 , 50 ,60 ]

print("MARKS:", marks)
print("First Mark:",marks[0])
print("Last Mark :",marks[-1])
print("Number of Subjects :",len(marks))

new_mark = int (input("Enter a new mark :"))
marks.append(new_mark)
print("Updated mark:",marks)