# function 
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def info(name, age):
    return f"Name: {name}, Age: {age}"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add_result = add(a, b)
print(f"Addition: {add_result}")

sub_result = subtract(a, b)
print(f"Subtraction: {sub_result}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(info(name, age))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
fact = factorial(num)
print(f"Factorial of {num} is {fact}")

# ------------------------------------------------------

def tridev():
            print("Name Tridev")
            print("course BCA")
            print("Age 18")
tridev()

def sum_two(a,b):
                print("the sum of a and b is : ", a + b)
sum_two(10,20)

def sum_three(a,b,c):
                    print("the sum of three is : ", a + b + c)
sum_three(10,20,30)

def subtract_two(a,b):
                print("the subtract of a and b is : ", a - b)
subtract_two(30,20)

def subtract_three(a,b,c):
                print("the subtract of three is : ", a - b - c)
subtract_three(30,20,10)

def sum_and_subtract(a,b,c):
                    sum = a + b + c
                    subtract = a - b - c
                    print("the sum is : ", sum)
                    print("the subtract is : ", subtract)

a = int(input("Enter first no : "))
b = int(input("Enter second no : "))
c = int(input("Enter third no : "))
sum_and_subtract(a,b,c)
# ------------------------------------------------------

# 29:01:2026

# function to calculate area of rectangle
def area_of_rectangle(length, breadth):
    return length * breadth
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = area_of_rectangle(length, breadth)
print("Area of rectangle:", area)

# function to make a simple calculator
def calculator(num1, num2, op):
    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid op."

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter what you want to do (add, subtract, multiply, divide): ")
result = calculator(num1, num2, op)
print("Result:", result)

# function to enter name and age
def enter_name_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print("Name:", name, "Age:", age)
enter_name_age()

# function to get details and print
def get_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    print("Name: ",name," Age: ",age," City:", city)
get_details()

# function to check voter eligibility
def check(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
age = int(input("Enter your age: "))
eligibility = check(age)
print(eligibility)


