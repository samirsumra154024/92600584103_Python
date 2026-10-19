
# Write mode
with open("student.txt", "w") as f:
    f.write("Name: Samir\n")
    f.write("Course: MCA\n")

# Read mode
with open("student.txt", "r") as f:
    print("File Content:")
    print(f.read())

# Append mode
with open("student.txt", "a") as f:
    f.write("College: Marwadi University\n")

# Read updated content
with open("student.txt", "r") as f:
    print("Updated Content:")
    print(f.read())
