price = 50
total = 0

while total < price:

    try:
        coin = int(input("Insert Coin: "))
    except ValueError:
        print("Please insert a valid integer coin")
        continue

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {price - total}")
        continue

    total += coin

    if total < price:
        print(f"Amount Due: {price - total}")

change = total - price
print(f"Change Owed: {change}")