# Python Keywords Demonstration Program

import math
from math import sqrt

# Constants
True_value = True
False_value = False
none_value = None

# Global & nonlocal
x = 10

def outer():
    y = 5
    def inner():
        nonlocal y
        y += 1
        return y
    return inner()

# Class, pass, self
class Demo:
    def __init__(self, value):
        self.value = value

    def show(self):
        pass

# If, elif, else
def check_number(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

# For, while, break, continue
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("For loop:", i)

i = 0
while i < 3:
    print("While loop:", i)
    i += 1

# Try, except, finally, raise
try:
    a = 10 / 2
    if a == 5:
        raise ValueError("Custom Error")
except ValueError as e:
    print("Exception:", e)
finally:
    print("Finally block executed")

# With, as
with open("sample.txt", "w") as f:
    f.write("Hello Python")

# Lambda
square = lambda x: x * x
print("Lambda:", square(4))

# Return, yield
def generator():
    yield 1
    yield 2

# Assert
assert 5 > 3, "Assertion Failed"

# Logical operators: and, or, not
if True_value and not False_value or False_value:
    print("Logical operators used")

# In, is
list_data = [1, 2, 3]
if 2 in list_data:
    print("in keyword used")

if none_value is None:
    print("is keyword used")

# Del
temp = 100
del temp

# Global usage
def change_global():
    global x
    x += 5

change_global()
print("Global x:", x)

# Async, await (basic example)
import asyncio

async def async_func():
    await asyncio.sleep(1)
    return "Async Done"

async def main():
    result = await async_func()
    print(result)

asyncio.run(main())

# Comments listing all keywords:
# False, None, True, and, as, assert, async, await, break, class,
# continue, def, del, elif, else, except, finally, for, from, global,
# if, import, in, is, lambda, nonlocal, not, or, pass, raise, return,
# try, while, with, yield

# Python Keywords Example Program

# import, from
import math
from math import sqrt

# global
x = 10

# def, return
def add(a, b):
    return a + b

# if, elif, else
def check(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"

print(add(5, 3))
print(check(-2))

# for, break, continue
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("For:", i)

# while
i = 0
while i < 3:
    print("While:", i)
    i += 1

# try, except, finally
try:
    a = 10 / 2
    print(a)
except:
    print("Error")
finally:
    print("Done")

# class, self, pass
class Demo:
    def __init__(self):
        self.x = 5
    def show(self):
        pass

# lambda
square = lambda x: x * x
print(square(4))

# and, or, not
if True and not False:
    print("Logical operators")

# in, is
data = [1, 2, 3]
if 2 in data:
    print("In keyword")

a = None
if a is None:
    print("Is keyword")

# del
b = 100
del b

# with, as
with open("file.txt", "w") as f:
    f.write("Python")

# yield
def gen():
    yield 1
    yield 2

# assert
assert 5 > 2

# raise
try:
    raise ValueError("Error raised")
except ValueError:
    print("Raised error caught")

