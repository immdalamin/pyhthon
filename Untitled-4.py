print('GUESS THE NUMBER')
luckey_number = 6
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count = guess_count + 1
    if guess == luckey_number:
        print('you won!')
        break
else:
    print('you lose!')
