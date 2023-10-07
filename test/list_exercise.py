def add_function(numbers: list):
    total = 0
    for count in numbers:
        total += count
    return total

def multiply_function(numbers: list):
        #total = 1
    # for count in numbers:
    #     total *= count
    # return total

        #or

    product = 1
    for number in numbers:
        product *= number
    return product

def find_largest(numbers):
    largest_number = 0
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

def find_smallest(numbers):
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

# def no_duplicate(numbers):




