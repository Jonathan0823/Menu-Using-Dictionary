foods = {"popcorn": 6.44,
    "pizza": 3.99,
    "potato": 1.99,
    "nacho": 4.99,}

quantities = []
cart = []
total = 0
ordered_num=0

while True:
    print("\n------------Menu---------------")
    for food in foods:
        print(f"{food:10}: ${foods[food]}")
    print("-------------------------------\n\n")
    print("------------Cart---------------")
    print("Your order are: ")
    for i in range(ordered_num):
        print(f"{cart[i]:10}: {quantities[i]}")
    print("-------------------------------\n\n")

    item = input("What would you like to order? (q to quit): ")

    if item.lower() == "q":
        break
    elif item not in foods:
        print(f"{item} is not on the menu")
        continue
    else:
        quantity = int(input(f"How many {item} would you like? "))
        cart.append(item)
        quantities.append(quantity)
        total += foods[item] * quantity
        ordered_num+=1


print(f"Your total is: ${total:.2f}")