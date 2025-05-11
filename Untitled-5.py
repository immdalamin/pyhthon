#the car game
x = 'start'
y = 'stop'
z = 'quit'
a = ''
while True:
    a = input('>').lower()
    if a == x:
        print('Car started!')
    elif a == y:
        print('Car stopped!')
    elif a == 'help':
        print('''
    Start  -- to start the car
    Stop -- to Stop the car
    Quit -- to Quit game
          ''')
    elif a == z:
        break
    else:
        print('I cannot understand that!')