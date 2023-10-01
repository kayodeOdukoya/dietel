
                                        #FUNCTIONS
                                        #ARBITUARY FUNCTION.

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

# def average_score(*scores):
#     total = 0
#     for i in  scores:
#         total += i
#
#     return total / len(scores)
#
# print(average_score(1 , 2, 3, 5, 2, 2, 2, 2, 2, 2))


                #DIFFERENT BETWEEN BLOCK AND SUITE.
# def me(name, number: int, age: int = 18) -> str:
#     x = 2 + 3
#  x                                            # ---------> Block: x brings error
#pass


# name = "joe"
# if name:
#     x = 2 + 3                                  # ----------> Suit: x did not bring error.
# x


                #POSITIONAL AND KEYWORD ARGUMENTS
def me(name, number: int, age: int = 18) -> str:

    me("joy", 20000, 21)                    # --------- > positional Arguments
    me(number= 2323, age= 21, name= "joy")   #--------------> Keyword Arguments
    me(2222, name= "joy")                     # -------------> Positional and Keyword Arguments.