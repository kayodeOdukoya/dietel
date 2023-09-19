import random  #LENGTH OF NAMES
# name = 'Odukoya'
# print(len(name))


            #PASSWORD

# password = input("input your password: ")
# print(len(password) * "*")




            #Collect input from user & convert to integer from string.

# number = input("Enter a number: ")
# convert = int(number)
# r = (convert + 1)
# print(r)




            #INDETATION ----------- Snake Case.

# first_name = 'Joy'
# second_name = 'Precious'
# print(first_name, second_name)

                    #Collecting input from user.

# first_name = input("Enter 1st name: ")
# second_name = input("Enter second name: ")
# print(first_name, second_name)

                    #Or

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# full_name = (first_name + ' ' + ' ' + last_name)
# print(full_name)


            #ESCAPE CHARACTER
# message = "it's python"
# print(message)
#                 #Or
# message = 'it\'s python'
# print(message)




                #RULES OF OPERATORS: MULTIPLICATION, DIVISION, FLOOR DIVISION, ADDITION AND SUBTRACTION.
# print(2 * 2 * 2 * 2)
# print(6 / 3)
# print(6 // 3)
# print(6 % 3)
# print(6 + 3)
# print(6 - 3)

# num1 = int('1')
# num2 = 2
# print(num1 + num2)
# print(2 + 3 * 4 / 2 ** 4)





            #VARIABLES
# message1 = 'hello'
# message2 = 'welcome'
# message3 = 'xplorers'
# print(message1 + ' ' + message2 + ' ' + message3)

# #---- FORMATTING OUR STRINGS BY PASSING OUR VARIABLES INSIDE PLACEHOLDER {} FOR ESCAPE #CONCARTINATION
# message1 = 'hello'
# message2 = 'welcome'
# message3 = 'xplorers'
# # msg = (f'{message1}\n{message2}\n{message3}')
# # print(msg)
                    #OR
# msg = f'{message1} {message2} {message3}'
# print(msg)
                    #OR
# msg = f'{message1 + " how are you"}\t{message2}\t{message3}'
# print(msg)
#             #ANOTHER WAY OF PASSING ESCAPE CHARACTER
#print(message1 + ' ' + message2 + ' ' + message3, end='\n')
                #or
#print(message1 + ' ' + message2 + ' ' + message3, end='\t')




                        #MULTI LINE STRING
# long_string = """
#                 alfred and joy
#                 ope and qudus
#                 dike and melody"""
# print(long_string)

                        #OR BY FORMATTING IT
# print(f"""
#                 alfred and joy
#                 ope and qudus
#                 dike and melody""")



                        #DECISION MAKING OR COMPARISON OPERATOR (IF STATEMENT)
# age = int(input("Enter your age: "))
# if age < 18:
#     print("you're not eligible to enter our club...")
# if age >= 18 and age <=65:
#     print("you are eligible to enter our club...")
#                         #TO SET RANGE
# if age > 65:
#     print("Stay at home...")

                        #IF ELSE

# age = int(input("Enter your age: "))
# if age < 18:
#     print("you're not eligible to enter our club...")
# else:
#     print("you are eligible to enter our club...")


                        #LOGICAL OPERATOR (IF Elif or ifelse, ELSE)

# age = int(input("Enter your age: "))
# if age < 18:
#     print("you're not eligible to enter our club...")
# elif age >= 18 and age <=65:
#      print("you are eligible to enter our club...")
# else:
#     print("Stay at home...")


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
#
# largest = 0
# # lowest = 0
#
# if number1 >= largest:
#     largest = number1
# if number2 >= largest:
#     largest = number2
# if number3 >= largest:
#     largest = number3

# if number1 < lowest:
#     lowest = number1
# if number2 < lowest:
#     lowest = number2
# if number3 < lowest:
#     lowest = number3

# print(largest)
# print(lowest)



# if number1 >= largest:
#     largest = number1
#
# if number2 >= largest:
#     largest = number2
#
# if number3 >= largest:
#     largest = number3
#
# print(largest)

                                #2ND CLASS IN PYTHON 9/8/2023

                        #Selection statements

# if i == 0:
#     print(i)
# if i == 5:
#     print("Five")
# if i == 10:
#     print("Ten")

# Converting it to Selection

# if  i == 0:
#     print(i)
# elif i == 5:
#     print("Five")
# elif i == 10:
#     print("Ten")





                                        #8TH OF SEPTEMBER 2023.

                        #REPITITION
                  #MATCH CASE IN PYTHON BUT SWITCH CASE IN JAVA
