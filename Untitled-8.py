x = input("enter your number: ")
last_digit = x[-1]

odd_num = ['2', '4', '6', '8', '0']

for item1 in odd_num:
    if item1 == last_digit:
        print('odd number')
        break
else:
    print('even number')


'''
def identify_odd_even(number):
  """
  This function effectively determines whether a number is odd or even.

  Args:
      number: The integer to be classified.

  Returns:
      A string indicating "odd" or "even" based on the number's parity.
  """

  # Use modulo operator for efficient odd/even check
  if number % 2 == 0:
    return "even"
  else:
    return "odd"

# Get user input and convert to integer (handles non-numeric input)
while True:
  try:
    number = int(input("Enter your number: "))
    break  # Exit loop if input is valid
  except ValueError:
    print("Invalid input. Please enter a number.")

# Call the function to determine odd or even
result = identify_odd_even(number)
print(f"The number {number} is {result}.")
'''