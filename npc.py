from quest import advance_main, complete_side

class NPC:
    def __init__(self, name, dialogue):
        self.name, self.dialogue = name, dialogue
    def talk(self, game):
        print(f"\n{self.name}: {self.dialogue}")

class Elder(NPC):
    def __init__(self):
        super().__init__("Elder Rowan", "The Crown was broken to seal the dragon. Follow the old road, gather strength, and end the threat.")
    def talk(self, game):
        super().talk(game)
        if game.player.quest_progress["main"] == 0:
            advance_main(game.player)
            print("Main quest updated: the Elder has entrusted you with the journey.")

class Healer(NPC):
    def __init__(self):
        super().__init__("Mira the Healer", "The woods are sick with shadow. Bring back experience, and remember that a potion can save a journey.")
    def talk(self, game):
        super().talk(game)
        if not game.player.quest_progress["herbs"]:
            complete_side(game.player, "herbs", 15, 20)

class Merchant(NPC):
    def __init__(self):
        super().__init__("Tobin the Merchant", "I trade in useful supplies. Take a look at my shop.")

class Guard(NPC):
    def __init__(self):
        super().__init__("Captain Vale", "Bandits have taken the eastern road. Someone needs to stop them.")
    def talk(self, game):
        super().talk(game)
        if not game.player.quest_progress["bandits"]:
            print("Defeat a Bandit, then return to me for your reward.")
            game.pending_bandit_reward = True

class Seer(NPC):
    def __init__(self):
        super().__init__("The Seer", "The dragon's lair lies beyond the woods. Only a prepared hero should enter.")