# language = input("Enter a language: ")
# match language:
#     case "Yoruba":
#             print("Welcome to Ogun State")


#Example:

# language = input("Enter a language: ")
# if language == 'Yoruba':
#     print('Yoruba')
# elif language == 'Ibo':
#     print('Ibo')
# else:
#     print("Not available")


                            #Example: conditional statement: if + elif + else

# age = int(input("Enter age: "))
# if age < 18:
#     print("You are not eligible to enter our club.... ")
# elif age >= 18 and age <=60:
#     print("Eligible")
# else:
#     print("Not Eligible")


                                #USING DIFFERENT elif STATEMENTS
# score = int(input("Enter your score: "))
# # result *= 10
# result = ""
# if  90 <= score <= 100:
#     result = "Distinctions"
#
# elif 80<= score <= 90:
#     result = "Excellent"
#
# elif 70 <= score < 80:
#     result = "B grade"
#
# elif 60 <= score < 70:
#     result = "C1 grade"
#
# elif 50 <= score < 60:
#     result = "C2 grade"
#
# elif 40 <= score < 50:
#     result = "D grade"
#
# else:
#     result = "fail, come back next year"
#
# #print(result)

                    #or

# print(f"Your score is= {score}\nand your result is= {result}")

                    # or
# print(f"""
#             ---------
#             Your score is= {score}
#             ----------------------
#             \nand your result is= {result}""")


                                #BOOLEAN (True or False)
# print(bool(0))
# print(bool(5))
# print(bool(''))
# print(bool('fhfhfhfh'))

                                #True Output: Because the String has a value to input name

# name = input("Enter your name: ")
# if name:
#     print(f"your name is {name}")
#     print("Second line")
#     print("Third line")
#     print("Fourth line")
#     print("etc.")
# else:
#     print("no name entered")

                              #False Output: Cos the String has no value to input a name due to empty parenthesis, it result in false
# name = print()
# if name:
#     print(f"your name is {name}")
# else:
#     print("no name entered")



                                #Using tenary Operation for the above

# result = "Not Eligible" if age < 18 else "Eligible"
# print(result)



                                # USING SWITCH CASE:::::: MATCH CASE
# language = input("Enter a language: ")
# match language:
#     case "Yoruba":
#       print("welcome to Ibadan")
#     case "Ibo":
#        print("welcome to Anambra")
#     case "Hausa":
#         print("welcome to Kano")
#     case _:
#         print("You are not from Nigeria")



                                    #INTRODUCING UPPER/LOWER CASE INPUT USING .lower() or .upper()

# language = input("Enter a language: ")
# match language.lower():
#     case "yoruba":
#       print("welcome to Ibadan")
#     case "ibo":
#        print("welcome to Anambra")
#     case "hausa":
#         print("welcome to Kano")
#     case _:
#         print("You are not from Nigeria")


                                         #RANDOM & RANDINT
                                    #TO GENERATE NUMBERS.
                                    # USE RANDOM FUNCTION: IT'S USED TO HOLD A VARIABLE TEMPORARILY
# _precious = random.random()
# print(_precious)

# _precious = random.randint(21, 221)
# print(_precious)

                                        #PYTHON REPEATITIVE STATEMENT OR LOOP IN JAVA
                                        #TYPES OF LOOP IN PYTHON: FOR LOOP AND WHILE LOOP
                  #WHILE LOOP REPEAT A TASK AS LONG AS THE CONDITION IS TRUE. SET IT TO FALSE TO AVOID INFINITE LOOP.

# count = 0
# while count < 10:
#     print(random.randint(1, 21))

                            #OR
# count = 0
# while count < 10:
#     count += 1
#     print(random.randint(1, 21))

                            #OR

# count = 0
# while count < 10:
#     print(count)
#     count += 1

                            #OR
# count = 50
# while count >= 10:
#     print(count)
#     count -= 2            #This makes it to be false.
#


                            #TO INTRODUCE A COUNTER TO NUMBER IT "count"
# count = 0
# while count < 10:
#     print(count, random.randint(1, 21))
#     count += 1


# count = 1
# while count < 10:
#     print(count)
#     count += 1

                            #TASK: Play a game till it resolved to false.
# random = random.randint(1, 10)
# guess_number = int(input("Enter a number: "))
#
# while guess_number != random:
#     guess_number = eval(input("keep guess a number: "))
#     if guess_number == random:
#      print("correct, you won")





                                        #9/11/2023


                                            #OR
