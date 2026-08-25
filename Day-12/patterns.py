print("1. Square")
print("2. Triangle")
print("3. Inverted Triangle")
print("4. Number Pattern")

choice = int(input("Enter your choice: "))

if choice == 1:
    # Square Pattern
    for i in range(4):
        print("* " * 4)

elif choice == 2:
    # Triangle Pattern
    for i in range(1, 5):
        print("* " * i)

elif choice == 3:
    # Inverted Triangle Pattern
    for i in range(4, 0, -1):
        print("* " * i)

elif choice == 4:
    # Number Pattern
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

else:
    print("Invalid choice")
