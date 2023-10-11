def sorted_tuple(numbers):

    result = []

    for count in numbers:
        result.append(count)
    result.sort(key=lambda x: x[1])

    return tuple(result)

