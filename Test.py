count = 3
while count <= 90 :
    print('Tridev Sharma' , count )
    count += 3 

n = int(input('Enter No -->'))
i = 1
while i <= 100 :
    print(n*i)
    i += 1


num = [1,4,9,12,3,4,5,6,7,8]
idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1

num1 = (1,4,9,12,3,4,5,6,7,8)
x = int(input('Number --> '))
i = 0
while i < len(num1):
    if (num1[i] == x):
      print('Found At Index -->',i)
    i += 1

i = 1
while(i <= 5):
    print("Tridev Sharma")
    i += 1
for j in range(1,6):
    print("Prem Sharma")
for k in range(1,11):
    print("5 x", k , "=" , 5*k)
for m in range(1,11):
    print("7 x", m , "=" , 7*m)
for n in range(1,21):
    print("9 x", n , "=" , 9*n)
for p in range(1,16):
    print("12 x", p , "=" , 12*p)
for q in range(1,11):
    print("15 x", q , "=" , 15*q)
#break and continue
for r in range(1,11):
    if(r == 5):
        break
    print("Break Example :", r) 
for s in range(1,11):
    if(s == 5):
        continue
    print("Continue Example :", s)  
#nested loop
for a in range(1,4):
    for b in range(1,4):
        print("a =", a , " b =", b)     
#pattern printing
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=' ')
    print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=' ')
    print()
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,i+1):
        print("*", end=' ')
    print()
for i in range(5,0,-1): 
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,i+1):
        print("*", end=' ')
    print()
for i in range(1,6):
    for j in range(1,6):
        if(j <= 6 - i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for i in range(5,0,-1):
    for j in range(1,6):
        if(j <= i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for i in range(1,6):
    for j in range(1,6):
        if(j >= i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for i in range(5,0,-1):
    for j in range(1,6):
        if(j >= 6 - i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for i in range(1,6):    
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,2*i):
        print("*", end=' ')
    print()
for i in range(5,0,-1):    
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,2*i):
        print("*", end=' ')
    print()
for i in range(1,6):    
    for j in range(1,6):
        if(j <= 6 - i):
            print(" ", end=' ')
        else:
            print("*", end=' ')
    for k in range(2, i+1):
        print("*", end=' ')
    print()
for i in range(5,0,-1):   
    for j in range(1,6):
        if(j <= i - 1):
            print(" ", end=' ')
        else:
            print("*", end=' ')
    for k in range(2, i+1):
        print("*", end=' ')
    print()
for i in range(1,6):    
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,i+1):
        print("*", end=' ')
    for l in range(2,i+1):
        print("*", end=' ')
    print()
for i in range(5,0,-1):   
    for j in range(5,i,-1):
        print(" ", end=' ')
    for k in range(1,i+1):
        print("*", end=' ')
    for l in range(2,i+1):
        print("*", end=' ')
    print()
for i in range(1,6):    
    for j in range(1,6):
        if(j <= 6 - i):
            print(" ", end=' ')
        else:
            print("*", end=' ')
    for k in range(2, i+1):
        print("*", end=' ')
    for l in range(2, i+1):
        print("*", end=' ')
    print()
for i in range(5,0,-1):   
    for j in range(1,6):
        if(j <= i - 1):
            print(" ", end=' ')
        else:
            print("*", end=' ')
    for k in range(2, i+1):
        print("*", end=' ')
    for l in range(2, i+1):
        print("*", end=' ')
    print()
#factorial of number
num = float(input("Enter Number --> "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial of", num , "is", factorial)
#factorial using while loop
num = int(input("Enter Number --> "))
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1
print("Factorial of", num , "is", factorial)
#sum of n natural numbers
n = int(input("Enter Number --> "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum of first", n , "natural numbers is", sum)
#sum of n natural numbers using while loop
n = int(input("Enter Number --> "))
sum = 0 
i = 1
while i <= n:
    sum = sum + i
    i += 1
print("Sum of first", n , "natural numbers is", sum)
#reverse of number
num = int(input("Enter Number --> "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse of number is -->", reverse)
#check prime number
num = int(input("Enter Number --> "))   
is_prime = True
if num <= 1:
    is_prime = False
else:   
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")