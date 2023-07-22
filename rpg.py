import time 
import random as rd
import os

devil = """
                         . `  `. .`  ` .
                        . `     `.  ;  .`     ` .
                     .`           \   /           `.
                   .`     . - .   ( @ )   . - .     `.
                  /    .`      `.  '-'  .'      `.    \
          /\    .`    /   .--.   `-._.-'   .--.   \    `.    /\
        .`  `. /    .'  .`    `. `.   .` .`    `.  `.    \ .`  `.
      .`     .`    /   /        \  \ /  /        \   \    `.     `.
     /      /    .'   /   . ''' .\     /. ''' .   \   `.    \      \
    |    .`(    /    |   /        \   /        \   |    \    )`.    |
     \   | /  .'      \ |   /##\  |   |  /##\   | /      `.  \ |   /
      |  / | /         \\  | ###| /   \ |### |  //         \ | \  |
    .`\  | \/)       _.-'.  \##/ |     | \##/  .'-._       (\/ |  /`.
   /   | |  (      .`     `-.   /       \   .-'     `.      )  | |   \
  |  .`\ \   )               `.'         `.'               (   / /`.  |
  /\/  | |                  .'             `.                  | |  \/\
  \   / /     /            (   .-.     .-.   )            \     \ \   /
   `./ |    .`              `.(   `._.'   ).'              `.    | \ /
   / \ \   /.`\      )._           ) (           _.(      /`.\   / /  \
  /  |  `-'/   \    /  ''--.__    .' '.    __.--''  \    /   \`-'  |   \
  |   `---'/  .`'.  '.       ''--..___..--''       .'  .'`.  \`---'    |
  |    _.-/  /   |'.  '.                         .'  .'|   \  \-._     |
  /\ .`  |  /|  /   '.  ''---....._____.....---''  .'   \  |\ |   `.  /
 |  /     \/ \ |       - . _     _.---._     _ . -       \ /|/      \|
 \ /          \/            ''--._______.--''             \|         \
 .`        \                                                 /        `.
/       ;   |  `.                                       .`  |   ;       \
| (      )  /    \                  ^                  /    \  (      ) |
|  `.      / .`   `.              .` `.              .`   `. \      .`  |
\         \         `-._         /     \         _.-`         /         /
 \         \  _.-`   _  `--.__.-`       `-.__.--`  _   `-._  /         /
 |          `-._    / )   _                   _   ( \    _.-`          |
  \             `-.` (   / )    `-.___.-`    ( \   ) `.-`             /
   \      `.         /.-' / )               ( \ '-.\         .`      /
    `-._     `.     |  .-' / )  `-.___.-`  ( \ '-.  |     .`     _.-`
    /   `--._        \  .-' / )           ( \ '-.  /        _.--`  \
    |   |   \`--.._   |  .-' /  `-.___.-`  \ '-.  |   _..--`/  |    |
     `./     \ .`  `-/.__.--'               '--.__.\-`  `. /    `.  |
      |     / |_           -._            _.-            _| \    |\/
       `.  | /  ''--..__            _            __..--''  \ |  .`
       | \/  |==  ==    ''--..__/\_/ \_/\__..--''    ==  ==|  \/ \
       \     \ _==   ==   ==   / o)|-|(o \   ==   ==   ==_ /     /
       |    /|  ''--..__==  == \ (\) (/) / ==  ==__..--'' ||\    |
        \  / |      |  |''--..__\ )\_/( /__..--''   _.-'\ \\ \  /
         \|  /     /  /          \/___\/     \\ _.-'     \ \\ |/
             |    /  /  :                     \\\    @ .-'  ||
             \_.-`  /          :            : || \_.-'      \\
             /___.-`                          ||       _     \\
             | :                       :       \\     / (    ||
             /               :                  \\    =:_\   \\
             |   :                              ||     )      \\
             |         :                 :      \\          _.//
              \     /\                           \\     _.-'
              |    |  \    |\   :            |\   ||_.-'   |
              | : /   |   /  |      /|      /  |   /|     /
              \  /    \  |   \     | |     | `./  |  \   /
              | / `    |/  `. |    / \  : /    | /    \  |
              \|\ `            \  |   |  | `   \|    ` \ |
                 | `     `.     \ /   / /  `  `.     ` ||/
                 \  `        ,   \|   \ | `          ` /
                  | `.      ,    |    |/            ` |   .    .
                   \             /     \           ,`/     \  /
                    \    . - .   |     |   . - .    /     ( O  )
                     \  .`-._ . /       \ . _.-'.  /       )  (
                     \  : _.-': |       | :`-._ :  /      (    )
                     |   `- -`  \       /  `- -`   |        \ /
          )\         |    ___   |       |   ___    |         |
       )\/ (         /_.-'___'-._\     /_.-'___'-._\        /
      (  @  )       [__.-'   '-._]     [_.-'   '-.__]      |
       \( )/       /|\ _ \   /_  /     \  _\   /_  /   /|  /
           \      | /|`   | |  -_| /\  |_-  | |  ` |  | / /
       |\   |  |\/ | /.-` | |`-._\/ |  /_.-`| |`-. \ /  |/|\       /|
  /\  /  \   \ \ \ \ \-_ /   \.-'/\ \  \'-./   \ _-/ |  / / \ /\  | \
 | / |  / /\ | /  |/ /`-.\ _ /.-'\|  \ /'-.\ _ /.-`\ / | /  / | \ \ |
 \ | \ | |  \\\|  \ .`-_ // \ \ .-\  // -./ / \\ _-`.  \ | |  / / | \
 / \ / \ |  //|\  .`,`__//___\ \__/   \__/ /___\\__`,`. |/ \ / | /  |
 \ |/  |/  |/ |/ /_-_--_--_---,--.`) (`,--.---_--_--_-_\\|  \| \/   \
 / \|  /   /\ /\(_`'_`'_`'_) (____)   (____) (_`'_`'_`'_)/  /\  |   /
"""