# guess_number = random.randint(1, 10)
# print(guess_number)
# guess = int(input("Enter your guess number between 1 and 10: "))
# while guess_number != guess:
#     guess = int(input("Enter your guess numbrer: "))
# print("You won")


                                    #TASK:*** Ask user for the score of 10 students....
                                    #Calculate the average of the score.

# score = 0
# students = 10
# count = 1
#
# while count <= students:
#     scores = int(input("Enter students scores: "))
#     if 0 <= scores <=10:
#         score += scores
#         count += 1
# average_score = score / count
# print(average_score)


# count = 1
# total = 0
# while count <=10:
#     score = int(input("Enter student score: "))
#     total += score
#     count += 1
# average = total / count
# print(average)

# desired_count = int(input("Enter the desired number of scores to input: "))

                        #To include Sentinel loop or value to stop the program e.g 0, -1, stop etc.

# total = 0
# count = 0
# score = int(input("Enter student score or -1 to stop: "))
# while score != -1:
#     score = int(input("Enter student score or -1 to stop: "))
#     total +=score                   #To store the score
#     count += 1                      #To increment the score to avoid infinity.
# average = total / count             #average formular.
# #print(average)
# print(f"{average:.2f}")             #To round up to 2 decimal places.


    #OR

# total = 0
# count = 0
# while True:
#     score = int(input("Enter student score or -1 to stop: "))
#     if score == -1:
#        break
#     total += score
#     count += 1
# average = total / count
# print(average)



              #TASK: MULTIPLE OF 6 THAT IS LESS THAN 3000 ON A STRAIGHT LINE.
# number = 1
# while number <=10
#     when = number * 5
#     print(when, end=" ")
#     number += 1

# number = 1
# while True:
#     number = number * 6
#     if number >= 3000:
#         break
#     print(number, end=" ")



                            #14/9/2023
                            #Taskumber = int ("0 to 6")

                               #TASK
# Write a program that prints all the numbrs between 0 to 6, except 3 and 6
                              #SOLUTION.
# count = 0
# while count <= 6:
#       if count != 3 and count !=6:
#             #print(count, end="\t")
#             print(f"{count}", end=" ")
#       count +=1

                            #FOR LOOP

#Using for loop
                                     #TASK
#Write a program that prints all the numbrs between 0 to 6, except 3 and 6

# for count in range (7):
#       if count != 3 and count != 6:
#           print(count, end="\t")


#1
# for i in "sikiru":
#     print(i)


#2
# for i in "sikiru":
#     print(i, "*")

#3
# for i in "sikiru":
#     print("muyiwa")

#4
# for i in range(10):
#     print(i)


#5
# for i in range(10):
#     print(i, "*")


#6
# for i in range(10):
#     print("muyiwa")


#7: pass is to ignore
# for i in range(10):
#     pass


#8
# for i in range(10):
#     print(i, end=" ")



#9: to start from 1 instead of 0
# for i in range(10):
#       print(i+1)


#10: to start from 5 instead of 0
# for i in range(10):
#       print(i+5)




#11
# for count in range(10):
#       if count == 8:
#             count += 1
#       print(count)

                                                #TASK

 # write a python prohram to count the number of even and odd numbers in a series of numbers
 # samples numbers: numbers = [1,2,3,4,5,6,7,8,9]
 # Expected Output:
 # Number of even numbers: 5
 # Number of odd numbers: 4

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# even = 0
# odd = 0
# for number in numbers:
#     if number % 2 == 0:
#      even += 1
# else:
#     odd+= 5
# print(f"Number of even numbers:",even, " \n", f"Number of odd numbers:", odd)





                                                                    #19/9/2023
                                                                    #TASK
               # MULTIPLICATION TABLE 1X1 TO 20X1

# for i in range(1, 13):
#     for j in range(2, 21):
#         print(f"{i:>2} * {j:>2} = {i * j:>2}", end="\t\t")
#     print()


# investment_initial = int(input("Enter investment amount: "))
# annual_interest = float(input("Enter annual investment amount: "))
# years = int(input("Enter number of years: "))
#
# for count in range (1, 31):
#     monthly_interest = annual_interest/12
#     months = years/12
#     future_years = investment_initial *(1 + annual_interest) **years
#     future_months = investment_initial * (1 + monthly_interest) **months
#     print("Value (monthly in $) is:", future_months)
#     print("Value (monthly in $) is:", future_years)
#     count += 1

user_input = float(input("Enter invested amount: "))
year = 0
invested_amount = 10/100
for count in range(1, 31):
    profit = user_input
    profit *= invested_amount
    user_input += profit
    print(f"your Roi is {profit:.2f}, Your investment is now ${user_input:.2f} in year {count}")


























