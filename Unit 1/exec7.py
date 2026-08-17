# Create a dictionary
student = {
    "RollNo": 101,
    "Name": "Samir",
    "Course": "MCA",
    "Marks": 85
}

print("Original Dictionary:", student)

# Accessing values
print("Student Name:", student["Name"])

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Add a new item
student["Grade"] = "A"
print("After adding Grade:", student)

# Update an item
student["Marks"] = 90
print("After updating Marks:", student)

# Remove an item
student.pop("Grade")
print("After removing Grade:", student)

# Iteration through dictionary
print("\nDictionary Elements:")

for key, value in student.items():
    print(key, ":", value)