# This program calculates the grade based on the marks entered by the user.

print("Welcome to the Grade Calculator!")
marks = float(input("Enter your marks:"))
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")