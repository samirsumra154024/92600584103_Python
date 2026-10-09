import re

with open("details.txt", "r") as f:
    text = f.read()

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
)

phones = re.findall(r"\b\d{10}\b", text)

print("Email addresses:", emails)
print("Phone numbers:", phones)