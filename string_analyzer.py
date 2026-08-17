text = input("Enter a text :")

print("ORIGINAL TEXT :",text)
print("LENGTH:",len(text))
print("UPPER:",text.upper())
print("LOWER:",text.lower())
print("REVERSED:",text[::-1])

character = input("ENTER A CHARACTER:")
print(character in text)