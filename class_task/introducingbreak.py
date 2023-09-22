even_numbers = []
for c in range(0, 51, 2):
    if c == 20:
        break
    even_numbers.append(c)
print(even_numbers)
average = sum(even_numbers) / len(even_numbers)

print(average)