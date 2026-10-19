
with open("data.txt", "w+") as f:
    f.write("Hello Python")

    print("Position:", f.tell())

    f.seek(0)
    print("After seek:", f.tell())

    print("Data:", f.read())

    f.seek(6)
    print("New Position:", f.tell())

    print("Remaining Data:", f.read())
