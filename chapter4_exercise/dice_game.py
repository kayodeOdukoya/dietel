import random
#Dice game

def roll_dice():
    diel1 = random.randrange(1, 7)
    diel2 = random.randrange(1, 7)
    return (diel1, diel2)
def display_dice(dice):
   diel1, diel2 = dice
   print(f"player rolled {diel1} + {diel2} = {sum(dice)}")

die_values = roll_dice()
display_dice(die_values)

sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):
    game_status = "Won"
elif sum_of_dice in (2, 3, 12):
    game_status = "Lost"
else:
    game_status = "Continue"
    my_point = sum_of_dice
    print("point is", my_point)

while game_status == "Continue":
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = "WON"
    elif sum_of_dice == 7:
        game_status = "LOST"

if game_status == "WON":
    print("Player wins")
else:
    print("Player loses")

