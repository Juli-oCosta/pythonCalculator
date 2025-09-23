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

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

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

def get_number_input(prompt_message):
    # Continua pedindo um número ao usuário até que uma entrada válida seja fornecida.
    while True:
        try:
            number = int(input(prompt_message))
            return number
        except ValueError:
            print("Oops! That's not a valid number. Please enter only digits.")

first_number = get_number_input("Type in the first number: ")
second_number = get_number_input("Type in the second number: ")

while True:
  operator = input("Select the operator: '+', '-', '*' or '/': ")
  if operator in ['+', '-', '*', '/']:
    break
  else:
    print("Invalid operator. Please, choose one of the following: +, -, *, /")

if operator == "+":
  result = add(num1 = first_number, num2 = second_number)
elif operator == "-":
  result = subtract(num1 = first_number, num2 = second_number)
elif operator == "*":
  result = multiply(num1 = first_number, num2 = second_number)
else:
  result = divide(num1 = first_number, num2 = second_number)

print(f"{first_number} {operator} {second_number} = {result}")
