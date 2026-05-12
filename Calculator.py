while True:
    print("\n===== SIMPLE PYTHON CALCULATOR =====")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice: ")

    if choice == '1':
        print("Result:", num1 + num2)

    elif choice == '2':
        print("Result:", num1 - num2)

    elif choice == '3':
        print("Result:", num1 * num2)

    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid choice!")

    again = input("\nDo you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Thanks for using calculator!")
        break

# This is a simple calculator program in Python that allows the user to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. The program continues to run until the user decides to exit by typing "no".
# added a new file named "Calculator.py" with the above code.

a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

