#string operations

str1 = 'Tridev Sharma'
str2 = "Tridev Sharma"
str3 = """Tridev Sharma"""

print(str1 + " " + str2)
print(len(str1 + str2 + str3)) #length

print(str1[0 :len (str1)]) #slicing

print(str1.endswith("ma")) #checking

print(str2.capitalize()) #capitalize

print(str3.replace("Tridev" , "Prem")) #Replacing

print(str1.find('v')) 

print(str2.count('a'))

#conditional Statment

a = int(input("First No "))
b = int(input("Second No "))

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

mark =  int(input("Marks --> ",  )) 

if(mark >= 90):
    Mark = "A"
elif(mark >= 80 and mark < 90 ):
    mark = "B"
elif(mark >= 70 and mark <= 80):
    mark = "C"
elif(mark >= 69):
    mark = "D"
elif(mark < 40):
    mark = "Fail"

print(mark)