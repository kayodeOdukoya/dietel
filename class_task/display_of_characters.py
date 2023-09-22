# picture = [
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 1, 1, 1, 0, 0],
# [0, 1, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1, 1],
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0],
# [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for every 0 display '' and for every 1 display *
#
# for picture in range (1, 7):
#     for picture in range (1, 7):
#         for picture in range (1, 7):
#             print()


# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for row in picture(0, 7):
#     if row == 0:
#         print(' ', end= '')
#     else:
#       print('*', end= ' ')
#     print()



                        #OR
# for every 0 display '' and for every 1 display *

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
#
# for numbers in picture:
#     for count in numbers:
#         if count == 0:
#             print(' ', end=' ')
#         else:
#             print('*', end=' ')
#     print()


                    #OR
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for pixel in picture:
    for img in pixel:
        if img == 0:
            print(" ", end=' ')
        else:
            print("*", end=' ')
    print()