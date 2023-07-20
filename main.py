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

rpg.print_menu()

print(Player)