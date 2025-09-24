logo = """
 _____________________
|  _________________  |
| |       2 + 2 = 4 | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

"""

print(logo)

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    return "Cannot divide by zero."
  else:
    return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def get_number_input(prompt_message):
    # keeps asking a number to the user until a valid input is given
    while True:
        try:
            number = int(input(prompt_message))
            return number
        except ValueError:
            print("Oops! That's not a valid number. Please enter only digits.")

first_number = get_number_input("Type in the first number: ")

over = False
while not over:
  while True:
    operator = input("Select the operator: '+', '-', '*' or '/': ")
    if operator in ['+', '-', '*', '/']:
      break
    else:
      print("Invalid operator. Please, choose one of the following: '+', '-', '*' or '/'")

  second_number = get_number_input("Type in the second number: ")

  calculation_function = operations[operator]
  result = calculation_function(first_number, second_number)

  print(f"{first_number} {operator} {second_number} = {result}")

  if isinstance(result, str):
    print("An error ocurred, cannot divide by zero.")
    first_number = get_number_input("What's the first number?: ")
    continue

  while True:
    next_step = input(f"Type 'c' to continue calculating with {result}, 'n' to start a new calculation, or 's' to stop: ").lower()

    if next_step == 'c':
      first_number = result
      break
    elif next_step == 'n':
      first_number = get_number_input("What's the first number?: ")
      break
    elif next_step == 's':
      over = True
      break
    else:
       print("Invalid option. Please, choose 'c', 'n', or 's'.")

print("Calculator finished. Goodbye!")
