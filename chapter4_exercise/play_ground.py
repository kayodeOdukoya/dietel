import random

#SQUARE ROOT OF ANY NUMBER

# def square(number):
#     return number **2
# print(square(2.5))

     #MAXIMUM NUMBER

# def maximum(value1, value2, value3):
#     max_value = value1
#     if value2 > max_value:
#         max_value = value2
#     if value3 > max_value:
#         max_value = value3
#     return max_value
# print(maximum(12, 27, 36))


    #Produce 10 random integers in the range 1-6 to simulate rolling a six sided die?

# import random
#
# for roll in range(10):
#     print(random.randrange(1, 7), end= " ")

    #Rolling a 6 sided die 6,000,000 times.


# frequency1 = 0
# frequency2 = 0
# frequency3 = 0
# frequency4 = 0
# frequency5 = 0
# frequency6 = 0
#
# for roll in range(6_000_000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         frequency1 +=1
#     elif face == 2:
#         frequency2 += 1
#     elif face == 3:
#         frequency3 += 1
#     elif face == 4:
#         frequency4 += 1
#     elif face == 5:
#         frequency5 += 1
#     elif face == 6:
#         frequency6 += 1
#
# print(f'Face{"Frequency":>13}')
# print(f"{1:>4}{frequency1:>13}")
# print(f"{2:>4}{frequency2:>13}")
# print(f"{3:>4}{frequency3:>13}")
# print(f"{4:>4}{frequency4:>13}")
# print(f"{5:>4}{frequency5:>13}")
# print(f"{6:>4}{frequency6:>13}")


            #Dice game
# def roll_dice():
#     diel1 = random.randrange(1, 7)
#     diel2 = random.randrange(1, 7)
#     return (diel1, diel2)
# def display_dice(dice):
#    diel1, diel2 = dice
#    print(f"player rolled {diel1} + {diel2} = {sum(dice)}")
#
# die_values = roll_dice()
# display_dice(die_values)
#
# sum_of_dice = sum(diel2_values)
#
# if sum_of_dice in (7, 11):
#     game_status = "Won"
# elif sum_of_dice in (2, 3, 12):
#     game_status = "Lost"
# else:
#     game_status = "Continue"
#     my_point = sum_of_dice
#     print("point is", my_point)
#
# while game_status == "Continue":
#     die_values = roll_dice()
#     display_dice(die_values)
#     sum_of_dice = sum(die_values)
#
#     if sum_of_dice == my_point:
#         game_status = "WON"
#     elif sum_of_dice == 7:
#         game_status = "LOST"
#
# if game_status == "WON":
#     print("Player wins")
# else:
#     print("Player loses")


#SQUARE MATH MODULE FUNCTIONS

import math

n = math.sqrt(900)
print(n)

n = math.fabs(-10)
print(n)


#---------------------------------
def rectangle_area(length=2, width=3):
    return length * width
print(rectangle_area(2, 3))

n = rectangle_area()
print(n)

n = rectangle_area(10)
print(n)

n = rectangle_area(10, 5)
print(n)




