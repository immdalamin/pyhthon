# this is a gusseing game
import random
num = random.randrange(0, 9)
guess = int(input("Guess the number: "))

if guess == num:
    print(f"You won, the number is {num}")
else:
    print(f"You loose, the number is {num}")