#python calculator
x = int(input('First number: '))
z = input('enter your operator: ')
y = int(input('Second number: '))

if z == '+':
    result = (x + y)

if z == '-':
    result = (x - y)

if z == '*':
    result = (x * y)

if z == '/':
    result = (x / y)

print(result)