import random

class Monster:
    def __init__(self, name, hp, attack, xp, gold, drops=None):
        self.name, self.hp, self.max_hp = name, hp, hp
        self.attack, self.xp, self.gold = attack, xp, gold
        self.drops = drops or []
    def take_turn(self, player):
        damage = random.randint(max(1, self.attack - 2), self.attack + 2)
        player.hp -= damage
        print(f"{self.name} hits you for {damage} damage.")

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 16, 5, 12, 7, ["Small Potion"])

class Wolf(Monster):
    def __init__(self):
        super().__init__("Wolf", 20, 6, 15, 9, ["Small Potion"])

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 24, 7, 18, 12, ["Iron Charm"])

class Bandit(Monster):
    def __init__(self):
        super().__init__("Bandit", 28, 8, 22, 16, ["Large Potion"])

class Dragon(Monster):
    def __init__(self):
        super().__init__("The Ashen Dragon", 85, 11, 150, 100, ["Dragon Scale"])

def random_monster():
    return random.choice([Goblin, Wolf, Skeleton, Bandit])()
