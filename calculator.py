def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def main():
    print("Simple Calculator")
    print("Supported operations: add, subtract, multiply, divide, power")
    print("Type 'exit' to quit.")
    
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide, power): ").strip().lower()
        
        if operation == 'exit':
            print("Goodbye!")
            break
        
        if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if operation == 'add':
                    print(f"Result: {add(x, y)}")
                elif operation == 'subtract':
                    print(f"Result: {subtract(x, y)}")
                elif operation == 'multiply':
                    print(f"Result: {multiply(x, y)}")
                elif operation == 'divide':
                    print(f"Result: {divide(x, y)}")
                elif operation == 'power':
                    print(f"Result: {power(x, y)}")
            except ValueError:
                print("Error: Invalid number. Please enter a valid number.")
        else:
            print("Error: Unsupported operation.")

if __name__ == "__main__":
    main()
