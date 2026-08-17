# Tuple
numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])


print("Sliced tuple:", numbers[1:4])

print("Length of tuple:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("\nSet 1:", set1)
print("Set 2:", set2)

set1.add(70)
print("After adding 70:", set1)

set1.remove(20)
print("After removing 20:", set1)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference:", set1.difference(set2))