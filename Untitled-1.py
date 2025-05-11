#this is a format of an email
first_name = input("First name: ")
last_name = input("Last name: ")
birth = input("Year of birth: ")
age = 2024 - int(birth)
ab = f"""
Hi {first_name}, 

You name: {first_name} {last_name}
Your age: {age}
Thanks for being with us:)

Thanks
BFF
"""

print(ab)