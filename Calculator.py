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
