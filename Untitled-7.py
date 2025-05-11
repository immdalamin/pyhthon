try:
    age= int(input("Your age: "))
    income = 2000
    total = income / age
    print(total)
except ValueError:
    print('Invalid input!')
except ZeroDivisionError:
    print('Age cannot be zero.')