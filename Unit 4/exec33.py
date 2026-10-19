
class Student:
    college = "Marwadi University"

    def __init__(self, name):
        self.name = name

s1 = Student("Samir")
s2 = Student("Rahul")

print("Student 1:", s1.name)
print("Student 2:", s2.name)
print("College:", Student.college)
