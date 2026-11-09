from skill import SKILL_CLASSES

def battle(player, monster):
    print(f"\nA {monster.name} appears!")
    while player.hp > 0 and monster.hp > 0:
        print(f"\nYour HP: {player.hp}/{player.max_hp} | {monster.name}: {max(0, monster.hp)} HP")
        print("Skills:", ", ".join(player.skills))
        choice = input("Choose skill (or 'item' to use potion): ").strip()
        if choice.lower() == "item":
            from inventory import show_inventory
            show_inventory(player)
            if player.hp <= 0:
                break
            continue
        if choice not in player.skills or choice not in SKILL_CLASSES:
            print("That skill is not available.")
            continue
        skill = SKILL_CLASSES[choice]()
        remaining = player.cooldowns.get(choice, 0)
        if remaining > 0:
            print(f"{choice} is on cooldown for {remaining} more turn(s).")
            continue
        skill.use(player, monster)
        for key in list(player.cooldowns):
            player.cooldowns[key] = max(0, player.cooldowns[key] - 1)
        if skill.cooldown:
            player.cooldowns[choice] = skill.cooldown
        if monster.hp > 0:
            monster.take_turn(player)
    if player.hp <= 0:
        print("You were defeated and wake up safely in the village.")
        player.hp = max(1, player.max_hp // 2)
        player.map_name, player.position = "village", [1, 1]
        return False
    print(f"You defeated {monster.name}!")
    player.gold += monster.gold
    player.gain_xp(monster.xp)
    print(f"Gained {monster.xp} XP and {monster.gold} gold.")
    if monster.drops:
        import random
        if random.random() < 0.55:
            drop = random.choice(monster.drops)
            player.inventory.append(drop)
            print(f"Monster dropped: {drop}")
    return True
