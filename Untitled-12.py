# this is a guessing game
print("**Guess a number between 0-9**")
import random
chances = 3

while chances > 0:
    num = random.randrange(0, 10)
    guess = int(input("Guess the number: "))
    chances -= 1
    if guess == num:
        print(f"You had more {chances} chances; *You won the game!")
        break
    elif guess != num and chances != 0:
        print(f'You have {chances} chances; the number was {num}; try again!')
    else:
        print("You have no chances; you loose!")