def introduction(name, rpg_class):
    print(f"So, {name}... This is the start of your journey at RPyG.\n")
    time.sleep(2.0)
    print("Now, I, the ancient Moldan, shall conduct you to your next mission.\n")
    time.sleep(2.0)
    print("For centuries... Our people, the Loeppe's Dwarves, have been tormented with the tirany and wrath of the evil Lediv, the Devil.\n")
    time.sleep(2.0)
    print(f"Now, in behalf of my name, Moldan, the ancient wise elder in the Loeppe's village, we have contracted you, {name}, to exterminate all the monsters in the area, and, of course, Lediv, the Devil.\n")
    time.sleep(1.5)
    answer = input("Do you accept the mission we presented to you? (y/n) ")
    return answer

def transition():
    os.system("cls")
    print(" _______ _    _ ______   _____  _____        _____   ")
    time.sleep(0.3)
    print("|__   __| |  | |  ____| |  __ \|  __ \      / ____| ")
    time.sleep(0.3)
    print("   | |  | |__| | |__    | |__) | |__) |   _| |  __     ")
    time.sleep(0.3)
    print("   | |  |  __  |  __|   |  _  /|  ___/ | | | | |_ |    ")
    time.sleep(0.3)
    print("   | |  | |  | | |____  | | \ \| |   | |_| | |__| |    ")
    time.sleep(0.3)
    print("   |_|  |_|  |_|______| |_|  \_\_|    \__ | \_____|    ")
    time.sleep(0.3)
    print("                                        __/ |       ")
    time.sleep(0.3)
    print("                                       |___/        ")
    time.sleep(3.0)
    os.system("cls")
    return

