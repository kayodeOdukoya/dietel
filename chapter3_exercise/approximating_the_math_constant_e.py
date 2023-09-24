user_input = 5
divide = 1
sum = 1
product = 1
count = 1
while count <= user_input:
    product *= count
    divide /= product
    sum += divide
    count += 1
print(f"the sum is: {sum:.2f}")