import random
import math
n = random.randint(1,9)
count = 0

guess = int(input("Guess a number:- ")) 

while count < math.log(5):
    count += 1

    if(n==guess):
        print("Congrats")
        
        break

    elif n < guess:
            print("Better luck next time")

    elif n > guess:
            print("Better luck next time")
    if(count>math.log(5)):
        print("You are out of chances")
