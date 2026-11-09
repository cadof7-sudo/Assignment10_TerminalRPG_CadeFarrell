ITEMS = {
    "Small Potion": {"kind": "heal", "power": 15, "price": 8},
    "Large Potion": {"kind": "heal", "power": 35, "price": 20},
    "Iron Charm": {"kind": "bonus", "power": 5, "price": 25}
}

def use_item(player, item_name):
    if item_name not in player.inventory:
        print("You do not have that item.")
        return
    item = ITEMS.get(item_name)
    if not item:
        print("That item has no usable effect.")
        return
    if item["kind"] == "heal":
        before = player.hp
        player.hp = min(player.max_hp, player.hp + item["power"])
        print(f"Recovered {player.hp - before} HP.")
        player.inventory.remove(item_name)
    else:
        print("The charm is a keepsake and cannot be consumed.")
