decimal_equivalent = 0
bit = 1
binary_integer = int(input("Enter a binary integer: "))
while binary_integer !=0:
    decimal_equivalent = decimal_equivalent + binary_integer % 10 * bit
    binary_integer = binary_integer / 10
    bit *= 2
print("the decimal equivalent is: ", decimal_equivalent)