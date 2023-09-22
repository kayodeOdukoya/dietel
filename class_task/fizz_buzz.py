
                            #22//9/2023
  #TASK: Write a python  program that iterates the  integers from 1 to 50. For multiples of three, print "Fizz"instead  of thenumber
# and for four multiples  of five, print  "Buzz".  For numbbers  that  are multiples of three and five, print "Fizzuzz"

for multiples in range(50):
    if multiples % 3 == 0 and multiples % 5 == 0:
        print("fizbuzz")
        continue
    elif multiples % 3 == 0:
        print("fizz")
        continue
    elif multiples % 5 == 0:
        print("buzz")
        continue
    print(multiples)

count = 1
