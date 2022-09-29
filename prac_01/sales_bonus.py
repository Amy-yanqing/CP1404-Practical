"""
program to calculate and display a user's bonus base on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales:$ "))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.1
    else:
        bonus_rate = 0.15
    total_bonus = bonus_rate*sales
    print(f"your sales is {sales},your total bonus is {total_bonus:.2f}")
    sales = float(input("Enter sales:$ "))



