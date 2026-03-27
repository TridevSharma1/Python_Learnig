name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello",name,"You are",age,"years old.")
# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello", self.name, "You are", self.age, "years old.")
# create an object of the class
person1 = Person(name, age)
# call the method
person1.greet()
