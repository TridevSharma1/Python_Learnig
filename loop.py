# for loop
for i in range(5):
    print("Iteration:", i)

# while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# nested loop
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

# loop with break
for i in range(10):
    if i == 5:
        break
    print("Breaking at:", i)

# loop with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# loop with pass
for i in range(3):
    if i == 1:
        pass
    print("Value:", i)

# loop with else
for i in range(3):
    print("Looping:", i)    
else:
    print("Loop completed")

# looping through a list
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print("List item:", item)
# looping through a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print("Key:", key, "Value:", value)
    
# using enumerate
for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)

# using zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print("Number:", num, "Character:", char)

# list comprehension with loop
squared = [x**2 for x in range(5)]
print("Squared values:", squared)

# dictionary comprehension with loop
squared_dict = {x: x**2 for x in range(5)}
print("Squared dictionary:", squared_dict)

# for loop with list slicing
my_list1 = [100, 200, 300, 400, 500, 600]
for item in my_list1[1:4]:
    print("Sliced item:", item)

mylist2 = [1, 2, 3, 4, 5, 6]
for i in mylist2:
                   print("Item from mylist1:", i)
