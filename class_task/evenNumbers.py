# for number in range(1, 51):
#
#     if number % 2 == 0:
#         print(number, end=" ")
#
                                #OR

# for c in range(0, 51, 2):
#     print(c, end=" ")
                        #To calculate the average
# count = 0
# total = 0
# for c in range(0, 51, 2):
#     count +=1
#     total+= c
#     print (f"{total/count}")

                            #OR
# even_numbers = []
# for c in range(0, 51, 2):
#     even_numbers.append(c)
# print(even_numbers)
# average = sum(even_numbers) / len(even_numbers)
#
# print(average)

                            #INTRODUCING BREAK
even_numbers = []
for c in range(0, 51, 2):
    if c == 20:
        break
    even_numbers.append(c)
print(even_numbers)
average = sum(even_numbers) / len(even_numbers)

print(average)