from colorama import Fore, Style, init
from player import Player
from database import load_save, save_game
from world_map import display_map, can_move, symbol_at
from npc import Elder, Healer, Merchant, Guard, Seer
from shop import visit_shop
from quest import show_quests, advance_main
from monster import random_monster, Bandit, Dragon
from combat import battle
from skill import Fireball, Heal

init(autoreset=True)

class Game:
    def __init__(self, username):
        self.username = username
        self.player = Player(username, load_save(username))
        self.pending_bandit_reward = False
        self.npcs = {
            "E": Elder(), "H": Healer(), "M": Merchant(),
            "G": Guard(), "S": Seer()
        }
        print(Fore.CYAN + "\nSTORY: The kingdom of Asterfall is fading. The Shattered Crown once held an ancient dragon beneath the mountain. Its seal is failing, and you are the last traveler brave enough to seek the fragments.")

    def save(self):
        save_game(self.username, self.player.to_dict())
        print(Fore.GREEN + "Game saved.")

    def interact(self):
        symbol = symbol_at(self.player)
        npc = self.npcs.get(symbol)
        if npc:
            npc.talk(self)
            if symbol == "M":
                visit_shop(self.player)
            if symbol == "S" and "Fireball" not in self.player.skills:
                self.player.skills.append("Fireball")
                print("The Seer teaches you Fireball!")
            if symbol == "G" and self.pending_bandit_reward:
                # Reward is granted only after the bandit flag is set by combat.
                if getattr(self, "bandit_defeated", False):
                    from quest import complete_side
                    complete_side(self.player, "bandits", 25, 30)
                    self.bandit_defeated = False
        elif self.player.map_name == "woods" and symbol == "D":
            if self.player.quest_progress["main"] >= 3:
                boss = Dragon()
                if battle(self.player, boss):
                    self.player.quest_progress["main"] = 4
                    print(Fore.YELLOW + "THE ASHEN DRAGON FALLS. The Crown is restored, and Asterfall is free. YOU WIN!")
                    self.save()
                    return True
            else:
                print("A sealed doorway blocks the lair. Advance the main quest first.")
        else:
            print("There is nothing here to interact with.")
        return False

    def run(self):
        while True:
            if self.player.quest_progress["main"] == 0:
                print("Tip: find Elder Rowan (E) in the village and interact with him.")
            display_map(self.player)
            print("\nW/A/S/D move | I inventory | C character | Q quests | T talk/interact | B explore | F learn Heal | SAVE | X logout")
            command = input("> ").strip().lower()
            if command in ("w", "a", "s", "d"):
                dx, dy = {"w": (0,-1), "s": (0,1), "a": (-1,0), "d": (1,0)}[command]
                x, y = self.player.position[0] + dx, self.player.position[1] + dy
                if can_move(self.player.map_name, x, y):
                    self.player.position = [x, y]
                else:
                    print("A wall blocks your way.")
            elif command == "i":
                from inventory import show_inventory
                show_inventory(self.player)
            elif command == "c":
                self.player.show_status()
            elif command == "q":
                show_quests(self.player)
            elif command == "t":
                if self.interact():
                    return
            elif command == "b":
                self.explore()
            elif command == "f":
                if "Heal" not in self.player.skills:
                    self.player.skills.append("Heal")
                    print("You learned Heal!")
                else:
                    print("You already know Heal.")
            elif command == "save":
                self.save()
            elif command == "x":
                self.save()
                print("Logged out.")
                return
            else:
                print("Unknown command. Try one of the listed commands.")

    def explore(self):
        if self.player.map_name == "village":
            print("You travel to the Whispering Woods.")
            self.player.map_name, self.player.position = "woods", [1,1]
        else:
            print("You return to the village.")
            self.player.map_name, self.player.position = "village", [1,1]
        if self.player.map_name == "woods":
            monster = random_monster()
            won = battle(self.player, monster)
            if won:
                if self.player.quest_progress["main"] == 1:
                    advance_main(self.player)
                if monster.name == "Bandit":
                    self.bandit_defeated = True
                    if self.player.quest_progress["main"] == 2:
                        advance_main(self.player)
                if not self.player.quest_progress["herbs"]:
                    # A victory represents finding useful herbs on the trail.
                    from quest import complete_side
                    complete_side(self.player, "herbs", 10, 10)
