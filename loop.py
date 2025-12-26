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

    
