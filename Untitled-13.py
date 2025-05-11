# rock, paper, scissors game
from random import randint
options = ['rock', 'paper', 'scissors']
point = 0

while True:
    computer = options[randint(0, 2)]
    user = input("Rock, Paper or Scissors?: ")
    user = user.lower()

    if user == computer:
        marks = 0
        print(f"It is a tie!, your points: {point}\n")
        
    elif user == 'scissors':
        if computer == "paper":
            marks = 1
            point += marks
            print(f"You won the game!, computer was {computer}, your points: {point}\n")
            
        else:
            marks = 0
            print(f"You loose the game!, computer was {computer}, your points: {point}\n")
            
    elif user == 'paper':
        if computer == "rock":
            marks = 1
            point += marks
            print(f"You won the game!, computer was {computer}, your points: {point}\n")
            
        else:
            marks = 0
            print(f"You loose the game!, computer was {computer}, your points: {point}\n")
            
    elif user == 'rock':
        if computer == 'scissors':
            marks = 1
            point += marks
            print(f"You won the game!, computer was {computer}, your points: {point}\n")
            
        else:
            marks = 0
            print(f"You loose the game!, computer was {computer}, your points: {point}\n")

    elif user == 'exit':
        break

    else:
        print("Write properly\n")
















'''
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
'''