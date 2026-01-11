# calculator loop

a = input("Enter Start , End : ")

while a != "End":
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Error: Invalid operator"
    print("Result:", result)
    a = input("Enter Start , End Or Begain: ")


# password checker
password = "secure123" 
user_input = input("Enter the password: ")
while user_input != password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")
print("Access granted.")

# password checker with limited attempts
password = "secure123"
max_attempts = 3
attempts = 0
user_input = input("Enter the password: ")
while user_input != password and attempts < max_attempts - 1:
    attempts += 1
    print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    user_input = input("Enter the password: ")
if user_input == password:
    print("Access granted.")
else:
    print("Access denied. Too many incorrect attempts.")
# password checker with limited attempts and lockout
import time
password = "secure123"
max_attempts = 3
lockout_time = 10
attempts = 0
user_input = input("Enter the password: ")
while user_input != password and attempts < max_attempts - 1:
    attempts += 1
    print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    user_input = input("Enter the password: ")
if user_input == password:
    print("Access granted.")
else:
    print("Too many incorrect attempts. You are locked out for 10 seconds.")
    time.sleep(lockout_time)
    print("You can try again now.")

# password checker with unlimited attempts after lockout
import time
password = "secure123"
max_attempts = 3
lockout_time = 10
attempts = 0
user_input = input("Enter the password: ")
while user_input != password:
    if attempts < max_attempts - 1:
        attempts += 1
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    else:
        print("Too many incorrect attempts. You are locked out for 10 seconds.")
        time.sleep(lockout_time)
        attempts = 0
    user_input = input("Enter the password: ")
print("Access granted.")



    

        

