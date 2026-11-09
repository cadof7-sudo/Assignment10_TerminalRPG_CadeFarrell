from item import ITEMS

def visit_shop(player):
    while True:
        print(f"\nSHOP | Gold: {player.gold}")
        for name, data in ITEMS.items():
            print(f"- {name}: {data['price']} gold")
        print("Enter an item name to buy, or 'exit'.")
        choice = input("> ").strip()
        if choice.lower() == "exit":
            return
        if choice not in ITEMS:
            print("That item is not sold here.")
        elif player.gold < ITEMS[choice]["price"]:
            print("Not enough gold.")
        else:
            player.gold -= ITEMS[choice]["price"]
            player.inventory.append(choice)
            print(f"Purchased {choice}.")
