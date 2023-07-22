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
time.sleep(6.5)
Monster_1 = rpg.Monster(20)
print(Monster_1)
rpg.fight(Player, Monster_1)