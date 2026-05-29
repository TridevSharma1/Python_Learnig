"""Shared helper functions for the Python Learning examples."""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculator_loop():
    while True:
        print("\n===== SIMPLE PYTHON CALCULATOR =====")
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

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


def arithmetic_demo(a=10, b=5):
    print("\n--- Arithmetic Operations Demo ---")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)


def operator_demo():
    print(" 1. ARITHMETIC OPERATORS ")
    a = 10
    b = 3

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)

    print(" 2. COMPARISON OPERATORS ")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)

    print(" 3. ASSIGNMENT OPERATORS ")
    x = 5
    print("x:", x)

    x += 2
    print("x += 2:", x)

    x -= 1
    print("x -= 1:", x)

    x *= 3
    print("x *= 3:", x)

    x /= 2
    print("x /= 2:", x)

    x %= 3
    print("x %= 3:", x)

    x **= 2
    print("x **= 2:", x)

    print("4. LOGICAL OPERATORS ")
    p = True
    q = False

    print("p and q:", p and q)
    print("p or q:", p or q)
    print("not p:", not p)

    print("5. BITWISE OPERATORS")
    m = 6
    n = 3

    print("m & n:", m & n)
    print("m | n:", m | n)
    print("m ^ n:", m ^ n)
    print("~m:", ~m)
    print("m << 1:", m << 1)
    print("m >> 1:", m >> 1)

    print(" 6. MEMBERSHIP OPERATORS")
    list1 = [1, 2, 3, 4]
    print("2 in list1:", 2 in list1)
    print("5 not in list1:", 5 not in list1)

    print("7. IDENTITY OPERATORS ")
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]

    print("x is y:", x is y)
    print("x is z:", x is z)
    print("x == z:", x == z)
    print("x is not z:", x is not z)
