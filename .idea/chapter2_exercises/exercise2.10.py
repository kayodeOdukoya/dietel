
number1 = int(input("input first integer: "))
number2 = int(input("input second integer: "))
number3 = int(input("input third integer: "))

largest = 0
smallest = number1 + number2 + number3

sum = number1 + number2 + number3
average = number1 / number2 / number3
product = number1 * number2 * number3

if number1 > largest:
    largest = number1

if number2 > largest:
    largest = number2

if number3 > largest:
    largest = number3

if number1 < smallest:
    smallest = number1

if number2 < smallest:
    smallest = number2

if number3 < smallest:
    smallest = number3

print(largest, '\n', smallest, '\n')
print(sum, '\n', average, '\n', product)
