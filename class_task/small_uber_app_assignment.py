import sys

scores = []

for count in range(1, 11):
    try:
        score = int(input("Enter a score {}: ".format(count)))
        scores.append(score)
    except ValueError:
        print("Invalid input. Please enter a valid score.")
        sys.exit(1)
print(scores)

largest = scores[0]
for score in scores:
    if score > largest:
        largest = score

print("The largest number is:", largest)
