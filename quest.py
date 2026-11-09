def show_quests(player):
    q = player.quest_progress
    print("\nMAIN QUEST: The Shattered Crown")
    steps = [
        "Speak with Elder Rowan",
        "Defeat a monster in the Whispering Woods",
        "Defeat a Bandit and recover a crown fragment",
        "Defeat the Ashen Dragon"
    ]
    for i, step in enumerate(steps):
        mark = "✓" if q["main"] > i else " "
        print(f"[{mark}] {i+1}. {step}")
    print("SIDE QUEST: Herbal Remedy -", "Complete" if q["herbs"] else "Find a herb bundle (win a forest battle).")
    print("SIDE QUEST: Road Trouble -", "Complete" if q["bandits"] else "Defeat a bandit.")

def advance_main(player, amount=1):
    player.quest_progress["main"] = min(3, player.quest_progress["main"] + amount)

def complete_side(player, key, reward_gold, reward_xp):
    if not player.quest_progress[key]:
        player.quest_progress[key] = True
        player.gold += reward_gold
        player.gain_xp(reward_xp)
        print(f"Side quest completed! Reward: {reward_gold} gold and {reward_xp} XP.")
