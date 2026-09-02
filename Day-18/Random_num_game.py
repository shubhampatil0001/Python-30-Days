# random number game 
import random
secret = random.randint(1, 30)

guess = int( input (" Enter your number :"))

if guess == secret:
    print("Congratulations ! Correct Guess")

else:
    print("Sorry ! Wrong Guess")
    print("The secret number was :", secret)
