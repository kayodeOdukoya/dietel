#
# number = [10, 20, 15, 25, 5, 30, 35, 20, 10, 9, 20]
# print("Origina list:", number)
#
# for i in range(0, len(number)):
#     for j in range(i+1, len(number)):
#         if number[i] > number [j]:
#             number[i], number[j] = number[j], number[i]
#
# print("arranged list", number)
#
# if len(number) % 2 == 0:
#     mid1 = len(number) // 2
#     mid2 = mid1 - 1
#     median = (number[mid1] + number[mid2]) / 2
# else:
#     mid = len(number) // 2
#     midian = number[mid]
# print(midian)


# import calendar
# import statistics


#OR
ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20,]
for i in range(0, len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[i]  > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)
l = len(ls)

if l % 2 == 0:
    m1 = ls[l // 2]
    m2 = ls[(l // 2) - 1]
    mid = (m1 + m2) / 2
    print(mid)
else:
    mid = ls[l // 2]
    print(mid)

total = 0
for a in ls:
    total += a
mean = total/l
print(mean)


# ls = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20,]
# ls.sort()
# print(ls)
#
# statistics.mean(ls)
# statistics.median(ls)
# statistics.mode(ls)
# print(ls)

