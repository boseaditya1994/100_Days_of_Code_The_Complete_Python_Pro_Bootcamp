def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero."
    return n1 / n2

# 1. Map symbols to functions using a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    # 2. Get the initial number
    num1 = float(input("What's the first number?: "))
    
    # Print available operations
    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        # 3. Retrieve and execute the function directly from the dictionary
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # 4. Check if the user wants to continue chaining calculations
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        
        if choice == 'y':
            num1 = answer  # Carry over the result to the next iteration
        else:
            should_continue = False
            print("\n" * 20)  # Clear screen space
            calculator()     # Recursively restart for a fresh calculation

# Start the calculator
calculator()