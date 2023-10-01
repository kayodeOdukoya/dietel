# product = 7
# while product <= 1000:
#     print(product)
#     product = product * 7



# score = int(input("Enter score: "))
#
# if  90 <= score <= 100:
#     result = ("A")
#
# elif 80 <= score <= 89:
#     result = ("B")
# elif 70 <= score <= 79:
#     result = ("C")
# elif 60 <= score <= 69:
#     result = ("C2")
# elif 50 <= score <= 59:
#     result = ("D")
# else:
#     result = ("fail" "\n" "retake")
#
# print(result)

# result = 4
# while result <= 40:
#     print(result)
    #result = result * 2
    #result += 2
                                                #FOR LOOP
# for character in "programming":
#     print(character, end="   ")
                                #average of class result.
total = 0
counter = 0

# grade = int(input("Enter a grade, -2 to stop and run: "))
# while grade != -2:
#     total += grade
#     counter += 1
#     grade = int(input("Enter a grade, -2 to stop and run: "))
#
# if counter != 0:
#     average = total / counter
#     print(f"class average is {average}")
# else:
#     print("no grade was entered")

# def multiply(*args):
#     product = 1
#     for i in args:
#         product *= 1
#     return product
# print(multiply(2))


                                    #FUNCTIONS
    #Declear a function that collect 10 numbers from user and print out the average.

                                    #29/9/2023
# def average_score(scores):
#     return sum(scores) / len(scores)
#
#
# exam_scores = []
# for i in  range(10):
#     score =  int(input("Enter the scores: "))
#     exam_scores.append(score)
#
# print(average_score(exam_scores))


                                    #OR FOR *args

# def average_score(*scores):
#     return sum(scores) / len(scores)
#
# print(average_score(1 , 2, 3, 5, 10))

                                    #OR

def average_score(*scores):
    total = 0
    for i in  scores:
        total += i

    return total / len(scores)

print(average_score(1 , 2, 3, 5, 2, 2, 2, 2, 2, 2))

