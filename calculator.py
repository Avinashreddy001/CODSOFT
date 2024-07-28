def add(k, l):
    return k + l  # Adding two numbers 

def subtract(k, l):
    return k - l  # Subtracting second number from first 

def multiply(k, l):
    return k * l  # Multipling two numbers

def divide(k, l):
    if l != 0:  # Checks if the second number is not zero
        return k / l  # Dividing the first number with second number
    else:
        return "Error! Division by zero."  # Returns an error message if the second number is zero

def main():
    print("CALCULATOR") 
    
    #input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    #menu of operations
    print("Choose any one operation:")
    print("1. Addition +")
    print("2. Subtraction -")
    print("3. Multiplication *")
    print("4. Division /")
    
    #choose an operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the operation
    if operation == '+':
        result = add(num1, num2)  #add function
    elif operation == '-':
        result = subtract(num1, num2)  #subtract function
    elif operation == '*':
        result = multiply(num1, num2)  #multiply function
    elif operation == '/':
        result = divide(num1, num2)  #divide function
    else:
        result = "Invalid operation!"  #error message if operation is invalid
    
    # Display the result
    print(f"The result is: {result}") 

if __name__ == "__main__":
    main()
