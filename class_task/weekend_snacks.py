class ArraySnacks:


    def the_largest_number(array):
        largest = array[0]
        for index in range(1, len(array)):
            if array[index] > largest:
                largest = array[index]
        return largest


    def reverse_list(array):
        length = len(array)
        reverse = [0] * length
        for index in range(len(array)):
            reverse[index] = array[length - 1 - index]
        return reverse


    def check_element(array, value):
        check = False
        for element in array:
            if element == value:
                check = True
                break
        return check


    def sum_of_for_loop(array, total):
        sum_result = 0
        count = 0
        for count in range(total):
            sum_result += array[count]
        return sum_result


    def sum_while_loop(array, total):
        sum_result = 0
        count = 0
        while count < total:
            sum_result += array[count]
            count += 1
        return sum_result


    def sum_do_while_loop(my_array, total):
        sum_result = 0
        count = 0
        while count < total:
            sum_result += my_array[count]
            count += 1
        return sum_result


array = [1, 3, 5, 7, 9]
print(ArraySnacks.the_largest_number(array))
print(ArraySnacks.reverse_list(array))
print(ArraySnacks.check_element(array, 5))
print(ArraySnacks.sum_of_for_loop(array, 3))
print(ArraySnacks.sum_while_loop(array, 2))
print(ArraySnacks.sum_do_while_loop(array, 4))
