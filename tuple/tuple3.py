def swap_elements(tuple):

    if len(tuple) < 2:
        return tuple
    first, *middle, last = tuple
    return (last, first)

