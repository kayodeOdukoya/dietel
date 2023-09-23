principal = int(input("Enter principal: "))
rate = int(input("Enter rate: "))
year = int(input("Enter numbers of years: "))
for year in range (1, 31):
    investment = principal *(1 + rate / 100) ** year
    print(f"year{year}, total return {investment:.2f}")