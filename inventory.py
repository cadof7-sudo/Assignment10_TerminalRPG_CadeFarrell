from item import use_item

def show_inventory(player):
    if not player.inventory:
        print("Your inventory is empty.")
        return
    for index, item in enumerate(player.inventory, 1):
        print(f"{index}. {item}")
    choice = input("Use an item number, or press Enter to go back: ").strip()
    if not choice:
        return
    if not choice.isdigit() or not 1 <= int(choice) <= len(player.inventory):
        print("Invalid inventory selection.")
        return
    use_item(player, player.inventory[int(choice) - 1])
