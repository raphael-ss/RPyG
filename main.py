import random
import time
import rpg
import os

rpg.transition()

Player = rpg.start()
rpg.transition()
answer = rpg.introduction(Player.name, Player.special)

if (answer == 'y'):
    rpg.mission_accepted(Player.name, Player.special)

else:
    print("Another time then, mate.\n")
    exit(0)

time.sleep(10.0)
rpg.transition()
print(Player)
time.sleep(4.0)

rpg.location_0(Player)
Player.next_location()
Player.next_floor()

#-LOCATION 01
#-FLOOR ONE
Monster_1, Monster_2, Monster_3 = rpg.Monster(20), rpg.Monster(25), rpg.Monster(30)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR TWO
Monster_1, Monster_2, Monster_3 = rpg.Monster(30), rpg.Monster(35), rpg.Monster(40)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR THREE
Monster_1, Monster_2, Monster_3 = rpg.Monster(40), rpg.Monster(45), rpg.Monster(45)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.finished_location()
Player.next_location()
#-LOCATION 2
Player.next_floor()
#-FLOOR ONE
Monster_1, Monster_2, Monster_3 = rpg.Monster(50), rpg.Monster(55), rpg.Monster(60)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR TWO
Monster_1, Monster_2, Monster_3 = rpg.Monster(70), rpg.Monster(75), rpg.Monster(80)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR THREE
Monster_1, Monster_2, Monster_3 = rpg.Monster(80), rpg.Monster(85), rpg.Monster(90)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.finished_location()
Player.next_location()
#-LOCATION 3
Player.next_floor()
#-FLOOR ONE
Monster_1, Monster_2, Monster_3 = rpg.Monster(90), rpg.Monster(90), rpg.Monster(90)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR TWO
Monster_1, Monster_2, Monster_3 = rpg.Monster(100), rpg.Monster(105), rpg.Monster(110)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

Player.next_floor()
#-FLOOR THREE
Monster_1, Monster_2, Monster_3 = rpg.Monster(110), rpg.Monster(110), rpg.Monster(120)
rpg.floor(Player, Monster_1, Monster_2, Monster_3)

rpg.boss(Player)



