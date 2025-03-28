import art  

# Basic math operation functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# Dictionary mapping operators to their corresponding functions
operation_dictionary = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div
}

# Main calculator function
def calculator():
    print(art.logo)
    
    # Get the first number from the user
    num1 = float(input("What's the first number? "))

    # Display available operations
    for symbol in operation_dictionary:
        print(symbol)

    should_continue = True

    while should_continue:
        # Ask user to pick an operation and the next number
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        # Get the appropriate function from the dictionary and perform the calculation
        calculation_function = operation_dictionary[operation_symbol]
        result = calculation_function(num1, num2)

        # Display the result
        print(f"{num1} {operation_symbol} {num2} = {result}")

        # Ask if user wants to continue with the result
        next_step = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()

        if next_step == 'y':
            num1 = result  # Use the current result as the new first number
        else:
            should_continue = False
            print("\n" * 20)  # Clear the console
            calculator()  # Restart the calculator

# Start the calculator
calculator()
