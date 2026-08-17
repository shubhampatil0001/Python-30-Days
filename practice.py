#upper lower length of character and  data type of character
name = str (input("Enter your name "))
print(name.upper())
print(name.lower())
print(len(name))
print(type(name))


# Reverse string
word = str (input("Enter your word:"))
print(word[::-1])

#checking word exist or not using in membership operator
sentence = str (input ("Enter your sentence;"))
print("python" in sentence)

#adding two strings using string concatenation
first_name = "Shubham "
last_name ="patil"


full_name = first_name + last_name
print(full_name)

# counting of pasword
password =  (input ("Enter your Password:"))
password_len = (len(password))

print(len(password))


name = str (input("Enter your name:"))

print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])
print(name[::-1])