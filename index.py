# Simple Calculator

def calculator():
    print("=== Simple Calculator ===")
    
    try:
        # Take user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Operation choice
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        # Perform calculation
        if choice == "1":
            result = num1 + num2
            operation = "+"
        elif choice == "2":
            result = num1 - num2
            operation = "-"
        elif choice == "3":
            result = num1 * num2
            operation = "*"
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                operation = "/"
            else:
                print("⚠ Cannot divide by zero!")
                return
        else:
            print("⚠ Invalid choice!")
            return
        
        # Display result
        print(f"\n✅ Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("⚠ Please enter valid numbers!")

# Run calculator
calculator()
