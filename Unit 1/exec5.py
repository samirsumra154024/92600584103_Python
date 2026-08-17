numbers=[10,20,30,40,50]
print("Original Numbers:",numbers)

print("Number First:",numbers[1])
print("Number Third:",numbers[2])
print("Last Number:",numbers[-1])

print("Last three elements:",numbers[2:5])
print("First three elements:",numbers[0:3])
print("First element:",numbers[0])

numbers.append(60)
print("After appened:",numbers)

numbers.remove(10)
print("After remove:",numbers)

numbers[0]=25
print("After changing the value:",numbers)

squares=[x*x for x in numbers]
print("Squares Numbers are:",squares)

even_numbers=[x for x in numbers if x %2==0]
print("Even Numbers are:",even_numbers)