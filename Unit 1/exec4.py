# Program to demonstrate string operations

# Input string
name = input("Enter your name: ")

# Slicing
print("\n--- String Slicing ---")
print("Original String :", name)
print("First 3 characters :", name[:3])
print("Last 3 characters :", name[-3:])
print("Characters from index 2 to 5 :", name[2:6])

# String Formatting
age = int(input("\nEnter your age: "))
print("\n--- String Formatting ---")
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# Built-in String Functions
print("\n--- Built-in String Functions ---")
print("Upper Case :", name.upper())
print("Lower Case :", name.lower())
print("Length :", len(name))
print("Replace 'a' with '@' :", name.replace('a', '@'))
print("Starts with 'S' :", name.startswith('S'))
print("Ends with 'r' :", name.endswith('r'))
print("Is Alphabetic :", name.isalpha())