def start():
    time.sleep(0.5)
    print("------------------------------------------------")
    print("Hello there. This is a text-based RPG adventure.")
    time.sleep(0.5)
    print("There are 4 Classes in RPyG:")
    time.sleep(1.0)
    print("""1. The Knight:
                      - Strong Vitality
                      - Honorable Warrior
                      - Special Attack: Berserk Rage (20 DP)
                      - 2 Rounds to Recharge""")
    time.sleep(2.0)
    print("""2. The Mage
                      - High Wisdom
                      - Ancient Monk
                      - Special Attack: Mega FireBall (35 DP)
                      - 3 Rounds to Recharge""")
    time.sleep(2.0)
    print("""3. The Thief
                      - Quick Thinking
                      - Young Slick Kid
                      - Special Attack: Murderous Intention (30 DP)
                      - 3 Rounds to Recharge""")
    time.sleep(2.0)
    print("""4. The Ninja
                      - Sharpened Abilities
                      - Mature Samurai
                      - Special Attack: Spiraling Katana (40 DP)
                      - 4 Rounds to Recharge""")
    time.sleep(1.0)

    rpg_class = input("Choose your class: ")
    
    rpg_class = rpg_class.lower()
    if (rpg_class != "ninja") and (rpg_class != "knight") and (rpg_class != "mage") and (rpg_class != "thief"):
        rpg_class = "peasant"
    
    print(f"\n\tYou chose {rpg_class.title()}. Good choice.")
    name = input(f"\tNow, lastly, tell me your first name, {rpg_class.title()}: ")

    name = name.title()

    player = Player(name, rpg_class)

    player.initialize()

    return player
    
def mission_accepted(name, rpg_class):
    print("\nAh, yes, that is what I like to hear. We thank you for your help.\n")
    time.sleep(2.5)
    print("But no more fooling around: let's begin. You have 3 regions to clear from monsters, before facing Lediv, the Devil.\n")
    time.sleep(2.5)
    print("Exterminating the monsters from those regions will help you gather the strength and ability required to defeat Lediv, the Devil.\n")
    time.sleep(2.5)
    print(f"Again: we thank you, {name}, the {rpg_class}. It shall be a tormented path, but surely, it will be for a good cause.\n")
    time.sleep(2.5)
    return

def print_menu():
    print("""\033[22;35m
          
            MENU
#############################
# (1) View Status           #
# (2) Change Current Weapon #
# (3) Use Potion            #
# (4) Level Up              #
# (5) Change Name           #
#############################""")
    return

class Player:
    current_weapon = "Skinny Fists"
    special_abilitie = "None"
    special_abilitie_damage = 0
    special_abilitie_recharge_time = 0
    current_location = 0
    recharge = 0
    monsters_defeated = 0
    locations = ["The Loeppe's Village", "The Abandoned Dark Castle", "The Tyran Wizard Dungeon", "Lediv's Lair "]
    def __init__(self, name="Player", rpg_class="peasant"):
        self.level = 0
        self.name = name
        self.hp = 100
        self.exp = 0
        self.weapons = {}
        self.potions = {}
        self.special = rpg_class
        self.dead = 0

    def initialize(self):
        self.potions["Health Potion (weak)"] = [1, 10]
        self.current_location = self.locations[0]
        if self.special == "peasant":
            self.weapons["Skinny Fists"] = 3

        elif self.special != "peasant":
            if self.special == "knight":
                self.weapons["Unsharpened Sword"] = 7
                self.hp += 10
                Player.special_abilitie = "Berserk Rage"
                Player.special_abilitie_damage = 20
                Player.special_abilitie_recharge_time = 2
                Player.recharge = 2
                Player.current_weapon = "Unsharpened Sword"
                
            elif self.special == "mage":
                self.weapons["Broken Wand"] = 6
                self.hp += 5
                Player.special_abilitie = "Mega FireBall"
                Player.special_abilitie_damage = 35
                Player.special_abilitie_recharge_time = 3
                Player.recharge = 3
                Player.current_weapon = "Broken Wand"

            elif self.special == "thief":
                self.weapons["Rusted Dagger"] = 5
                self.hp += 5
                Player.special_abilitie = "Murderous Intention"
                Player.special_abilitie_damage = 30
                Player.special_abilitie_recharge_time = 3
                Player.recharge = 3
                Player.current_weapon = "Rusted Dagger"

            elif self.special == "ninja":
                self.weapons["Chipped Katana"] = 7
                self.hp += 10
                Player.special_abilitie = "Spiraling Katana"
                Player.special_abilitie_damage = 40
                Player.special_abilitie_recharge_time = 4
                Player.recharge = 4
                Player.current_weapon = "Chipped Katana"
    
    def __repr__(self):
        return """
----------------------------------------------
           # {name}, the {rpg_class} #
                       
->  HP: {HP}                                          
->  EXP: {EXP}                                       
->  LEVEL: {LEV}                                   
->  CURRENT WEAPON: {WEAPON}   
->  SPECIAL ABILITIE: {SPECIAL}                                                              
----------------------------------------------
""".format(name=self.name, rpg_class=self.special.title(), HP=self.hp, EXP=self.exp, LEV=self.level, WEAPON=Player.current_weapon, SPECIAL=Player.special_abilitie)
    
    def level_up(self, weapon):
        if (self.exp >= 100):
            self.exp -= 100
            self.level += 1
            
            if ("Health Potion (weak)" in self.potions.keys()):
                self.potions["Health Potion (weak)"][0] += 1
            else:
                self.potions["Health Potion (weak)"] = [1, 10]

        if self.special == "peasant":
            self.weapons["Skinny Fists"] += 5

        elif self.special != "peasant":
            if self.special == "knight":
                self.weapons["Unsharpened Sword"] += 5
                self.hp = 120
                Player.current_weapon = "Unsharpened Sword"
                
            elif self.special == "mage":
                self.weapons["Broken Wand"] += 5
                self.hp = 115
                Player.current_weapon = "Broken Wand"

            elif self.special == "thief":
                self.weapons["Rusted Dagger"] += 5
                self.hp = 115
                Player.current_weapon = "Rusted Dagger"

            elif self.special == "ninja":
                self.weapons["Chipped Katana"] += 5
                self.hp = 120
                Player.current_weapon = "Chipped Katana"

    def next_location(self):
        self.current_location += 1
        print("You moved to {location}.\n".format(location=self.locations[self.current_location]))
        
    def reduce_health(self, DP):
        self.hp -= DP
        if self.hp <= 0:
            self.dead = 1

