total = 0
counter = 0

grade = int(input("Enter a grade, -2 to stop and run: "))
while grade != -2:
    total += grade
    counter += 1
    grade = int(input("Enter a grade, -2 to stop and run: "))

if counter != 0:
    average = total / counter
    print(f"class average is {average}")
else:
    print("no grade was entered")
