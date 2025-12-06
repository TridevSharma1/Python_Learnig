def calculator():
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1-4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result =", num1 + num2)
    elif choice == '2':
        print("Result =", num1 - num2)
    elif choice == '3':
        print("Result =", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid choice!")


def check_palindrome():
    print("\n--- Palindrome Checker ---")
    num = input("Enter a number: ")

    if num == num[::-1]:
        print(num, "is a Palindrome")
    else:
        print(num, "is NOT a Palindrome")


while True:
    print("\n==============================")
    print("1. Calculator")
    print("2. Palindrome Check")
    print("3. Exit")
    print("==============================")

    option = input("Choose an option: ")

    if option == '1':
        calculator()
    elif option == '2':
        check_palindrome()
    elif option == '3':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid input! Try again.")
