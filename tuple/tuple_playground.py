
tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x, *others, y = tuple
print(x, others, y)

print(tuple[2:7:2])

names = ["arua", "joy", "qudus", "ope"]
del names[1]
print(names)

del names[:]
print(names)

names.sort()
print(names)

names.sort(reverse= True)
print(names)

names.append("Precious")
print(names)

n = sorted((11, 7, 5, 3, 1), reverse=True)
print(n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers *= 1
# print(numbers.index(5, 7))

tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x, *others, y = tuple
print(x, others, y)

print(tuple[2:7:2])

name = ["arua", "joy", "qudus", "ope"]

name.pop(2)
print(names)

