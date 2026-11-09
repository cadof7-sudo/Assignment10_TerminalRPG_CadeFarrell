class Skill:
    name = "Skill"
    cooldown = 0
    def use(self, player, monster):
        raise NotImplementedError

class Strike(Skill):
    name = "Strike"
    cooldown = 0
    def use(self, player, monster):
        damage = 5 + player.level * 2
        monster.hp -= damage
        print(f"You strike for {damage} damage.")

class Fireball(Skill):
    name = "Fireball"
    cooldown = 2
    def use(self, player, monster):
        damage = 12 + player.level * 3
        monster.hp -= damage
        print(f"Fireball hits for {damage} damage!")

class Heal(Skill):
    name = "Heal"
    cooldown = 3
    def use(self, player, monster):
        amount = 12 + player.level * 2
        before = player.hp
        player.hp = min(player.max_hp, player.hp + amount)
        print(f"You recover {player.hp - before} HP.")

SKILL_CLASSES = {c.name: c for c in (Strike, Fireball, Heal)}