# Returns the Damage Points (integer) that the selected attack causes
    def attack(self):
        self.recharge -= 1
        flag = True
        while(flag):
            id = input("Select your attack (s - special / a - normal attack): ")
            id = id.lower()
            if id == "s":
                if self.recharge == 0:
                    self.recharge = self.special_abilitie_recharge_time
                    flag = False
                    print(f"{self.name} dealed {self.special_abilitie_damage} damage points!")
                    return self.special_abilitie_damage
                else:
                    if self.recharge == 1:
                        print(f"You can't use the special abilitie for another {self.recharge} round!")
                    else:
                        print(f"You can't use the special abilitie for another {self.recharge} rounds!")                  

            
            elif id == "a":
                flag = False
                print(f"{self.name} dealed {self.weapons[self.current_weapon]} damage points!")
                return self.weapons[self.current_weapon]
    


class Monster:
    monster_names = ["Jirk", "Borl", "Hugat", "Rater", "Nadimr", "Ryat", "Fje", "Laqo", "Zirlq", "Kamr"]

    def __init__(self, hp):
        self.hp = hp
        self.name = rd.choice(Monster.monster_names)
        self.damage = hp//3
        self.active = 1

    def __repr__(self):
        return "{name}, the Monster has appeared!\nIt has {hp} health points, and it causes {damage} damage points!".format(name=self.name, hp=self.hp, damage=self.damage)
    
    def attack(self):
        print(f"{self.name} dealed {self.damage} damage points!")
        return self.damage

    def reduce_health(self, DP):
        self.hp -= DP
        if self.hp <= 0:
            self.active = 0


def round(Player:Player, Monster:Monster):
    dp = Player.attack()
    Monster.reduce_health(dp)
    if Monster.active: dp_monster = Monster.attack()
    Player.reduce_health(dp_monster)
    print("\n+++ Result of Round +++")
    if not Player.dead: print("{name}, the {rpg_class}: {hp} HP left.".format(name=Player.name, rpg_class=Player.special, hp=Player.hp))
    if Monster.active: print("{name}, the Monster: {hp} HP left.\n".format(name=Monster.name, hp=Monster.hp))
    return 

def fight(Player:Player, Monster:Monster):
    round_number = 0
    while ((not Player.dead) and Monster.active):
        print(f"\n--- Round {round_number+1} ---")
        round(Player, Monster)
        round_number += 1

    if not Player.dead:
        Player.monsters_defeated += 1
        Player.exp += 15
        print(f"{Player.name} has won the fight!")
    
    else:
        print(f"Unfortunately... {Monster.name} won the fight.")
        exit(0)