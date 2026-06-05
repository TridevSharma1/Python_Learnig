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

# login system with user database
user_db = {"admin": "admin123", "user1": "pass1", "user2": "pass2"}
username = input("Enter username: ")    
password = input("Enter password: ")
squared = [x**2 for x in range(5)]
while username not in user_db or user_db[username] != password:
    print("Invalid username or password. Try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")
print("Login successful. Welcome,", username)
print("Squared numbers:", squared)
squared_dict = {x: x**2 for x in range(5)}
print("Squared dictionary:", squared_dict)

# signup system with user database
user_db = {}    
username = input("Choose a username: ")
while username in user_db:
    print("Username already taken. Please choose another one.")
    username = input("Choose a username: ")
password = input("Choose a password: ")
user_db[username] = password
print("Signup successful. You can now log in.")
username = input("Enter username: ")
password = input("Enter password: ")
while username not in user_db or user_db[username] != password:
    print("Invalid username or password. Try again.")
    username = input("Enter username: ")
    password = input("Enter password: ")
print("Login successful. Welcome,", username)
print("User Database:", user_db)

# dictionaries and sets
Info = {
    'name' : 'Tridev Sharma',
    'Age' : 17,
    'Marks' : [20,30,20,19,30],
    'percent' : 98.9,
    'pass' : True
}
Info['name']= 'Tridev'
Info['Gender'] = 'Male'
print(Info)
print(Info['name'],Info['Age'])
Student = {
    'name' :' Tridev Sharma',
    "subject" :{
    'Geo' :  30,
    'Eco' : 20,
    'Hindi' : 20
 }
}
print(Student)
print(Info.keys())
print(Info.values())
print(Info.items())
print(Info.get('name'))
Info.update({"Gender" : "MAle"})
print(Info) 

# Controler Statements
a = 10
if a > 0:
    print("a is positive")
else:
    print("a is non-positive")

# Sun and Moon
time = input("Enter time (day/night): ")
if time == "day":
    print("The sun is shining.")
elif time == "night":
    print("The moon is visible.")
else:
    print("Invalid input. Please enter 'day' or 'night'.")

# Grade Calculator
score = float(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# library system
books = {
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "available": True},
    "To Kill a Mockingbird": {"author": "Harper Lee", "available": True},
    "1984": {"author": "George Orwell", "available": True}
}
book_name = input("Enter the name of the book you want to borrow: ")
if book_name in books:
    if books[book_name]["available"]:
        print(f"You have borrowed '{book_name}' by {books[book_name]['author']}.")
        books[book_name]["available"] = False
    else:
        print(f"Sorry, '{book_name}' is currently unavailable.")
else:
    print("Sorry, we don't have that book in our library.")

# fabonaci series
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

# converting temperature
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = (temp_c * 9/5) + 32
print(f"{temp_c}°C is equal to {temp_f}°F.")


# lambda function for square
square = lambda x: x**2
num = float(input("Enter a number to find its square: "))
print(f"The square of {num} is {square(num)}.")

# recursive function for factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}.")

   
# voting system
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# voting for party
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    party = input("Which party do you want to vote for? (Democrat/Republican/Other): ")
    if party in ["Democrat", "Republican", "Other"]:
        print(f"You have voted for the {party} party.")
    else:
        print("Invalid party choice.")
else:
    print("You are not eligible to vote yet.")

# scheduling system
day = input("Enter the day of the week: ")
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("You have work/school today.")
elif day in ["Saturday", "Sunday"]:
    print("You have a day off today.")
else:
    print("Invalid day of the week.")


