import random
import time
import rpg

name = input("Tell me your name, traveler: ")

rpg_class = input("What is it that you do? ")

player = rpg.Player(name, rpg_class)
player.initialize()
print(player)