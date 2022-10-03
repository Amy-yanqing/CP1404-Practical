"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
"""
stock start price=10

get random volatile choice
get random volatile rate
calculate random stock price
get valid stock price
    while 0.01<= random stock price <= 1000
        get random volatile choice
        get random volatile rate
        calculate random stock price
    get valid stock price
display final stock price

"""

import random


def main():
    stock_price = 10
    number_of_days = 0
    update_stock_price = get_valid_price(stock_price)
    print(f"starting price:${stock_price}")
    while 1 <= update_stock_price <= 100:
        update_stock_price = get_valid_price(stock_price)
        stock_price = update_stock_price
        number_of_days += 1
        print(f"on day {number_of_days} price is ${update_stock_price:.2f}")
    print(f"Finish price is {stock_price:.2f}, on day {number_of_days} ")


def get_valid_price(stock_price):
    determine_value = determine_stock_volatile_result()
    rate = get_update_stock_price(determine_value)
    update_stock_price = determine_stock_price(stock_price, rate)
    return update_stock_price


def get_update_stock_price(determine_value):
    if determine_value == 1:
        volatile_rate = get_increase_rate()
        return volatile_rate

    else:
        volatile_rate = get_decrease_rate()
        return volatile_rate


def determine_stock_volatile_result():
    return random.randint(0, 1)


def get_increase_rate():
    increase_rate = random.uniform(0, 0.1)
    return increase_rate


def get_decrease_rate():
    decrease_rate = random.uniform(0, 0.05)
    return decrease_rate


def determine_stock_price(stock_price, volatile_rate):
    stock_price *= 1 + volatile_rate
    return stock_price


main()