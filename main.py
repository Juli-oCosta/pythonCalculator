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

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

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

first_number = int(input("Type in the first number: "))
second_number = int(input("Type in the second number: "))
operator = input("Select the operator: '+', '-', '*' or '/': ")

if operator == "+":
  add(num1 = first_number, num2 = second_number)
elif operator == "-":
  subtract(num1 = first_number, num2 = second_number)
elif operator == "*":
  multiply(num1 = first_number, num2 = second_number)
else:
  divide(num1 = first_number, num2 = second_number)

