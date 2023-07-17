class Player:
    current_weapon = "Skinny Fists"
    special_abilitie = "None"
    special_abilitie_damage = 0
    special_abilitie_recharge_time = 0
    def __init__(self, name="Player", rpg_class="Peasant"):
        self.level = 0
        self.name = name
        self.hp = 100
        self.exp = 0
        self.weapons = {}
        self.potions = {}
        self.special = rpg_class

    def initialize(self):
        self.potions["Health Potion (weak)"] = 10
        if self.special == "Peasant":
            self.weapons["Skinny Fists"] = 1

        elif self.special != "Peasant":
            if self.special == "Knight":
                self.weapons["Unsharpened Sword"] = 5
                self.hp += 10
                Player.special_abilitie = "Berserk Rage"
                Player.special_abilitie_damage = 20
                Player.special_abilitie_recharge_time = 2
                Player.current_weapon = "Unsharpened Sword"
                
            elif self.special == "Mage":
                self.weapons["Broken Wand"] = 4
                self.hp += 5
                Player.special_abilitie = "Mega FireBall"
                Player.special_abilitie_damage = 35
                Player.special_abilitie_recharge_time = 3
                Player.current_weapon = "Broken Wand"

            elif self.special == "Thief":
                self.weapons["Rusted Dagger"] = 3
                self.hp += 5
                Player.special_abilitie = "Murderous Intention"
                Player.special_abilitie_damage = 30
                Player.special_abilitie_recharge_time = 3
                Player.current_weapon = "Rusted Dagger"

            elif self.special == "Ninja":
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
""".format(name=self.name, rpg_class=self.special, HP=self.hp, EXP=self.exp, LEV=self.level, WEAPON=Player.current_weapon, SPECIAL=Player.special_abilitie)
    


