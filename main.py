import random
import time
import rpg

rpg.title()

Player = rpg.start()
answer = rpg.introduction(Player.name, Player.special)

if (answer == 'y'):
    pass

else:
    print("Another time then, mate.\n")
    exit(0)

print(Player)