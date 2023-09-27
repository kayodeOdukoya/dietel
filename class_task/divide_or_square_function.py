# import math
# def divide_or_square(number):
#     if number % 5 == 0:
#         return math.sqrt(number)
#     else:
#         return number % 5
# print(f"{divide_or_square(10):.2f}")

                        #OR
# import math
# def divide_or_square(number):
#     if number % 5 == 0:
#         return math.sqrt(number)
#     else:
#         return number % 5
# number = 10
# result = divide_or_square(number)
# print(result)

def square_or_root(number):
    numbers=number**0.50
    if number%5==0:
        return numbers
    elif number%5!=0:
        return numbers

resolve=(square_or_root(10))
print(f'{resolve:.2f}')


