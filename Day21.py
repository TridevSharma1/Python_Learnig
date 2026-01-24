# for loop on list,string,tuple
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print( i)

my_string = "Hello"
for i in my_string:
    print( i)

my_tuple = (10, 20, 30)
for i in my_tuple:
    print( i)

# mutable and immutable types
mutable_list = [1, 2, 3]
for i in range(len(mutable_list)):
    mutable_list[i] += 1
print( mutable_list)

immutable_string = "abc"
new_string = ""
for char in immutable_string:
    new_string += char.upper()
print( new_string)

# list is mutable
my_list = [1, 2, 3]
for i in range(len(my_list)):
    my_list[i] *= 2
print( my_list)

# tuple is immutable
my_tuple = (1, 2, 3)
new_tuple = ()
for i in my_tuple:
    new_tuple += (i * 2,)
print( new_tuple)

# apply for loop in your name

name = "Tridev sharma"
for i in name:
    print(i)

# apply for loop in list
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

# apply for loop in tuple
tuple = (10, 20, 30, 40)
for i in tuple:
    print(i)

# distonary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
for value in my_dict.values():
    print(f"Value: {value}")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
    

