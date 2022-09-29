# print("Electricity bill estimator")
# cents_per_kwh = float(input("Enter cents per kwh:"))
# daily_use_kwh = float(input("Enter daily use in kwh:"))
# number_of_days = int(input("Enter number of billing days: "))
# dollar_per_kwh = cents_per_kwh / 100
# electricity_bill = dollar_per_kwh * daily_use_kwh * number_of_days
# print(f"Estimated bill:{electricity_bill}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

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
bills = dollar_per_kwh * daily_use_kwh * number_of_days
print(f"Estimated bill:{bills:.2f}")






