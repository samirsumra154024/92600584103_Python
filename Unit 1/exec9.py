
def greet():
    print("Hello, Welcome to Python!")
def add(a, b):
    print("Addition:", a + b)

def student(name, course="MCA"):
    print("Name:", name)
    print("Course:", course)

def details(name, age):
    print("Name:", name)
    print("Age:", age)

def total(*numbers):
    print("Total:", sum(numbers))

greet()

add(10, 20)

student("Samir")

student("Rahul", "BCA")

details(age=22, name="Samir")

total(10, 20, 30, 40)