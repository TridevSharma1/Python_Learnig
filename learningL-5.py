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