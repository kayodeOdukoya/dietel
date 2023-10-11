tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#numbers *= 2

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

names = ["arua", "joy", "qudus", "ope"]

# print(n.count(5))

print(all(numbers))
print(any(numbers))

def my_index(li: list, n, start = 0):
    index = 0
    for i in range(start, len(li)):
        if li[i] == n:
            index = i
    return index
print(numbers)
print(my_index(numbers, 3, 5))


def my_sort_func(list1: list, n):
    index = 0
    for i in range():
        return index
print(sorted(n))


numbers = [(range(1, 11))]
print(numbers)
def even_check(n):
    ans = 0
    if n % 2 == 0:
        ans = n
    return ans

# even_list = filter (even_check, n)
# print(list(even_list))

result = [i for i in range(1, 11) if i % 2 == 0]
print(result)

name = input("Enter your name: ")
if name:
    print(name)
