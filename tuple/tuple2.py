def get_method(numbers):

    result = []
    outer_number = 0

    for sub_number in numbers:
        inner_index = 0
        for item in sub_number:
            if item in (20, 25):
                result.append((outer_number, item))
            inner_number += 1
        outer_number += 1

    return tuple(result)

