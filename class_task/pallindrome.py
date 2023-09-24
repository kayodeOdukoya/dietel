#TASK
#CREATE A PALINDROME PROGRAMME called is_palindrome. If user input a number, print true, "It's Palindrome", false, "Its not palindrome"

# count = 1
#
#
# def is_palindrone(number):
#     result = count
#     returning = 0
#     while number != 0:
#         value = number % 10
#         returning = returning * 10 + value
#         number = number // 10
#         if returning == result:
#             return True
#         else:
#             return False
# print(is_palindrone(11222213))



                                        #OR
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print(is_palindrome(12223))