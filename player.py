class Player:
    def __init__(self, username, data=None):
        data = data or {}
        self.username = username
        self.name = data.get("name", username)
        self.level = data.get("level", 1)
        self.xp = data.get("xp", 0)
        self.gold = data.get("gold", 20)
        self.max_hp = data.get("max_hp", 30)
        self.hp = data.get("hp", self.max_hp)
        self.inventory = data.get("inventory", ["Small Potion"])
        self.skills = data.get("skills", ["Strike"])
        self.cooldowns = data.get("cooldowns", {})
        self.map_name = data.get("map_name", "village")
        self.position = data.get("position", [1, 1])
        self.quest_progress = data.get("quest_progress", {
            "main": 0, "herbs": False, "bandits": False
        })

    def to_dict(self):
        return {
            "name": self.name, "level": self.level, "xp": self.xp,
            "gold": self.gold, "max_hp": self.max_hp, "hp": self.hp,
            "inventory": self.inventory, "skills": self.skills,
            "cooldowns": self.cooldowns, "map_name": self.map_name,
            "position": self.position, "quest_progress": self.quest_progress
        }

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.level * 30:
            self.xp -= self.level * 30
            self.level += 1
            self.max_hp += 8
            self.hp = self.max_hp
            print(f"LEVEL UP! You are now level {self.level}. Max HP increased.")

    def show_status(self):
        print(f"\n{self.name} | Level {self.level} | HP {self.hp}/{self.max_hp}")
        print(f"XP: {self.xp}/{self.level * 30} | Gold: {self.gold}")
        print("Skills:", ", ".join(self.skills))
        print("Inventory:", ", ".join(self.inventory) if self.inventory else "(empty)")
