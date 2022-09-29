total = 0
number_of_items = int(input("number of items: "))
while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("number of items: "))
for item in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total += price_of_item
if total > 100:
    total *= 0.9
print(f"Total price for {number_of_items} items is ${total:.2f}")

