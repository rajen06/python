def calculator():
    while True:
        # Start a new calculation
        print("\n--- New Calculation ---")
        first_number = float(input("What's the first number?: "))
        print("+\n-\n*\n/")
        result = first_number
        
        while True:
            operation = input("Pick an operation: ")
            next_number = float(input("What's the next number?: "))
            
            if operation == "+":
                result += next_number
            elif operation == "-":
                result -= next_number
            elif operation == "*":
                result *= next_number
            elif operation == "/":
                if next_number == 0:
                    print("Error: Division by zero is undefined.")
                    continue
                result /= next_number
            else:
                print("Invalid operation.")
                continue
            
            print(f"Result: {result}")
            
            continue_calculating = input(f"Type 'y' to continue calculating with {result}, 'n' for a new calculation, or 'exit' to quit: ").lower()
            if continue_calculating == "n":
                break
            elif continue_calculating == "exit":
                print("Goodbye!")
                return

calculator()
