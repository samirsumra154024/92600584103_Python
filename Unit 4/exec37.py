
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()

print("MRO:", D.mro())

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s1 = Student("Samir")
print(s1)
