from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  should_continue = True

  num1 = float(input("What's the first number?: "))

  while should_continue:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))  

    operation = operations[operation_symbol]
    answer = operation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, 'end' to exit or 'n' to start a new calculation: ").lower()
    if choice == "end":
      break
    elif choice == "y":
      num1 = answer
    elif choice == "n":
      calculator()

calculator()
