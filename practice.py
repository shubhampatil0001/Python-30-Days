fruits = ["apple", "banana", "orange", "grapes", "strawberry"]
for fruit in fruits :
    print(fruits)
    
    #print first and last item using index index, negative index
    print("First fruit:",fruits[0])
    print("Last fruit:",fruits[-1])
    
    # used append to add fruit at end of list
    fruits.append("Guvava")
    print(fruits)
    break 
  
  #changing the fruit
fruits [1] = "Watermalon"
print(fruits)

# remove fruit using remove ()
fruits.remove("orange")
print(fruits)

#finding lenth of list
print(len(fruits))

#taking no from users and store in list
numbers = []
for i in range(10):
    number = int(input("Enter a number : "))
    numbers.append(number)
print(numbers)


num = []
for i in range(5):
    num = int(input("Enter a number"))
    numbers.append(num)
    total_sum = sum(numbers)
    
    print(numbers)
    print(total_sum)