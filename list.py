# simple list operations
my_list = [1, 2, 3, 4, 5]
print(my_list) # Output: [1, 2, 3, 4, 5]

# mixed data types
mixed_list = [1, "Tridev", 3.14, True]
print(mixed_list) # Output: [1, "Tridev", 3.14, True]

# nested lists
nested_list = [1, [2, 3], [4, 5, 6]]
print(nested_list) # Output: [1, [2, 3], [4, 5, 6]]

# accessing nested list elements
print(nested_list[1][0]) # Output: 2
print(nested_list[2][2]) # Output: 6

# list slicing
sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(sample_list[2:5]) # Output: [30, 40, 50]

# empty list
empty_list = []
print(empty_list) # Output: []

# list with different data types
varied_list = [42, "Hello", 3.14, False, [1, 2, 3]]
print(varied_list) # Output: [42, "Hello", 3.14, False, [1, 2, 3]]

# using list() constructor
constructed_list = list((1, 2, 3, 4))   
print(constructed_list) # Output: [1, 2, 3, 4]

# list with repeated elements
repeated_list = [7] * 5
print(repeated_list) # Output: [7, 7, 7, 7, 7]

# list with duplicates
duplicates_list = [1, 2, 2, 3, 4, 4, 4]
print(duplicates_list) # Output: [1, 2, 2, 3, 4, 4, 4]

# list comprehension
squared_list = [x**2 for x in range(6)]
print(squared_list) # Output: [0, 1, 4, 9, 16, 25]

# with conditional logic
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) # Output: [0, 4, 16, 36, 64]

#  append method
append_list = [1, 2, 3]
append_list.append(4)
print(append_list) # Output: [1, 2, 3, 4]

# extend method
extend_list = [1, 2, 3]
extend_list.extend([4, 5, 6])
print(extend_list) # Output: [1, 2, 3, 4, 5, 6]

# insert method
insert_list = [1, 2, 4, 5]  
insert_list.insert(2, 3)
print(insert_list) # Output: [1, 2, 3, 4, 5]
# remove method
remove_list = [1, 2, 3, 4, 5]
remove_list.remove(3)
print(remove_list) # Output: [1, 2, 4, 5]
# pop method
pop_list = [1, 2, 3, 4, 5]  
popped_element = pop_list.pop()
print(popped_element) # Output: 5
print(pop_list) # Output: [1, 2, 3, 4]
