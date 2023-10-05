
#LIST DECLARATION

# my_playlist = []
#
# names = ["arua", "Joy", "Qudus", "Ope"]
# print(names)
#
# #LIST WITH INBUILD FUNCTION
# names2 = list("Isreal")
# print(names2)
#
# placelist = ['west_life', 'barister, akin']
#
# #OR
#
# ['west_llfe, barrister', akon]
# letter = list ('abcdefghij')
# letters ['a', 'b', 'c', 'd']
#
# numbers = list[12345678910]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
#
# li [10, 15, 20, 25, 30]
# li[2] + l1[4]
# # -----> 50
#
# li [10, 15, 20, 25, 30]
# li[2] #-------------> 45
#
# li [10, 15, 20, 25, 30]
# li.append(55)
# #li ------------> [10, 15, 45, 25, 30, 55, 70]
#
# #TO SEE MEMORY LOCATION
#
# id(li)
# #------------> 263467839203
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [6, 7, 8, 9, 10]
#
# numbers1 + numbers2
# [1,2,3,4,5,6,7,8,9,10]
# #To see the id of numbers1 or memory address
# id(numbers1)
# 16789364709821 #----> Memory location.
#
# #to modify numbers1
# numbers1.append(11)
# [1, 2, 3, 4, 5, 11]





#EXAMPLE:
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1[2]
for i in range(len(l1)):
    print(i)

#LIST IS ENTEROGENIOUS: It can take all type at once.
list3 = [1, 1.2, 'Kay', True]
print(list3)

#LIST CAN BE CONCARTINATE: Left is List while right must be Iterable
list3 += 'Gist'
name = 'Kay'
print(list3)

#SLICING: Start, Stop, Step.
kay = list3[2:7:2]
print(kay)

kay = list3[2::2]
print(kay)

kay = list3[4::4]
print(kay)

kay = list3[2:7:2]
print(kay)