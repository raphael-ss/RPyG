import time 
import random as rd
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
    intro = """
\nSo, {name}... This is the start of your journey at RPyG.\n
Now, I, the ancient Moldan, shall conduct you to your next mission.\n
For centuries... Our people, the Loeppe's Dwarves, have been tormented with the tirany and wrath of the evil Lediv, the Devil.\n
Now, in behalf of my name, Moldan, the ancient wise elder in the Loeppe's village, we have contracted you, {name}, to exterminate all the monsters in the area, and, of course, Lediv, the Devil.\n
""".format(name=name, rpg_class=rpg_class)
    for letter in intro:
        if letter == '\n':
            time.sleep(2.0)
            print(letter, end="")
        else:
            time.sleep(0.2)
            print(letter, end="")

    answer = input("Do you accept the mission we presented to you? (y/n) ")
    return answer

def title():
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
    return

def start():
    print("------------------------------------------------")
    print("Hello there. This is a text-based RPG adventure.")
    rpg_class = input("""There are 4 Classes in RPyG:
                      1. The Knight:
                      - Strong Vitality
                      - Honorable Warrior
                      - Special Attack: Berserk Rage (20 DP)
                      - 2 Rounds to Recharge

                      2. The Mage
                      - High Wisdom
                      - Ancient Monk
                      - Special Attack: Mega FireBall (35 DP)
                      - 3 Rounds to Recharge

                      3. The Thief
                      - Quick Thinking
                      - Young Slick Kid
                      - Special Attack: Murderous Intention (30 DP)
                      - 3 Rounds to Recharge

                      4. The Ninja
                      - Sharpened Abilities
                      - Mature Samurai
                      - Special Attack: Spiraling Katana (40 DP)
                      - 4 Rounds to Recharge
                      Choose your class: """)
    
    rpg_class = rpg_class.lower()
    if (rpg_class != "ninja") and (rpg_class != "knight") and (rpg_class != "mage") and (rpg_class != "thief"):
        rpg_class = "peasant"
    
    print(f"\n\tYou chose {rpg_class.title()}. Good choice.")
    name = input(f"\tNow, lastly, tell me your first name, {rpg_class.title()}: ")

    name = name.title()

    player = Player(name, rpg_class)

    player.initialize()

    return player
    

class Player:
    current_weapon = "Skinny Fists"
    special_abilitie = "None"
    special_abilitie_damage = 0
    special_abilitie_recharge_time = 0
    def __init__(self, name="Player", rpg_class="peasant"):
        self.level = 0
        self.name = name
        self.hp = 100
        self.exp = 0
        self.weapons = {}
        self.potions = {}
        self.special = rpg_class

    def initialize(self):
        self.potions["Health Potion (weak)"] = [1, 10]
        if self.special == "peasant":
            self.weapons["Skinny Fists"] = 1

        elif self.special != "peasant":
            if self.special == "knight":
                self.weapons["Unsharpened Sword"] = 5
                self.hp += 10
                Player.special_abilitie = "Berserk Rage"
                Player.special_abilitie_damage = 20
                Player.special_abilitie_recharge_time = 2
                Player.current_weapon = "Unsharpened Sword"
                
            elif self.special == "mage":
                self.weapons["Broken Wand"] = 4
                self.hp += 5
                Player.special_abilitie = "Mega FireBall"
                Player.special_abilitie_damage = 35
                Player.special_abilitie_recharge_time = 3
                Player.current_weapon = "Broken Wand"

            elif self.special == "thief":
                self.weapons["Rusted Dagger"] = 3
                self.hp += 5
                Player.special_abilitie = "Murderous Intention"
                Player.special_abilitie_damage = 30
                Player.special_abilitie_recharge_time = 3
                Player.current_weapon = "Rusted Dagger"

            elif self.special == "ninja":
                self.weapons["Chipped Katana"] = 6
                self.hp += 10
                Player.special_abilitie = "Spiraling Katana"
                Player.special_abilitie_damage = 40
                Player.special_abilitie_recharge_time = 4
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
        
class Monster:
    monster_names = ["Jirk", "Borl", "Hugat", "Rater", "Nadimr", "Ryat", "Fje", "Laqo", "Zirlq", "Kamr"]

    def __init__(self, hp):
        self.hp = hp
        self.name = rd.choice(Monster.monster_names)
        self.damage = hp//3

    def __repr__(self):
        return "{name}, the Monster has appeared!\nIt has {hp} health points, and it causes {damage} damage points!".format(name=self.name, hp=self.hp, damage=self.damage)
    


    