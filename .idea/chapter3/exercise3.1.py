passes = 0
failures = 0


while True:
    try:
        user_input = int(input("Enter 1 for pass or 2 for fail (-1 to exit): "))

        if user_input == -1:
            break
        elif user_input == 1:
            passes += 1
        elif user_input == 2:
            failures += 1
        else:
            print("Invalid input. Please enter 1 for pass or 2 for fail.")

    except ValueError:
        print("Invalid input. Please enter 1 for pass or 2 for fail.")

total_tests = passes + failures
print(f"Total tests: {total_tests}")
print(f"Passes: {passes}")
print(f"Failures: {failures}")


