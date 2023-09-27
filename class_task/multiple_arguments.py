#IT'S USED WHEN WE ARE NOT SURE OF THE NUMBERS OF ARGUMENTS OR PARAMETERS THAT USER'S WILL IMPUTTED.
def my_sum(* numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(my_sum(2, 3, 4, 5, 6, 7, 8, 20, 30))