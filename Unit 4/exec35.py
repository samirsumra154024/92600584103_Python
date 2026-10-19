
# Single Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")

obj = B()
obj.show()
obj.display()

# Multilevel Inheritance
class C(B):
    def message(self):
        print("Class C")

obj2 = C()
obj2.show()
obj2.display()
obj2.message()

# Multiple Inheritance
class X:
    def method_x(self):
        print("Class X")

class Y:
    def method_y(self):
        print("Class Y")

class Z(X, Y):
    pass

obj3 = Z()
obj3.method_x()
obj3.method_y()
