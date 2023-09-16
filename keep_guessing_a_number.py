import random

random = random.randint(1, 10)
guess_number = int(input("Enter a number: "))

while guess_number != random:
    guess_number = eval(input("keep guess a number: "))
    if guess_number == random:
     print("correct, you won")