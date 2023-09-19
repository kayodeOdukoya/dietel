user_input = int(input("Enter invested amount: "))
year = 0
invested_amount = 10/100
for count in range(1, 31):
    profit = user_input
    profit *= invested_amount
    user_input += profit
    print(f"your Roi is {profit:.2f}, Your investment is now ${user_input:.2f} in year {count}")