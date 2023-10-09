
def reverse_tuple(self, tuple_to_reverse):
    reversed_list = []
    for item in tuple_to_reverse:
        reversed_list.insert(0, item)
        return tuple(reversed_list)

    def create_single_element_tuple(self, value):
        return (value,)

# why do you make single tuple function inner function ??
