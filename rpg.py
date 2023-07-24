import time 
import random as rd
import os

devil = """\033[1;31m
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
    print(f"\033[0;33mSo, {name}... This is the start of your journey at RPyG.\n")
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
    print("\033[0;36m _______ _    _ ______   _____  _____        _____   ")
    time.sleep(0.3)
    print("\033[0;36m|__   __| |  | |  ____| |  __ \|  __ \      / ____| ")
    time.sleep(0.3)
    print("\033[0;36m   | |  | |__| | |__    | |__) | |__) |   _| |  __     ")
    time.sleep(0.3)
    print("\033[0;36m   | |  |  __  |  __|   |  _  /|  ___/ | | | | |_ |    ")
    time.sleep(0.3)
    print("\033[1;36m   | |  | |  | | |____  | | \ \| |   | |_| | |__| |    ")
    time.sleep(0.3)
    print("\033[1;36m   |_|  |_|  |_|______| |_|  \_\_|    \__ | \_____|    ")
    time.sleep(0.3)
    print("\033[1;36m                                        __/ |       ")
    time.sleep(0.3)
    print("\033[1;37m                                       |___/        ")
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
    print("""\033[22;32m
          
            MENU
#############################
# (1) View Status           #
# (2) Show Potions          #
# (3) Level Up              #
# (4) Change Name           #
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
    current_floor = 0
    locations = ["The Loeppe's Village", "The Abandoned Dark Castle", "The Tyran Wizard Dungeon", "Lediv's Lair "]
    def __init__(self, name="Player", rpg_class="peasant"):
        self.level = 1
        self.name = name
        self.hp = 150
        self.exp = 0
        self.weapons = {}
        self.potions = {}
        self.special = rpg_class
        self.dead = 0
        self.max_hp = self.hp

    def initialize(self):
        self.potions["Health Potion (weak)"] = [1, 10]
        self.current_location = 0
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
        return """\033[1;36m
----------------------------------------------
           # {name}, the {rpg_class} #
                       
->  HP: {HP}                                          
->  EXP: {EXP}                                       
->  LEVEL: {LEV}                                   
->  CURRENT WEAPON: {WEAPON}   
->  SPECIAL ABILITIE: {SPECIAL}                                                              
----------------------------------------------
""".format(name=self.name, rpg_class=self.special.title(), HP=self.hp, EXP=self.exp, LEV=self.level, WEAPON=Player.current_weapon, SPECIAL=Player.special_abilitie)
    
    def add_potion(self, potion:str, hp:int):
        if (potion in self.potions.keys()):
                self.potions[potion][0] += 1
        else:
            self.potions[potion] = [1, hp]

    def level_up(self):
        if (self.exp >= 100):
            self.exp -= 100
            self.level += 1
            
            self.add_potion("Health Potion (weak)", 10)

            if self.special == "peasant":
                self.weapons["Skinny Fists"] += 5

            elif self.special != "peasant":
                if self.special == "knight":
                    self.weapons["Unsharpened Sword"] += 10
                    self.max_hp += 50
                    self.hp += self.max_hp
                    self.special_abilitie_damage += 15
                    #Player.current_weapon = "Unsharpened Sword"
                    
                elif self.special == "mage":
                    self.weapons["Broken Wand"] += 10
                    self.max_hp += 50
                    self.hp += self.max_hp
                    self.special_abilitie_damage += 15
                    #Player.current_weapon = "Broken Wand"

                elif self.special == "thief":
                    self.weapons["Rusted Dagger"] += 10
                    self.max_hp += 50
                    self.hp += self.max_hp
                    self.special_abilitie_damage += 15
                    #Player.current_weapon = "Rusted Dagger"

                elif self.special == "ninja":
                    self.weapons["Chipped Katana"] += 10
                    self.max_hp += 50
                    self.hp += self.max_hp
                    self.special_abilitie_damage += 15
                    #Player.current_weapon = "Chipped Katana"

            print("\033[1;32mLeveling Up...")
            time.sleep(2.0)
            print("\033[1;32m[#.........]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[##........]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[###.......]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[####......]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[#####.....]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[######....]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[#######...]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[########..]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[#########.]")
            time.sleep(0.8)
            print ("\033[A\033[A")
            print("\033[1;32m[##########]")
            time.sleep(0.8)
            print("\033[1;32mLeveling Succesful!")
            time.sleep(2.5)

        else:
            print(f"Not enough EXP to level up! You still need {100-self.exp} EXP.")

    def next_location(self):
        self.current_location += 1
        self.hp += 50
        print(f"You left {self.locations[self.current_location-1]} and moved to {self.locations[self.current_location]}.\n")
        self.add_potion("Health Potion (strong)", 30)
        
    def reduce_health(self, DP:int):
        self.hp -= DP
        if self.hp <= 0:
            self.dead = 1

    def use_potion(self, potion:str):
        if potion in self.potions.keys():
            if self.potions[potion][0] > 0: 
                self.potions[potion][0] -= 1
                if potion == "Health Potion (weak)":
                    self.hp += 10
                elif potion == "Health Potion (medium)":
                    self.hp += 20
                else:
                    self.hp += 30
        return

    def finished_location(self):
        print(f"You just cleaned {self.locations[self.current_location]}. Congrats!")
        return
    
# Returns the Damage Points (integer) that the selected attack causes
    def attack(self):
        if self.recharge > 0: self.recharge -= 1
        flag = True
        while(flag):
            id = input("\033[1;37mSelect your attack (s - special / a - normal attack): ")
            id = id.lower()
            if id == "s":
                if self.recharge == 0:
                    self.recharge = self.special_abilitie_recharge_time
                    flag = False
                    print(f"\033[1;31m{self.name} dealed {self.special_abilitie_damage} damage points!")
                    return self.special_abilitie_damage
                else:
                    if self.recharge == 1:
                        print(f"\033[1;37mYou can't use the special abilitie for another {self.recharge} round!")
                    else:
                        print(f"\033[1;37mYou can't use the special abilitie for another {self.recharge} rounds!")                  

            
            elif id == "a":
                flag = False
                print(f"\033[1;31m{self.name} dealed {self.weapons[self.current_weapon]} damage points!")
                return self.weapons[self.current_weapon]
    
    def next_floor(self):
        if self.current_floor == 0 or self.current_floor > 3:
            self.current_floor = 1
            self.hp += 15
            print("\033[1;37mYou just entered floor 1.\n")
            return
        else:
            self.current_floor += 1
            self.hp += 15
            print(f"\033[1;37mYou just entered floor {self.current_floor}.\n")
            return

    def show_potions(self):
        print("\033[1;35m--- Items in your Awesome Bag: ---")
        for potion in self.potions.keys():
            print(f"{potion}: {self.potions[potion][1]} HP. {self.potions[potion][0]} available.")

    def select_option(self):
        op1 = input("\033[1;37mType (w) to move on or (m) to see the menu: ")
        if op1 == "w":
            return "w"
        else: 
            print_menu()
            op2 = input("\033[1;37mChoose an option from the menu: ")
            if op2 == "1":
                print(self)
                return "m"
            elif op2 == "2":
                self.show_potions()
                potion = input("\033[1;37mType (n) to leave, (1) to use Health Potion (weak), (2) to use (medium) or (3) to use (strong): ")
                if potion == "n":
                    return "m"
                elif potion == "1":
                    self.use_potion("Health Potion (weak)")
                    print(f"{self.name} used Health Potion (weak). 10 HP added.")
                    return "m"
                elif potion == "2":
                    self.use_potion("Health Potion (medium)")
                    print(f"{self.name} used Health Potion (medium). 20 HP added.")
                    return "m"
                elif potion == "3":
                    self.use_potion("Health Potion (strong)")
                    print(f"{self.name} used Health Potion (strong). 30 HP added.")
                    return "m"
                else:
                    print("\033[1;37mNot an option!")
                    return 'm'
            elif op2 == "3":
                self.level_up()
                return "m"
            
            elif op2 == "4":
                self.name = input("\033[1;37mType in your new name: ")
                self.name = self.name.title()
                return "m"
            
            else:
                print("\033[1;37mNot an option!")
                return "m"
                    

class Monster:
    monster_names = ["Jirk", "Borl", "Hugat", "Rater", "Nadimr", "Ryat", "Fje", "Laqo", "Zirlq", "Kamr"]
    drop_loot = {"Health Potion (weak)": 10, "Health Potion (weak)": 10, "Health Potion (weak)": 10, "Health Potion (medium)": 20, "Health Potion (medium)": 20,
                 "Health Potion (medium)": 20, "Health Potion (strong)": 30, "Health Potion (strong)": 30}
    def __init__(self, hp, boss=False):
        self.hp = hp
        self.boss = boss
        if boss == False: 
            self.name = rd.choice(Monster.monster_names)
        else:
            self.name = "Lediv, the Devil"
        self.damage = hp//3
        self.active = 1

    def __repr__(self):
        if self.boss == False: 
            return "\033[1;34m{name}, the Monster has appeared!\nIt has {hp} health points, and it causes {damage} damage points!".format(name=self.name, hp=self.hp, damage=self.damage)
        else:
            return "\033[1;31m{name} has appeared!\nIt has {hp} health points, and it causes {damage} damage points!".format(name=self.name, hp=self.hp, damage=self.damage)
    
    def attack(self):
        print(f"\033[1;31m{self.name} dealed {self.damage} damage points!")
        return self.damage

    def reduce_health(self, DP):
        self.hp -= DP
        if self.hp <= 0:
            self.active = 0




def round(Player:Player, Monster:Monster):
    dp = Player.attack()
    Monster.reduce_health(dp)
    if Monster.active: dp_monster = Monster.attack()
    if Monster.active: Player.reduce_health(dp_monster)
    print("\n\033[1;32m+++ Result of Round +++")
    if not Player.dead: print("\033[1;32m{name}, the {rpg_class}: {hp} HP left.".format(name=Player.name, rpg_class=Player.special, hp=Player.hp))
    if Monster.active: print("\033[1;32m{name}, the Monster: {hp} HP left.".format(name=Monster.name, hp=Monster.hp))
    return 

def fight(Player:Player, Monster:Monster):
    round_number = 0
    while ((not Player.dead) and Monster.active):
        print(f"\n\033[1;37m--- Round {round_number+1} ---")
        round(Player, Monster)
        round_number += 1

    if not Player.dead:
        Player.monsters_defeated += 1
        Player.exp += 15
        print(f"\033[1;32m{Player.name} has won the fight!")
    
    else:
        print(f"\033[1;31mUnfortunately... {Monster.name} won the fight.")
        exit(0)

def location_0(Player:Player):
    time.sleep(0.5)
    print(f"\033[1;37mLet's move on to our next location: {Player.locations[Player.current_location+1]}")
    time.sleep(2.0)
    print("Over there, you may find monsters to battle with, so be careful.")
    time.sleep(2.0)
    print("Usually, each location is divided in 3 floors. That's all I can tell you.")
    time.sleep(3.5)
    print("Good Luck.")
    time.sleep(3.0)
    transition()
    return

def drop(Player:Player, Monster:Monster):
    drops = list(Monster.drop_loot.keys())
    loot = rd.choice(drops)
    Player.add_potion(loot, Monster.drop_loot[loot])
    print(f"\033[1;36m{Monster.name} has dropped {loot}. Added to inventory.")
    return

def floor(Player:Player, Monster_1:Monster, Monster_2:Monster, Monster_3:Monster):
    print(Monster_1)
    fight(Player, Monster_1)
    drop(Player, Monster_1)
    op = Player.select_option()
    while (op is not "w"):
        op = Player.select_option()

    print(Monster_2)
    fight(Player, Monster_2)
    drop(Player, Monster_2)
    op = Player.select_option()
    while (op is not "w"):
        op = Player.select_option()

    print(Monster_3)
    fight(Player, Monster_3)
    drop(Player, Monster_3)
    op = Player.select_option()
    while (op is not "w"):
        op = Player.select_option()

def boss(Player:Player):
    transition()
    print("Oh no...")
    time.sleep(1.5)
    print("Do you hear that?")
    time.sleep(1.5)
    print("Tum.. Tum.. Tum..")
    time.sleep(1.5)

    print(devil)

    lediv = Monster(250, True)

    print("\033[1;31mLEDIV, THE DEVIL, HAS APPEARED!!!")
    fight(Player, lediv)

    if lediv.active:
        transition()
        print("Sadly, you have lost. Try again later!")
    else:
        transition()
        print("Congratulations! You beated Lediv, the Devil!")
        print("I'm sure our people will really appreciate this act of heroism.")
        time.sleep(2.0)
        print(f"Until we meet again, {Player.name}, the {Player.special}.")
        time.sleep(3.5)
        transition()
        

    

