number = int(input("Enter a number: "))
result = 1
for count in range (number, 0, -1):
    result *= count
print(f"factorial of {number} equals {result}")

