TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_to_cost = {}

print("Electricity bill estimator 2.0")

dollar_per_kwh = 0
daily_use_kwh = float(input("Enter daily use in kwh:"))
number_of_days = int(input("Enter number of billing days: "))
choice = input("which tariff? 11 or 31 ")
if choice == "11":
    dollar_per_kwh = TARIFF_11
elif choice == "31":
    dollar_per_kwh = TARIFF_31
else:
    print("Invalid choice")
tariff_to_cost[choice] = dollar_per_kwh * daily_use_kwh * number_of_days
print(f"{tariff_to_cost}")
