# my_playlist = []   #----------- declaring a list

number = [1, 2, 3, 4, 5]
print(number)

characters = ["A", "B", "C", "D"]
print(characters)

my_list = ["A", "B", "C", "D"]
print(len(my_list))

numbers = [1, 2, 3, 4, 5]
result = numbers[1] + numbers[2]
print(result)

n = 2
n = n + 4
id(n)  # ----------------------> memory location
print(n)
print(id(n))

numbers = [1, 2, 3, 4, 5]
result = numbers[2]
print(result)

numbers = [1, 2, 3, 4, 5]
characters = ["A", "B", "C", "D"]
result = numbers + characters  # ----------------------> Concertination
print(result)


letters = ["Joy"]
numbers = [1, 2, 3, 4, 5]
result = letters + numbers
print(result)