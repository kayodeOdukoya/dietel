number = int(input("Enter a number: "))
highest = number
lowest = number
counter = 1
count = 0
sum = number
product = number

for counter in range(1, 4):
    number = int(input("Enter a number: "))
    count += 1
    sum += number
    product *= number
average = sum / count
if (number > highest):
    highest = number
if (number < lowest):
    lowest = number
print(f"{sum}")
print(f"{product}")
print(f"{average}")
print(f"{highest}")
print(f"{lowest}")