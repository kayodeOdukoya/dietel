numbers = [15, 20, 25, 20, 10, 5]

total = sum(numbers)
print("sum:", total)


product = 1
for number in numbers:
    product *= number
print("product:", product)


largest_number = max(numbers)
print(largest_number)


smallest_number = min(numbers)
print(smallest_number)


duplicate = set(numbers)
duplicate = list(duplicate)

print("duplicate:", duplicate)

