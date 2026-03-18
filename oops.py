class User_1:
     name = "Tridev"
     age = 18
     course = "BCA"

print("Name :", User_1.name)
print("Age  :", User_1.age)
print("Course  :", User_1.course)

class User_2:
    def user_info(self):
        print("Name : Tridev")
        print("Age : 18")
        print("Course : BCA")
user2 = User_2()
user2.user_info()

class User_3:
    def user_info(self, name, age, course):
        print("Name :", name)
        print("Age  :", age)
        print("Course  :", course)

user3 = User_3()
user3.user_info("Tridev Sharma", 18, "BCA")

# 02/02/2026

# Oops Concepts in Python
class User_4:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def user_info(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Course  :", self.course)
user4 = User_4("Tridev Sharma", 18, "BCA Ai & Ml")
user4.user_info()

# Encapsulation
class User_5:
    def __init__(self, name, age, course):
        self.__name = name
        self.__age = age
        self.__course = course

    def user_info(self):
        print("Name :", self.__name)
        print("Age  :", self.__age)
        print("Course  :", self.__course)
user5 = User_5("Tridev Sharma", 18, "BCA Ai & Ml")
user5.user_info()
print(user5.__name) # AttributeError: 'User_5' object has no attribute '__name'

# Inheritance
class User_6:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def user_info(self):
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Course  :", self.course)
class Student(User_6):
    def __init__(self, name, age, course, roll_no):
        super().__init__(name, age, course)
        self.roll_no = roll_no

    def student_info(self):
        print("Roll No :", self.roll_no)
student = Student("Tridev Sharma", 18, "BCA Ai & Ml", 101)
student.user_info()
student.student_info()



