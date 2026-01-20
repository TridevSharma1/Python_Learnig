a = float(input("First No "))
b = float(input("Second No "))

s = (input("Choose Simble "))

if(s == "*"):
    print(a*b)

elif(s == "+"):
    print(a+b)

elif(s == "-"):
    print(a-b)

elif(s == "/"):
    print(a/b)

elif(s == "%"):
    print((a/b)*100)

else:
    print("Unknown Simble")


# nested if else

userid = "admin"
password = "admin123"
input_id = input("Enter User ID : ")

if(input_id == userid):
    input_pass = input("Enter Password : ")
    if(input_pass == password):
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Unknown User ID")

# break and continue

for i in range(1,11):
    if i == 5:
        break
    print(i)
# 1 2 3 4

for i in range(1,11):
    if i == 5:
        continue
    print(i)
# 1 2 3 4 6 7 8 9 10

#  if statement
a = 10
if a > 5:
    print("a is greater than 5")